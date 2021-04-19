#-*- coding: utf-8 -*-
from django.urls import path
from django.views.decorators.cache import cache_page

from shuup.apps.mailer.views import IndexView

urlpatterns = [
    path('', cache_page(60 * 5)(IndexView.as_view()), name="index"),
]
