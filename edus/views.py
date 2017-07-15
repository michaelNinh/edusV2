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


def downvote(request,pk):
    question = get_object_or_404(Question, pk=pk)
    question.points -= 1
    question.save()
    return HttpResponseRedirect(reverse('edus:question_detail', args=(
        question.pk,
    )))

###violated DRY??, could probably improve this

#need to pass in question pk as well??
def upvote_reply(request,pk,):
    reply = get_object_or_404(Reply, pk=pk)
    reply.points += 1
    reply.save()
    return HttpResponseRedirect(reverse('edus:question_detail', args=(
        reply.parent_question.pk,
    )))


def downvote_reply(request,pk,):
    reply = get_object_or_404(Reply, pk=pk)
    reply.points -= 1
    reply.save()
    return HttpResponseRedirect(reverse('edus:question_detail', args=(
        reply.parent_question.pk,
    )))
















