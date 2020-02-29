from . import views
from django.urls import path

urlpatterns = [

    path('login/', views.login.as_view(), name="login"),
    path('logout/', views.logout.as_view(), name="logout"),
    path('Save_emp_data/', views.Save_emp_data.as_view(), name="save_emp_Data"),

]