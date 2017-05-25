#!/usr/bin/env python
# encoding: utf-8
from rest_framework import viewsets, serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from stock.models import Stock


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ('stock_id', 'name', 'module')


class StockViewSet(viewsets.ModelViewSet):

    queryset = Stock.objects.all()
    serializer_class = StockSerializer

    @api_view(['get', 'post'])
    def post(request):
        return Response({'hehe': 'hehe'})
