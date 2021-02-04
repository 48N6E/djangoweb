from django.shortcuts import render
from django.http import HttpRequest,HttpResponse,HttpResponseBadRequest,JsonResponse
import simplejson
from .models import  User


# Create your views here.

#注册函数
def reg(request:HttpRequest):
    print(request.POST)
    print(request.body)
    payload = simplejson.loads(request.body)
    try:
            #有任何异常，都返回400，如果保存数据出错，则向外抛出异常
        email = payload['email']
        query = User.objects.filter(email=email)
        print(query)
        print(type(query),query.query) #查看sql语句
        if query.first():
            return HttpResponseBadRequest() #这里返回实例，这不是异常类

        name = payload['name']
        password = payload['password']
        print(email,name,password)

        user = User()
        user.email = email
        user.name = name
        user.password = password

        try:
            user.save()
            return JsonResponse({'user_id）':user.id})  #如果正常，返回json数据
        except:
            return JsonResponse({'reason':'afadass'},status=400)
    except Exception as e: #有任何异常，都返回
        print(e)
        return HttpResponseBadRequest('参数错误 ')#这里返回实例，这不是异常类

def show(request):
    query = User.objects.all()
    return JsonResponse({})


