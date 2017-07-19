from django.db import models
from datetime import date
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import User
from django.dispatch import receiver #for user creation
from django.db.models.signals import post_save #for user creation



# Create your models here.

class UserEdus(models.Model):
    #WHEN USER SIGNS UP, A USEREDUS MODEL NEEDS TO BE CREATED AND SAVED

    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    email = models.CharField(max_length=500, help_text="Your email", null=True)
    bio = models.TextField(max_length=400, help_text="Enter your bio details here.")

    # a feature like this would return the profile page?
    # def get_absolute_url(self):
    #     """
    #     Returns the url to access a particular blog-author instance.
    #     """
    #     return reverse('blogs_by_author', args=[str(self.id)])


    # this has to do something with extending default django User model
    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            UserEdus.objects.create(user=instance)
        instance.useredus.save()

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.user.username

class Question(models.Model):
    title = models.CharField(max_length=500, null=False)
    content = models.TextField(max_length=10000, null=False)
    author = models.ForeignKey(UserEdus, null=False)
    solution_found = models.BooleanField(default=False, null=False)
    points = models.IntegerField(default=1, null=False)
    post_date = models.DateField(default=date.today)

    voters = models.ManyToManyField(UserEdus, null=True, related_name='voters')

    image = models.ImageField(upload_to='MEDIA_ROOT/documents/', null=True, blank=True)

    #how to include media files like pictures??

    def get_absolute_url(self):
        """
        Returns the url to access a particular blog-author instance.
        """
        return reverse('question_detail', args=[str(self.pk)])

    #titles could get long...
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title


class Reply(models.Model):
    content = models.TextField(max_length=10000, null=False)
    author = models.ForeignKey(UserEdus, null=False) #what does onDelete model.CASCADE do?
    parent_question = models.ForeignKey(Question, null=True)
    correct_answer = models.BooleanField(default=False)
    points = models.IntegerField(default=1, null=False)
    post_date = models.DateField(default=date.today)

    voters = models.ManyToManyField(UserEdus, null=True, related_name='voters_reply')

    #how to include media files like pictures??

    #how to represent this in admin dashboard?
    #could do it by parent Question
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.content


# model for uploading media
class Document(models.Model):
    description = models.CharField(max_length=2000, blank=True)
    document = models.FileField(upload_to='MEDIA_ROOT/documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)



# ratchet implementation, check signal pk = 1, this is the MASTER QUESTION SIGNAL
# if new_signal == TRUE, then there are new questions
class NewUpdateSign(models.Model):
    new_signal = models.BooleanField(null=False, default=False)
    last_update = models.DateTimeField(auto_now_add=True)
    signal_id = models.CharField(null=False,blank= True, max_length= 200)

    @receiver(post_save, sender=Question)
    def update_signal(sender, instance, created, **kwargs):
        if created:
            # UserEdus.objects.create(user=instance)
            # UserEdus.objects.getObject
            try:
                print('DEBUG OBJECT FOUND')
                update_signal = NewUpdateSign.objects.get(pk=1)
                update_signal.new_signal = True
                update_signal.save()
            except NewUpdateSign.DoesNotExist:
                print('OBJECT NOT FOUND')
                # technically this should never happen
                create_master_signal = NewUpdateSign(new_signal=True, last_update= date.today(), signal_id= 'MASTER')
                create_master_signal.save()
                # raise Http404("No MyModel matches the given query.")

        # instance.newupdatesign.save()























