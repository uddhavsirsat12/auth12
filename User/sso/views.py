from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User 
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.core.mail import EmailMessage
from django.core.validators import EmailValidator
import re
from django.http import Http404
# Create your views here.

def register_1(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        if not re.match(EMAIL_REGEX,email):
            messages.error(request,'email not valid')

        password = request.POST['password']
        re_password = request.POST['re_password']
        if password == re_password:
            if User.objects.filter(username = username).exists():
                messages.error(request,'Username already exist')
                return render(request,'register.html')
            elif User.objects.filter(email = email).exists():
                messages.error(request,'email already exist')
                return render(request,'register.html')
            else:
                user=User.objects.create_user(first_name = first_name,last_name = last_name,username = username,email=email,password = password)
                user.save()
                mail_subject = 'Activate your account.'
                message = f'Hi {user.username}, please use this link to activate your account: {request.build_absolute_uri("/activate/")}{user.pk}/'
                to_email = email
                email = EmailMessage(mail_subject, message, to=[to_email])
                email.send()
                return redirect('activate')
        else:
            messages.error(request,'password does not match')
            return render(request,'register.html')
    else:
        return render(request,'register.html')
    
def login_1(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username,password = password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Invalid credencials')
            return render(request,'login.html')
    else:
        return render(request,'login.html')

def logout_1(request):
    logout(request)                                                                                                                          
    return redirect('register')


def home_1(request):
    return render (request,'logout.html')

def activate(request, pk):
    try:
        user = get_object_or_404(User,id=pk)
    except User.DoesNotExist:
        raise Http404('User does not exist.')
    user.is_active = True
    user.save()
    return redirect(request,'login')




      
# def activate(request, pk):
#     try:
#         user = User.objects.get(pk=pk)
#     except User.DoesNotExist:
#         raise Http404('User does not exist.')
#     user.is_active = True
#     user.save()
#     return redirect('account_activation_done')
