from django.conf.urls import url
from . import views

app_name = 'edus'
urlpatterns = [

    url(r'^$', views.index, name="index"),
    url(r'^questions/$', views.QuestionListView.as_view(), name='questions'),
    url(r'^questions/(?P<pk>\d+)$', views.QuestionDetailView.as_view(), name='question_detail'),
    url(r'^questions/(?P<pk>\d+)/upvote/$', views.upvote, name='upvote'),

    ]