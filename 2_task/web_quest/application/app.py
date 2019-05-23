from .models import Question
from django.views.generic import ListView
from django.shortcuts import render, redirect
from .QAsteps import AddQuestion, AddAnswer

class QuestionList(ListView):
    model = Question
    context_object_name = 'questions'

def new_question(request):
    if request.method == "POST":
        form = AddQuestion(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.save()
        return redirect('questions')

    form = AddQuestion()
    return render(request, 'new_question.html', {'form': form})

def new_answer(request):
    if request.method == "POST":
        form = AddAnswer(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.save()
        return redirect('questions')

    data = {
        'question': 0
    }
    form = AddAnswer(data)
    return render(request, 'answer.html', {'form': form})
