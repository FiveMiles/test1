# -*- coding: utf-8 -*-#
# Name:         urls
# Author:       $ Caoxianyun
# Date:         2021-01-10

from django.conf.urls import url
from django.urls import path
from .views import *

urlpattern = [
    path('', index)
]