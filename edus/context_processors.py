import datetime
import pytz

from django.utils import timezone


from edus.models import Question


def add_variable_to_context(request):
    '''
    the following code is to display the *NEW* sign in the navigation bar. I basically look at the total number of replies and questions.
    If that number has changed, then display the *NEW* sign. Complimentary code is also placed in the 
    VIEW classes for QuestionDetail & MyQuestionList 
    could be possible to improve if there is a way for logged in user to modify other user objects? 
    '''

    # sessions are automatically tied to current user

    # evaluating reply
    # run code only if user is logged in, otherwise crash
    if request.user.is_authenticated:
        total_reply_val = 0
        # code to get to get total number of replies associate to question that are associate to current user
        question_set = request.user.useredus.question_set.all()  # get all questions related to user
        for question in question_set:
            total_reply_val += question.reply_set.count()
        print(total_reply_val)

        request.session['new_reply_val'] = total_reply_val  # update new_reply_val session
        new_reply_val = request.session.get('new_reply_val', 0)  # create object
        old_reply_val = request.session.get('old_reply_val', 0)  # create object using val set in QuestionListView

        if old_reply_val < new_reply_val:
            new_reply_flag = 'true'
        else:
            new_reply_flag = 'false'
    else:
        new_reply_flag = 'false'

    # evaluating questions
    # set the new val to total question count
    request.session['new_question_val'] = Question.objects.count()  # set request, get # of questions
    new_question_val = request.session.get('new_question_val', 0) #create object
    old_question_val = request.session.get('old_question_val', 0) #create object using val set in QuestionListView

    # compare values, why in STR? personal choice of no reasoning at all
    if old_question_val < new_question_val:
        new_question_flag = 'true'
    else:
        new_question_flag = 'false'

    #         this code is how custom tag data is read??? it's called context processing
    return {

        'new_reply_flag' : new_reply_flag,
        'new_questions_flag': new_question_flag

    }



