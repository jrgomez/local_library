#
#//  urls.py
#//  Local Library
#//
#//  Created by Joseph Gomez on 1/5/25.
#//

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

]
