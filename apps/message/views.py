from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend

# Create your views here.

from .models import UserMessage, UserProfile


# 验证user
# class CustomBackend(ModelBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         try:
#             user = UserProfile.objects.get(username=username)
#             if user.check_password(password):
#                 return user
#         except Ellipsis as e:
#             return None


# 留言板
def getform(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        message = request.POST.get('message', '')
        user_message = UserMessage()
        user_message.name = name
        user_message.message = message
        user_message.email = email
        user_message.address = address
        user_message.save()

    return render(request, 'message_form.html')


# 登录
def user_login(request):
    if request.method == "POST":
        user_name = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=user_name, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return render(request, 'index.html')
        else:
            return render(request, 'login.html', {})
    elif request.method == "GET":
        return render(request, 'login.html', {})
