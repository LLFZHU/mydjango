from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request,'index.html')

# 登陆动作
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        if username == 'admin' and password == 'admin123456':
            return HttpResponseRedirect('/event_manage/')
        else:
            return render(request,'index.html',{'error': 'error'})

def event_manage(request):
    return render(request,'event_manage.html')
