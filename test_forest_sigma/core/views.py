from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
# @login_required


@login_required
def index(request):
    return render(request, "account/base.html")

def question(request, id):
    # fetch data from database for the index given
    context = {'id': id }
    return render(request, 'account/question.html', context)
