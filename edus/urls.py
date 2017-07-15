from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.index, name="index"),
    url(r'^questions/$', views.QuestionListView.as_view(), name='questions'),
    url(r'^questions/(?P<pk>\d+)$', views.QuestionDetailView.as_view(), name='question_detail'),

    ]