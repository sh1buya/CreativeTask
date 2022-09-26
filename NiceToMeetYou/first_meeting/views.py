from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {}
    context['name'] = 'Ярослава Чижикова'
    context['city'] = 'г. Мурманск'
    context['hobbies'] = '''Занимаюсь плаванием, люблю точные науки, особенно - математику. Увлекаюсь программированием, не очень люблю читать документацию:('''
    context['experience'] = '''Два года училась в Яндекс.Лицее, в течение которых мы в том числе и работали над различными проектами. Это те, в которых участвовала я:'''

    context['rosseti'] = 'Еще участвовала в программном проекте "Оптимизация собственной генерации просьюмеров" на Энергетической Проектной смене.'
    return render(request, 'index.html', context)



