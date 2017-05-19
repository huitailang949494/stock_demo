# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class User(models.Model):

    user_id = models.IntegerField()
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return "%d" % self.user_id
