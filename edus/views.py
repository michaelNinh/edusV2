from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic
from django.views.generic import CreateView, UpdateView
from .forms import SignUpForm
from django.contrib.auth import login, authenticate
from . models import UserEdus, Question, Reply

def index(request):
    """
    View function for home page of site.
    """

    num_visits = request.session.get('num_visits', 0) #creating a session object, with attr

    return render(
        request,
        'index.html',
    )
# all questions
class QuestionListView(generic.ListView):
    model = Question
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(QuestionListView, self).get_context_data(**kwargs)

        # code for *NEW* notification
        new_q_val = self.request.session.get('new_question_val', 0) #get new_question_val
        self.request.session['old_question_val'] = new_q_val #set the new to the old

        context['question_list'] = Question.objects.all().order_by('-post_date')

        # get_object_or_404(Question, pk=self.kwargs['pk'])


        return context

# view for questions asked by logged in user
class MyQuestionListView(generic.ListView):
    model = Question
    paginate_by = 10
    # queryset = Question.objects.filter(author=request.user)
    template_name = 'edus/myquestion_list.html'

    def get_queryset(self):
        # THIS WILL TARGET THE LOGGED IN USER / NOT THE AUTHOR
        # self.request.user.useredus.new_replies = False
        # self.request.user.useredus.save()

        new_reply_val = self.request.session.get('new_reply_val', 0)  # get new_reply_value
        self.request.session['old_reply_val'] = new_reply_val  # set the new to the old

        return self.request.user.useredus.question_set.all().order_by('-new_replies')

# view for unanswered questions
class OpenQuestionListView(generic.ListView):
    model = Question
    paginate_by = 10
    queryset = Question.objects.filter(solution_found=False)
    template_name = 'edus/openquestion_list.html'

    #pass context data

class QuestionDetailView(generic.DetailView):
    model = Question


    def get_context_data(self, **kwargs):
        context = super(QuestionDetailView, self).get_context_data(**kwargs)

        # set Question new_replies to false after user views the details
        # parent_question = get_object_or_404(Question, pk=self.kwargs['pk']) #specify which question is being viewed
        # parent_question.new_replies = False #set to false
        # parent_question.save() #save

        return context



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
        form.instance.author = self.request.user.useredus
        #associate comment with Question based on passed
        parent_question = get_object_or_404(Question, pk= self.kwargs['pk'])
        form.instance.parent_question = parent_question
        #the super class carried the validator function

        # parent_question.author.new_replies = True  #inform the author there are new replies
        parent_question.new_replies = True  # inform the question there are new replies
        parent_question.save()

        parent_question_author = get_object_or_404(UserEdus, pk=parent_question.author.pk)
        parent_question_author.new_replies = True
        parent_question_author.save()
        print('~~~~~~~~~~')
        print(parent_question_author)
        print('~~~~~~~~~_')
        print(parent_question_author.new_replies)


        return super(ReplyCreate, self).form_valid(form)

    def get_success_url(self):
        """
        After posting comment return to associated blog.
        """
        return reverse('edus:question_detail', kwargs={'pk': self.kwargs['pk'], })

# login mixin can be inserted here
class QuestionCreate(CreateView):
    """
    creates a Question object
    """
    model = Question #specify which model can be created here
    fields = ['title', 'content','image'] # which fields can be openly editted

    # once classrooms are implemented pass that data here
    # def get_context_data(self, **kwargs):


    def form_valid(self, form):
        """
        add associate blog and author to form.
        """

        # allows for asking questions without uploading images
        if self.request.FILES == {}:
            pass
        else:
            form.instance.document = self.request.FILES['image']

        form.instance.author = self.request.user.useredus
        #once classrooms are implemented, pass in here
        # form.instance.parent_classroom etc...
        return super(QuestionCreate, self).form_valid(form)

    def get_success_url(self):
        """
        After posting comment return to associated blog.
        """
        return reverse('edus:question_detail', kwargs={'pk': self.object.pk})


class QuestionUpdate(UpdateView):
    model = Question
    fields = ['title', 'content']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        """
        After posting comment return to associated blog.
        """
        return reverse('edus:question_detail', kwargs={'pk': self.kwargs['pk'], })


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.useredus.email = form.cleaned_data.get('email')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect(reverse('edus:questions'))
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})











