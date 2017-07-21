import datetime
import pytz

from django.utils import timezone


from edus.models import Question


def add_variable_to_context(request):

    # sessions are automatically tied to current user

    # set the new val to total question count
    request.session['new_question_val'] = Question.objects.count()  # set request, get # of questions
    new_question_val = request.session.get('new_question_val', 0) #create object
    old_question_val = request.session.get('old_question_val', 0) #create object using val set in QuestionListView

    # compare values
    if old_question_val < new_question_val:
        return {
            'new_questions': 'true'
        }
    else:
        return {
            'new_questions': 'false'
        }












