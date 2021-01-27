from django.urls import path
from . import views

urlpatterns = [
    #path('<str:query>/', views.queryResultView),
    path('<str:query>/', views.queryResultViewTmp),
    path('', views.queryResultViewTmp),
]
