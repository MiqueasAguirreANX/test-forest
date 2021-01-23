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
    if len(answers) == 407:
        return redirect('core:visualize')
    else:
        questions = Question.objects.all()
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
    print('length',len(answers))
    if len(answers) < 408:
        return redirect('core:requestions')
    subscale_score_dict = {}
    # For 2 subscales for now - will update during delievering to client for 36 subscales
    subscale_list = []
    for i in range(1,37):
        subscale_list.append(str(i))
    for subscale in subscale_list:
        ans_scores = []
        for ans in answers:
            if ans.question.subscale == subscale:
                ans_scores.append(ans.answer)
            ### Editing for now only
        if len(ans_scores)!=0:
            subscale_score_dict[subscale] = sum(ans_scores)/len(ans_scores)
    
    subscale_score_dict = dict(sorted(subscale_score_dict.items(),key=lambda val:val[1],reverse=True))
    ## sorted dictionary according to scores
    subscale_names_ = list(subscale_score_dict.keys())
    subscale_dict = {'1': 'SELF-ANALYSIS', '2': 'INTUITION', '3': 'MEDITATION', '4': 'AMBITION', '5': 'PRIDE', '6': 'LEADERSHIP', '7': 'CONVERSATION', '8': 'AFFILIATION', '9': 'SOLIDARITY', '10': 'AUTONOMY', '11': 'FREEDOM', '12': 'SOLITUDE', '13': 'AMUSEMENT', '14': 'EROTICISM', '15': 'PLAYFULNESS', '16': 'ORDERLINESS', '17': 'PLANNING', '18': 'PRECISION', '19': 'INNOVATION', '20': 'ABSTRACTION', '21': 'REFLECTION', '22': 'CONFORMITY', '23': 'TRADITION', '24': 'SECURITY', '25': 'DEVOTION', '26': 'HARMONY', '27': 'RESPECT', '28': 'RESPONSE', '29': 'REVENGE', '30': 'ANGER', '31': 'TEMERITY', '32': 'ADVENTURE', '33': 'VARIETY', '34': 'JOVIALITY', '35': 'VIVACITY', '36': 'OPTIMISM'}
    subscale_names = []
    for sub in subscale_names_:
        subscale_names.append(subscale_dict[sub])
    datadict = dumps(subscale_score_dict)

    return render(request, 'visualize.html', {'answers': datadict,"subscale_names_1":subscale_names[:5],"subscale_names_2":subscale_names[5:13],"subscale_names_3":subscale_names[13:23],"subscale_names_4":subscale_names[23:31],"subscale_names_5":subscale_names[31:36], "pagination": "false"})


@login_required
def reQuestions(request):
    answers = Answer.objects.filter(user=request.user)
    question = Question.objects.all()
    question_list = []
    for i in range(0, len(question)):
        try:
            if question[i] == answers[i].question:
                pass
        except:
            question_list.append(question[i])
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
