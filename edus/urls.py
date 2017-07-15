from django.conf.urls import url
from . import views

app_name = 'edus'
urlpatterns = [

    url(r'^$', views.index, name="index"),
    url(r'^questions/$', views.QuestionListView.as_view(), name='questions'),
    url(r'^questions/(?P<pk>\d+)$', views.QuestionDetailView.as_view(), name='question_detail'),
    url(r'^questions/(?P<pk>\d+)/upvote/$', views.upvote, name='upvote'),
    url(r'^questions/(?P<pk>\d+)/downvote/$', views.downvote, name='downvote'),
    url(r'^questions/(?P<pk>\d+)/upvote_reply/$', views.upvote_reply, name='upvote_reply'),
    url(r'^questions/(?P<pk>\d+)/downvote_reply/$', views.downvote_reply, name='downvote_reply'),

    ]