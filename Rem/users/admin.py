# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from users.models import User
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'name')

admin.site.register(User, UserAdmin)
