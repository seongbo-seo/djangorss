from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.cnn_list, name='cnn_list'),
    path('rss/', views.readfeed, name='readfeed'),
    path('cnnlist/',views.showcnn,name='cnnlist'),
]

