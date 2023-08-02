from django.http import HttpResponse 
from django.template.loader import render_to_string

import random
from articale.models import Article
def home(request):
    name = "Kareem"
    number = random.randint(2,4)
    article_obj = Article.objects.get(id=number)
    obj_list = Article.objects.all()
    context ={
        'obj':article_obj,
        'obj_list': obj_list,
    }
    HTML_STRING= render_to_string("home_views.html",context=context)
    return HttpResponse(HTML_STRING)