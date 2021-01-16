from django.urls import path
from core.views import index, question
app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
    path('question/<id>', question, name="question")
]

