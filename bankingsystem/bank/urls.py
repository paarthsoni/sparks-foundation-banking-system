from django.contrib import admin
from django.urls import path,include
from bank import views
urlpatterns = [
    path('', views.index,name="home"),
    path('transfer', views.transfer,name="transfer"),
    path('money', views.money,name="money"),
    path('customerinput', views.customerinput,name="customerinput"),
    path('customerinput/<int:id>', views.customerinput,name="customerinput"),
    path('confirmtransfer', views.confirmtransfer,name="confirmtransfer"),
    path('confirmtransfer/<int:id>', views.confirmtransfer,name="confirmtransfer"),
    path('transferfail', views.transferfail,name="transferfail"),
    path('transferhistorypage', views.transferhistorypage,name="transferhistorypage"),
    


]
