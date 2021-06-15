from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question,Choice
from django.urls import reverse


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    return render(request,'app1/index.html',{'latest_question_list':latest_question_list})

def detail(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request,'app1/detail.html',{'question':question})

def vote(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request,'app1/detail.html',{'question':question,'error_message': "You didn't select a choice."})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('app1:results', args=(question.id,)))


def results(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'app1/results.html',{'question':question})
    