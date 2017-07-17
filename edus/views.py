from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic
from django.views.generic import CreateView, UpdateView

from . forms import EditQuestionForm
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


###i could inc/dec the number text on the frontend while backend updates

def upvote(request,pk):
    question = get_object_or_404(Question, pk=pk)
    question.points += 1
    question.voters.add(request.user.useredus)

    if request.user.useredus in question.voters.all():
        print('present')
    else:
        print('not')

    question.save()
    return HttpResponseRedirect(reverse('edus:question_detail', args=(
        question.pk,
    )))


def downvote(request,pk):
    question = get_object_or_404(Question, pk=pk)
    question.points -= 1
    question.voters.add(request.user.useredus)

    question.save()

    return HttpResponseRedirect(reverse('edus:question_detail', args=(
        question.pk,
    )))

###violated DRY??, could probably improve this

#need to pass in question pk as well??
def upvote_reply(request,pk,):
    reply = get_object_or_404(Reply, pk=pk)
    reply.points += 1
    reply.voters.add(request.user.useredus)
    reply.save()
    return HttpResponseRedirect(reverse('edus:question_detail', args=(
        reply.parent_question.pk,
    )))


def downvote_reply(request,pk,):
    reply = get_object_or_404(Reply, pk=pk)
    reply.points -= 1
    reply.voters.add(request.user.useredus)
    reply.save()
    return HttpResponseRedirect(reverse('edus:question_detail', args=(
        reply.parent_question.pk,
    )))


def correct_reply(request,pk,):
    reply = get_object_or_404(Reply, pk=pk)
    reply.correct_answer = True
    reply.save()

    parent_question = get_object_or_404(Question, pk=reply.parent_question.pk)
    parent_question.solution_found = True
    parent_question.save()


    return HttpResponseRedirect(reverse('edus:question_detail', args=(
        reply.parent_question.pk,
    )))

#login mixin can be added here
class ReplyCreate(CreateView):
    """
    creates a comment object
    """
    model = Reply #specify which model can be created here
    fields = ['content', ] # which fields can be openly editted

    def get_context_data(self, **kwargs):
        """
        attach parent blog so I can display it on the comment template
        """
        #refer to the super view to generate context base
        context = super(ReplyCreate, self).get_context_data(**kwargs)
        #set 'blog' to equal queryset of Blog objects matching pk
        context['question'] = get_object_or_404(Question, pk=self.kwargs['pk'])
        #this will return a blog object
        return context

    def form_valid(self, form):
        """
        add associate blog and author to form.
        """
        #this is setting the author of the form
        #this has to be in lowercase for the association to work!
        form.instance.author = self.request.user.useredus
        #associate comment with blog based on passed
        form.instance.parent_question = get_object_or_404(Question, pk = self.kwargs['pk'])
        #the super class carried the validator function
        return super(ReplyCreate, self).form_valid(form)

    def get_success_url(self):
        """
        After posting comment return to associated blog.
        """
        return reverse('edus:question_detail', kwargs={'pk': self.kwargs['pk'], })




class QuestionUpdate(UpdateView):
    model = Question
    fields = ['title', 'content']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        """
        After posting comment return to associated blog.
        """
        return reverse('edus:question_detail', kwargs={'pk': self.kwargs['pk'], })










