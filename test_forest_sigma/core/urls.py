from django.urls import path
<<<<<<< HEAD
from core.views import index, createSession, visualize, getSession, reQuestions, submitAns
=======
from core.views import index, createSession, getSession, submitAns,visualize
>>>>>>> refs/remotes/origin/master
app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
    path('visualizing', visualize, name="visualize"),
    path('requestion', reQuestions, name="requestions"),
    # API Routes
    path('getsession/<str:question_id>', getSession, name="getsession"),
    path('createsession/<str:question_id>/<str:answerSelected>',
         createSession, name="createsession"),
    path('submitans/<question_id>/<answers>', submitAns, name="submitans"),
    path('visualize',visualize,name='visualize')
]
