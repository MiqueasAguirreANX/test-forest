from json import dumps
import json
from django.core.paginator import Paginator
import random
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Question, Answer, Randomized
from django.http import JsonResponse
from django.shortcuts import HttpResponse, HttpResponseRedirect, render

# Create your views here.
# @login_required


@login_required
def index(request):
    answers = Answer.objects.filter(user=request.user)
    if len(answers) == 33:
        return redirect('core:visualize')
    else:
        questions = Question.objects.all()
        # question_list = []
        # for i in questions:
        #     question_list.append(i)
        # try:
        #     isRandom = Randomized.objects.get(user=request.user, random=True)
        # except:
        #     isRandom = Randomized(user=request.user, random=True)
        #     isRandom.save()
        #     random.shuffle(question_list)
        page = request.GET.get('page', 1)
        paginator = Paginator(questions, 1)
        try:
            page_obj = paginator.page(page)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)
        return render(request, "question.html", {'page_obj': page_obj, "pagination": "true"})


@login_required
def submitAns(request, question_id, answers):
    question = Question.objects.get(pk=question_id)
    try:
        answer = Answer.objects.get(
            user=request.user, question=question)
        answer.answer = int(answers)
        print('answers', answer)
        answer.save()
        return JsonResponse({"status": "updated"})
    except:
        answer = Answer(user=request.user, question=question,
                        answer=int(answers))
        print('answer', answer)
        answer.save()
        return JsonResponse({
            "status": "added"
        })
    return JsonResponse({
        "error": "SomeThing Went Wrong"
    })


@login_required
def visualize(request):
    answers = Answer.objects.filter(user=request.user)
    if len(answers) < 21:
        return redirect('core:requestions')
    ans_scores_1, ans_scores_2 = [], []
    subscale_score_dict = {}
    # For 2 subscales for now - will update during delievering to client for 36 subscales
    for ans in answers:
        if ans.question.subscale == "1":
            ans_scores_1.append(ans.answer)
        elif ans.question.subscale == "2":
            ans_scores_2.append(ans.answer)

    
    subscale_score_dict["1"] = sum(ans_scores_1)/len(ans_scores_1)
    subscale_score_dict["2"] = sum(ans_scores_2)/len(ans_scores_2)

    datadict = dumps(subscale_score_dict)

    return render(request, 'visualize.html', {'answers': datadict, "pagination": "false"})


@login_required
def reQuestions(request):
    questions = Question.objects.all()
    question_list = []
    for i in questions:
        question_list.append(i)
    random.shuffle(question_list)
    page = request.GET.get('page', 1)
    paginator = Paginator(question_list, 1)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return render(request, "question.html", {'page_obj': page_obj, "message": "you have not answer all the questions please answer all the questions and then submit!", "pagination": "true"})


def createSession(request, question_id, answerSelected):
    request.session[question_id] = answerSelected
    return JsonResponse({
        "status": "done",
    })


def getSession(request, question_id):
    try:
        ans = request.session[question_id]
        return JsonResponse({
            "ans": ans,
            "id": question_id
        })
    except:
        return JsonResponse({
            "error": "no session found",
        })
