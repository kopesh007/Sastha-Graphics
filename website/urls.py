from django.urls import path
from . import views

app_name='website'

urlpatterns=[
    path("",views.home,name="home"),
    path("about/",views.about,name="about"),
    path("banner/",views.banner_page,name="banner"),
    path("invite/",views.invites,name="invitations"),
    path("art/",views.arts,name="arts"),
]