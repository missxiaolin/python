from django.shortcuts import render

# Create your views here.

# 留言板
def getform(request):
    return render(request, 'message_form.html')
