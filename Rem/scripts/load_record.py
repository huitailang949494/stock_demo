#!/usr/bin/env python
# encoding: utf-8

import csv
import time
from users.models import User
from stock.models import Stock, AccessRecord

stock_names = []

with open('data/stock_name.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        stock_names.append([row[0].decode('utf-8'), row[1]])

print len(stock_names)

for stock_row in stock_names:
    stock_name = stock_row[1]
    print stock_row[1]
    try:
        stock = Stock.objects.get(stock_id=stock_name)
    except:
        continue
    try:
        file_name = 'data/stock_data/{0}.csv'.format(stock_name)
        with open(file_name, 'rb') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                user_id = row[0]
                if not user_id.isdigit():
                    continue
                user = User.objects.get(user_id=user_id)
                created_time = time.mktime(time.strptime(row[1], "%a %b %d %H:%M:%S %Y"))
                created_time = time.localtime(created_time)
                created_time = time.strftime("%Y-%m-%d %H:%M:%S", created_time)
                AccessRecord.objects.get_or_create(user=user,
                                                   stock=stock,
                                                   created_time=created_time)
    except:
        pass
