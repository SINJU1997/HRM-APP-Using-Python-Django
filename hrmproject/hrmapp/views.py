from django.shortcuts import render, HttpResponse, redirect
from .forms import UserRegistrationForm
# Create your views here.
def index(request):
    return render(request,'login.html')

# def register(request):
#     return render(request,'register.html')
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_success')  # Redirect to a success page
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def userDashboard(request):
    return render(request,'user-dashboard.html')

def profile(request):
    return render(request,'profile.html')

def edit(request):
    return render(request,'edit.html')

def leaveStatus(request):
    return render(request,'leave-status.html')

def applyLeave(request):
    return render(request,'apply-leave.html')

# admin 

def adminDashboard(request):
    return render(request,'admin-dashboard.html')

def usersList(request):
    return render(request,'users-list.html')

def leaves(request):
    return render(request,'leave-entries.html')

def attendance(request):
    return render(request,'attendance.html')