# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from users.models import User
from stock.models import AccessRecord
from rnn.work import predict_stock

def index(request, user_id):
    user = User.objects.get(user_id=user_id)
    accessrecords = AccessRecord.objects.filter(user=user).order_by('created_time')
    target_sentence = []
    for a in accessrecords:
        target_sentence.append(a.stock.stock_id.lower())
    predict_sentence = predict_stock(target_sentence)
    # predict_sentence = [1,2,3,4,5]
    most_care_stock = ''
    most_care_module = ''
    stock_cnt = {}
    module_cnt = {}
    for r in accessrecords:
        stock_id = r.stock.stock_id
        module = r.stock.module
        stock_cnt[stock_id] = stock_cnt.get(stock_id, 0) + 1
        module_cnt[module] = module_cnt.get(module, 0) + 1
        if most_care_stock == '' or stock_cnt[stock_id] > stock_cnt[most_care_stock]:
            most_care_stock = stock_id
        if most_care_module == '' or module_cnt[module] > module_cnt[most_care_module]:
            most_care_module = module
    return render(request, 'users/index.html', locals())
