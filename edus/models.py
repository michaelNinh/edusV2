from django.db import models
from datetime import date
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import User  # Blog author or commenter

# Create your models here.

class UserEdus(models.Model):
    #WHEN USER SIGNS UP, A USEREDUS MODEL NEEDS TO BE CREATED AND SAVED

    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    bio = models.TextField(max_length=400, help_text="Enter your bio details here.")

    # a feature like this would return the profile page?
    # def get_absolute_url(self):
    #     """
    #     Returns the url to access a particular blog-author instance.
    #     """
    #     return reverse('blogs_by_author', args=[str(self.id)])

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

    #how to include media files like pictures??

    #how to represent this in admin dashboard?
    #could do it by parent Question
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.content



#########################

class Reporter(models.Model):
    first_name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.first_name


class Article(models.Model):
    title = models.CharField(max_length=100)
    reporter = models.ForeignKey(Reporter) #a report can have many articles , but they all belong to one reporter?

    def __unicode__(self):
        return self.title






















