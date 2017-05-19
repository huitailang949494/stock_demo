# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from stock.models import Stock, AccessRecord

# Register your models here.


class StockAdmin(admin.ModelAdmin):
    list_display = ('stock_id', 'name', 'module')


class AccessRecordAdmin(admin.ModelAdmin):
    list_display = ('user', 'stock', 'created_time')

admin.site.register(Stock, StockAdmin)
admin.site.register(AccessRecord, AccessRecordAdmin)
