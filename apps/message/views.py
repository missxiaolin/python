from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
# 发送邮箱
from django.core.mail import send_mail

# Create your views here.

from .models import UserMessage, UserProfile
from .forms import LoginForm


# 验证user
# class CustomBackend(ModelBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         try:
#             user = UserProfile.objects.get(username=username)
#             if user.check_password(password):
#                 return user
#         except Ellipsis as e:
#             return None

# 登录
class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = authenticate(username=user_name, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return render(request, 'index.html')
        else:
            return render(request, 'login.html', {'msg':'用户名密码错误'})


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
