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
            response = HttpResponseRedirect('/event_manage/')
            # response.set_cookie('user',username,3600)
            request.session['user'] = username
            return response
        else:
            return render(request,'index.html',{'error': 'error'})

def event_manage(request):
    # username = request.COOKIES.get('user', '')
    username = request.session.get('user','')
    return render(request,'event_manage.html',{'user':username})
