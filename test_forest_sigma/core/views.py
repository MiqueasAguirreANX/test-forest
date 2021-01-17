from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Question, Answer
from django.core.paginator import Paginator
# Create your views here.
# @login_required


@login_required
def index(request):
    questions = Question.objects.all()
    paginator = Paginator(questions, 11)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "question.html", {'page_obj': page_obj})


# Reusable view for every question
def question(request, id):
    if request.method == 'POST':
        # If the user push the next button, send his answer and procces it
        try:
            user_answer = int(request.POST['flexRadioDefault'])
            print(user_answer)
            print(request.username)
            if user_answer > 0 and user_answer <= 5:
                answer = Answer(user=request.username,
                                question_index=id, answer=user_answer)
                answer.save()
                # everything ok
                return redirect(f'question/{id+1}')
            else:
                # bad answer, redirect to the same page
                return redirect(f'question/{id}')
        except:
            pass

    user_question = Question.objects.filter(index=id)
    context = {'question': user_question[0], 'id': id}
    return render(request, 'account/question.html', context)
