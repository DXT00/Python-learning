# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from novel.models import Novelcontent1

def index(request):#request是用户请求信息
    c = Novelcontent1.objects.get(id=1)
    print(c.id)

    b=Novelcontent1.objects.filter().order_by('?')[:5]#从novels数据库中的Novelcontent1表随意取5个数据

    for bb in b:
        print(bb.id,bb.imgsrc)

    context={

        'novels':b
    }
    return render(request,'index.html',context=context)#接收的参数必须是个字典
    #return HttpResponse('<h1>Hello world</h1>')
    #return=响应 render=模板渲染
 # 'abcde':'哈哈哈',
 # a=DjangoContentType.objects.all().values_list('id','app_label','model')#查询