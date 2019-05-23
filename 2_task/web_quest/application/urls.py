from django.urls import path
from django.conf.urls import url

from . import app

urlpatterns = [
    path('questions', app.QuestionList.as_view(), name='questions'),
    path('questions/new', app.new_question, name='new_question'),
    url('questions/answer', app.new_answer, name='new_answer')
]
