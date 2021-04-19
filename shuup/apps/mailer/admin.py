#-*- coding: utf-8 -*-
from django.contrib import admin

from shuup.apps.mailer.models import (
    Company,
    Contact,
    Order
)

admin.site.register(Company)
admin.site.register(Contact)
admin.site.register(Order)
