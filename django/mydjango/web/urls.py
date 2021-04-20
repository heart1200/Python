from django.urls import include, path

import web.views

urlpatterns = [
    path('Hello_world', web.views.hello_world)
]