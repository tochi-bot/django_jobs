from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterUserForm
from resume.models import Resume
from company.models import company

def register_applicant(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_applicant = True
            var.username = var.email
            var.save()
            Resume.objects.create(user=var)
            messages.info(request, 'Your account has been created')
            return redirect('login')
        else:
            messages.warning(request, 'Something went wrong')
            return redirect('register_applicant')
    else:
        form = RegisterUserForm()
        context = {'form': form}
        return render(request, 'users/register_applicant.html', context)

def register_recruiter(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_recruiter = True
            var.username = var.email
            var.save()
            Company.objects.create(user=var)
            messages.info(request, 'Your account has been created')
            return redirect('login')
        else:
            messages.warning(request, 'Something went wrong')
            return redirect('register_recruiter')
    else:
        form = RegisterUserForm()
        context = {'form': form}
        return render(request, 'users/register_recruiter.html', context)

def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        if user is not None and user.is_active:
            login(request, user)
            if user.is_applicant:
                return redirect('applicant_dashboard')
            elif user.is_recruiter:
                return redirect('recruiter_dashboard')
            else:
                return redirect('login')
        else:
            messages.warning(request, 'Invalid credentials or account inactive')
            return redirect('login')
    else:
        return render(request, 'users/login.html')

def logout_user(request):
    logout(request)
    messages.info(request, 'You have successfully logged out')
    return redirect('login')

def index(request):
    return  render(request, 'users/index.html')

def about(request):
    return  render(request, 'users/about.html')

def contact(request):
    return  render(request, 'users/contact.html')

def proxy(request):
    return HttpResponse("This is the proxy view.")

def applicant_dashboard(request):
    return HttpResponse("This is the applicant dashboard.")

def recruiter_dashboard(request):
    return HttpResponse("This is the recruiter dashboard.")
