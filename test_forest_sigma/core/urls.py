from django.urls import path
from core.views import index, question, createSession, getSession
app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
    path('question/<id>', question, name="question"),


    # API Routes
    path('getsession/<str:question_id>', getSession, name="getsession"),
    path('createsession/<str:question_id>/<str:answerSelected>',
         createSession, name="createsession"),
]
