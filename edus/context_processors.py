import datetime
import pytz

from django.utils import timezone


from edus.models import NewUpdateSign, Question


def add_variable_to_context(request):

    # sessions are automatically tied to current user

    # new turns into old
    old_question_val = request.session.get('new_question_val', 0)

    # for setting the new question value
    request.session['new_question_val'] = Question.objects.count() #set initial request, get # of questions
    new_question_val = request.session['new_question_val'] #retrieve request


    # if increase in questions
    if old_question_val < new_question_val:
        return {
            'new_questions': 'true'
        }
    else:
        return {
            'new_questions': 'false'
        }





    # signal_object = NewUpdateSign.objects.get(pk=1) #this is the object
    # # if additional 24 hours is less than the current time
    #
    #
    # aware_time = pytz.utc.localize(datetime.datetime.now())
    #
    # if signal_object.last_update + datetime.timedelta(hours=24) < aware_time:
    #     print('OLD')
    #     signal_object.last_update = False
    #     signal_object.save()
    #     return {
    #         'new_questions': 'false'
    #     }
    #
    # else:
    #     print('still fresh')
    #
    #     print(signal_object.last_update)
    #
    # return {
    #     'new_questions': 'true'
    # }




