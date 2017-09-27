# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.
class UserManager(models.Manager):
    def validation(self, requestPost):
        string = ""
        if len(requestPost['first_name']) < 2:
            string += "First name is too short"
        if len(requestPost['last_name']) < 2: 
            string += " Last name is too short"
        if re.match(EMAIL_REGEX, requestPost['email']) == None:
            string += " Invalid E-mail"
        return string

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()