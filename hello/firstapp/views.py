from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect,HttpResponsePermanentRedirect
from django.http import *
from django.template.response import TemplateResponse

# Create your views here


# def index(request):
#     header = "Персональные данные"  # обычная переменная
#     langs = ["Английский", "Немецкий", "Испанский"]  # массив
#     user = {"name": "Максим,", "age": 30}  # словарь
#     addr = ("Виноградная", 23, 45)  # кортеж
#     data = {"header": header, "langs": langs, "user": user, "address": addr}
#     return render(request, "index.html", context=data)

def index(request):
    return render(request, "firstapp/home.html")


def about(request):
    return HttpResponse("About")


def contact(request):
    return HttpResponseRedirect("/about")


def details(request):
    return HttpResponsePermanentRedirect("/")


def m400(request):
    return HttpResponseBadRequest('Index Bad')


def products(request, productid):
    category = request.GET.get('cat', '')
    output = '<h2> Продукт № {0} Категория: {1}</h2>'.format(productid, category)
    return HttpResponse(output)


def users(request):
    id = request.GET.get('id', 1)
    name = request.GET.get('name', 'Максим')
    output = '<h2> Пользователь </h2><h3>id: {0} ' \
             'Имя: {1} </h3>'.format(id, name)
    return HttpResponse(output)