from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from . models import UserEdus, Question, Reply



def index(request):
    """
    View function for home page of site.
    """
    # Render the HTML template index.html
    return render(
        request,
        'index.html',
    )

class QuestionListView(generic.ListView):
    model = Question
    paginate_by = 5

class QuestionDetailView(generic.DetailView):
    model = Question


def upvote(request,pk):
    question = get_object_or_404(Question, pk=pk)
    question.points += 1
    question.save()
    return HttpResponseRedirect(reverse('edus:question_detail', args=(
        question.pk,
    )))













