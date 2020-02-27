from . import views
from django.urls import path

urlpatterns = [

    path('', views.Login.as_view(), name="login"),
    path('Save_emp_data/', views.Save_emp_data.as_view(), name="save_emp_Data"),

]