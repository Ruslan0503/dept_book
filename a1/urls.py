from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('homeAPI/', views.homeAPI, name="homeAPI"),

    path('add_customer/', views.add_customer, name="add_customer"),
    path('add_customerAPI/', views.addCustomerAPI, name="addCustomerFunc"),
    
    path('write_dept/', views.write_dept, name="write_dept"),
    path('write_deptAPI/', views.write_deptAPI, name="write_deptAPI"),

    path('customerdata/<int:id>/', views.Customerdata, name="customerdata"),
    
    path('turndept/', views.turnDept, name="turndept"),
    path('turnDeptAPI/', views.turnDeptAPI, name="turnDeptAPI"),
    
    path('showHistory/<int:id>/', views.showHistory, name="showHistory"),
] 

# represented = ifodalangan
# much yet = hali ko'p
# although = garchi
# realize = anglash
# overtake = quvib o'tish
# significant = muhim
# relevant = muvofiq
# refer=murojat qilmoq
# proud=mag'rur