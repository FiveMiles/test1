from django.shortcuts import render

from django.http import *
from django.template import RequestContext, loader
from .models import *
# Create your views here.


def index(request):
    # 旧方式处理
    # # 加载模板
    # temp = loader.get_template('booktest/index.html')
    # # 渲染模板
    # return HttpResponse(temp.render())
    # 新方式
    bookList = BookInfo.objects.all()

    context = {'list':bookList}
    return render(request, 'booktest/index.html', context)


