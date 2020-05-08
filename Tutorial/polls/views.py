from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from django.utils import timezone
from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django_tables2 import SingleTableView

from .models import Question, Choice, Genre, Log
from .tables import GenreTable


class LogView(ListView):
    model = Log
    template_name = 'log_list.html'


class LogDetailView(DetailView):
    model = Log


class IndexView(ListView):
    template_name = 'polls/index.html'
    model = Question
    context_object_name = 'latest_question_list'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()


    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html',
                      {'question': question, 'error_message': 'You didn\'t select a choice.'})
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
