import datetime
import pytz

from django.utils import timezone


from edus.models import NewUpdateSign


def add_variable_to_context(request):
    signal_object = NewUpdateSign.objects.get(pk=1) #this is the object
    # if additional 24 hours is less than the current time


    aware_time = pytz.utc.localize(datetime.datetime.now())

    if signal_object.last_update + datetime.timedelta(hours=24) < aware_time:
        print('OLD')
        signal_object.last_update = False
        signal_object.save()
        return {
            'new_questions': 'false'
        }

    else:
        print('still fresh')

        print(signal_object.last_update)

        return {

            'new_questions': 'true'
        }




