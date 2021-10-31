from django.conf.urls import url
from basic_app import views

app_name='basic_app'
urlpatterns=[
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^other/$',views.other,name='other'),
    url(r'^about/$',views.about,name='about'),
    url(r'^register/$',views.register,name='register'),
    url(r'^login/$',views.user_login,name='user_login'),
    url(r'^logout/$',views.user_logout,name='user_logout'),
    url(r'^special/$',views.special,name='special'),


]
