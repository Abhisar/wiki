# Create your views here.
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.core.context_processors import csrf
from articles.models import Article
from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.http import HttpResponseRedirect

def view_page(request,page_name):
    try:
           page=Article.objects.get(pk=page_name)
    except Article.DoesNotExist:
           return render_to_response("create.html",{"page_name":page_name})
    content=page.body
    return render_to_response("view.html",{"page_name":page_name,"content":content})


def edit_page(request,page_name):
    #c = {}
    #c.update(csrf(request))
    try:
           page=Article.objects.get(pk=page_name)
           content= page.body
    except Article.DoesNotExist:
           content=""
    return render_to_response("edit.html",{"page_name":page_name,"content":content},context_instance=RequestContext(request))



def save_page(request,page_name):
    content=request.POST["content"]
    try:
           page=Article.objects.get(pk=page_name)
           page.body=content
    except Article.DoesNotExist:
           page=Article(title=page_name,body=content)
    page.save()
    return HttpResponseRedirect("/wiki/"+page_name+"/")


def all_articles(request):
    return render_to_response('articles.html',{'articles':Article.objects.all()})


                    
                   
