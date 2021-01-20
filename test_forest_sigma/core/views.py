from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Question, Answer
from django.http import JsonResponse
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.core.paginator import Paginator
# Create your views here.
# @login_required


@login_required
def index(request):
    if request.method == 'POST':
        return render(request, 'question.html', {"message": "you have submitted the form"})
    questions = Question.objects.all()
    paginator = Paginator(questions, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "question.html", {'page_obj': page_obj})


@login_required
def submitAns(request, question_id, answers):
    question = Question.objects.get(pk=question_id)
    try:
        answer = Answer.objects.get(
            user=request.user, question=question)
        answer.answer = int(answers)
        answer.save()
        return JsonResponse({"status": "updated"})
    except:
        answer = Answer(user=request.user, question=question,
                        answer=int(answers))
        answer.save()
        return JsonResponse({
            "status": "added"
        })
    return JsonResponse({
        "error": "SomeThing Went Wrong"
    })


# Reusable view for every question


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
