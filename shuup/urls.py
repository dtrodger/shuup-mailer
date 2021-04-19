#-*- coding: utf-8 -*-
from django.conf import settings
from django.urls import path, include
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(("shuup.apps.mailer.urls", "mailer"), namespace="mailer")),
]
