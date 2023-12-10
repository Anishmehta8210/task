from django.shortcuts import render,redirect,HttpResponse
from django.views.generic import CreateView,View,FormView
from.models import User
from .forms import *
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.

class HomeView(View):
    def get(self,r):
       
        return render(r,"home.html")
class DashbordView(View):
    def get(self,req):
        data={
            "user":User.objects.get(pk=req.user.id),
        }
        return render(req,"dashboard.html",data)
    
class DoctorView(CreateView):
    model=Doctor
    form_class=DoctorForm
    template_name="signup.html"
    success_url="/doctor/dashboard/"
    def get_context_data(self,**kwargs):
        kwargs['user_type']="Doctor"
        return super().get_context_data(**kwargs)
    def form_valid(self,form):
        user=form.save()
        login(self.request,user)
        return redirect("dashboard")
class PatientView(CreateView):
    model = Patient
    form_class=PatientForm
    template_name="signup.html"
    success_url="/"
    def get_context_data(self,**kwargs):
        kwargs['user_type']="Patient"
        return super().get_context_data(**kwargs)
    def form_valid(self,form):
        user=form.save()
        login(self.request,user)
        return redirect("dashboard")
    
class LoginView(FormView):
    template_name="login.html"
    form_class=AuthenticationForm
    success_url="/"
    def post(self,request):
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                back = request.GET.get("next","dashboard")
                return redirect(back)
            else:
                return HttpResponse("Inactivated")
        else:
            return HttpResponse("login cheeking is not correct")
class LogoutView(View):
    def get(self,req):
        logout(req)
        return redirect("login")
