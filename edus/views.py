from django.shortcuts import render
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