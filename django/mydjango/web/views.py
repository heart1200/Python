from django.http import HttpResponse
from django.shortcuts import render
import json


# Create your views here.

def login(request):
    # GET 方法
    # if request.method == 'GET':
    #     result = {}
    #     username = request.GET.get('username')
    #     mobile = request.GET.get('mobile')
    #     result['username'] = username
    #     result['mobile'] = mobile
    #     result = json.dumps(result)
    #     return HttpResponse(result)
    #     # return HttpResponse(result, content_type='application/json;charset=utf-8')
    # else:
    #    return render(request, 'login.html')

    # POST 方法
    if request.method == 'POST':
        result = {}
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(password)
        result['username'] = username
        result['password'] = password
        result = json.dumps(result)
        return HttpResponse(result, content_type='application/json;charset=utf-8')
    else:
        return render(request, 'login.html')


def hello_world(request):
    return HttpResponse("Hello world")
