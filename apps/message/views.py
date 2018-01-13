from django.shortcuts import render

# Create your views here.

from .models import UserMessage

# 留言板
def getform(request):
    if request.method == "POST":
        name = request.POST.get('name','')
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



