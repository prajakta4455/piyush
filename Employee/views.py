from django.shortcuts import render
from . import views
from django.views import View
from django.contrib.auth.models import User
from .models import EmpDaTa
from django.http import HttpResponse
# Create your views here.

class Login(View):
    def get(self, request):
        return render(request, "Employee/login.html")

    def post(self, request):
        Username = request.post.get('username')
        Password = request.post.get('password')

class Save_emp_data(View):
    def get(self, request):
        return render(request, "Employee/login.html" )

    def post(self, request):
      try:
          type = request.POST.get('type', 'NA')
          fname = request.POST.get('fname', 'NA')
          email = request.POST.get('email', '00')
          password = request.POST.get('password', 'NA')
          job_title = request.POST.get('job_title', 'NA')
          doj = request.POST.get('doj', 'NA')
          last_ap_date = request.POST.get('last_ap_date', 'NA')
          evalute_by = request.POST.get('evalute_by', 'NA')
          reporting_mail = request.POST.get('reporting_mail', 'NA')
          print(fname,email,password,job_title)

          obj = User(username=email, password=password, first_name=type)
          obj.save()

          obj = EmpDaTa(fname=fname, email=email, job_title=job_title, doj=doj, last_ap_date=last_ap_date,
                    evalute_by=evalute_by, reporting_mail=reporting_mail)
          obj.save()
          return HttpResponse("Added employee successfully")
      except:

          return HttpResponse("Employee registration failed")

