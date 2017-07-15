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
    # try:
    #         selected_question = question.choice_set.get(pk=request.POST['question'])
    # except (KeyError, Question.DoesNotExist):
    #         # Redisplay the question voting form.
    #         return render(request, 'index.html', {
    #
    #         })
    # else:
    #         # See  Avoiding race conditions using F()
    #         # https://docs.djangoproject.com/en/1.9/ref/models/expressions/#avoiding-race-conditions-using-f
    #         selected_question.votes += 1
    #         selected_question.save()
    #         # Always return an HttpResponseRedirect after successfully dealing
    #         # with POST data. This prevents data from being posted twice if a
    #         # user hits the Back button.
    #         return HttpResponseRedirect(reverse('polls:question_detail', args=(
    #             question.pk,
    #         )))

#

# question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice."
#         })
#     else:
#         # See  Avoiding race conditions using F()
#         # https://docs.djangoproject.com/en/1.9/ref/models/expressions/#avoiding-race-conditions-using-f
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(
#             question.id,
#         )))












