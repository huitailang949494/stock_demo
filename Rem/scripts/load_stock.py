#!/usr/bin/env python
# encoding: utf-8

import csv
from stock.models import Stock

csv.field_size_limit(500 * 1024 * 1024)


def run():
    with open("data/stock_module.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            Stock.objects.get_or_create(name=row[0],
                                        stock_id=row[1],
                                        module=row[2])

run()
