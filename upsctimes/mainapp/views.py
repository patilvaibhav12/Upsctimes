import os
import urllib.parse
from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.contrib import messages
from .models import homepost, books, newspaper, eml, history, geography, polity, currentaffairs, generalscience, impupdates, gjobs, pjobs

from django.conf import settings             
from django.core.mail import send_mail
from django.template.loader import render_to_string
import math

# home function
def index(request):
    no_of_post = 3
    page = request.GET.get('page')
    if page is None:
        page = 1
    else:
        page = int(page)
    post = homepost.objects.all()
    posts = post[(page-1)*no_of_post : page*no_of_post]
    length = len(post)
    if page>1:
        prev = page-1
    else:
        prev = None
    if page<math.ceil(length/no_of_post):
        nxt = page + 1
    else:
        nxt = None
    m = "blog"
    contex ={'posts':posts, 'prev':prev, 'nxt':nxt, 'm':m}
    return render(request, 'index.html', contex)


def readArticle(request,slug):
    post = homepost.objects.filter(slug=slug).first()
    share_string = urllib.parse.quote(post.title, safe ='')
    return render(request, 'read.html', {'post':post, 'share_string': share_string})
# def getbooks(request):
#     context = {'file':books.objects.all()}
#     return render(request, 'getbooks.html', context)

def readgjob(request, slug):
    post = gjobs.objects.filter(slug=slug).first()
    return render(request, 'readjob.html', {'post':post})

def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(),content_type = "application/adminupload")
            response['Content-Disposition'] = 'inline;filename = '+os.path.basename(file_path)
            return response

    raise Http404


def questionpapers(request):
    m = "papers"
    return render(request, 'Questionpapers.html', {'m':m})

def notes(request):
    m = "notes"
    context = {'file':newspaper.objects.all(), 'm':m}
    return render(request, 'notes.html', context)

def quiz(request):
    no_of_post = 10
    page = request.GET.get('page')
    if page is None:
        page = 1
    else:
        page = int(page)
    post = history.objects.all()
    posts = post[(page-1)*no_of_post : page*no_of_post]
    length = len(post)
    if page>1:
        prev = page-1
    else:
        prev = None
    if page<math.ceil(length/no_of_post):
        nxt = page + 1
    else:
        nxt = None
    t = "History MCQs"
    m = "h"
    contex ={'posts':posts, 'prev':prev, 'nxt':nxt, 't':t, 'm':m}
    return render(request, 'quiz.html',contex )

def jobs(request):
    no_of_post = 10
    page = request.GET.get('page')
    if page is None:
        page = 1
    else:
        page = int(page)
    post = gjobs.objects.all()
    posts = post[(page-1)*no_of_post : page*no_of_post]
    length = len(post)
    if page>1:
        prev = page-1
    else:
        prev = None
    if page<math.ceil(length/no_of_post):
        nxt = page + 1
    else:
        nxt = None

    m = "jobs"
    contex ={'posts':posts, 'prev':prev, 'nxt':nxt, 'm':m}
    return render(request, 'jobs.html',contex )

def corporatejobs(request):
    no_of_post = 10
    page = request.GET.get('page')
    if page is None:
        page = 1
    else:
        page = int(page)
    post = pjobs.objects.all()
    posts = post[(page-1)*no_of_post : page*no_of_post]
    length = len(post)
    if page>1:
        prev = page-1
    else:
        prev = None
    if page<math.ceil(length/no_of_post):
        nxt = page + 1
    else:
        nxt = None
    contex ={'posts':posts, 'prev':prev, 'nxt':nxt}
    return render(request, 'jobs.html',contex )

def Geography(request):
    no_of_post = 10
    page = request.GET.get('page')
    if page is None:
        page = 1
    else:
        page = int(page)
    post = geography.objects.all()
    posts = post[(page-1)*no_of_post : page*no_of_post]
    length = len(post)
    if page>1:
        prev = page-1
    else:
        prev = None
    if page<math.ceil(length/no_of_post):
        nxt = page + 1
    else:
        nxt = None
    t = "Geography MCQs"
    m = "g"
    contex ={'posts':posts, 'prev':prev, 'nxt':nxt, 't':t, 'm':m}
    return render(request, 'quiz.html',contex )

def Polity(request):
    no_of_post = 10
    page = request.GET.get('page')
    if page is None:
        page = 1
    else:
        page = int(page)
    post = polity.objects.all()
    posts = post[(page-1)*no_of_post : page*no_of_post]
    length = len(post)
    if page>1:
        prev = page-1
    else:
        prev = None
    if page<math.ceil(length/no_of_post):
        nxt = page + 1
    else:
        nxt = None
    t = "Polity MCQs"
    m = "p"
    contex ={'posts':posts, 'prev':prev, 'nxt':nxt, 't':t, 'm':m}
    return render(request, 'quiz.html',contex )

def Generalscience(request):
    no_of_post = 10
    page = request.GET.get('page')
    if page is None:
        page = 1
    else:
        page = int(page)
    post = generalscience.objects.all()
    posts = post[(page-1)*no_of_post : page*no_of_post]
    length = len(post)
    if page>1:
        prev = page-1
    else:
        prev = None
    if page<math.ceil(length/no_of_post):
        nxt = page + 1
    else:
        nxt = None
    t = "General Science MCQs"
    m = "gs"
    contex ={'posts':posts, 'prev':prev, 'nxt':nxt, 't':t, 'm':m}
    return render(request, 'quiz.html',contex )

def Currentaffairs(request):
    no_of_post = 10
    page = request.GET.get('page')
    if page is None:
        page = 1
    else:
        page = int(page)
    post = currentaffairs.objects.all()
    posts = post[(page-1)*no_of_post : page*no_of_post]
    length = len(post)
    if page>1:
        prev = page-1
    else:
        prev = None
    if page<math.ceil(length/no_of_post):
        nxt = page + 1
    else:
        nxt = None
    t = "Current Affairs MCQs"
    m = "ca"
    contex ={'posts':posts, 'prev':prev, 'nxt':nxt, 't':t, 'm':m}
    return render(request, 'quiz.html',contex )

def email(request):
    posts = homepost.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        if name  == '' or email == '' :
            messages.success(request, 'please Enter details!')
            return render(request,'index.html', {'posts': posts})
        else:
            Eml = eml(name = name, email=email)
            Eml.save()
        messages.warning(request, 'Congratulations!, You have connected with us!!!!')
        msg_plain = render_to_string('email.txt')
        msg_html = render_to_string('email.html')

        send_mail("You have been subscribed successfully!", msg_plain, settings.EMAIL_HOST_USER, [email], html_message = msg_html)
        return render(request,'index.html', {'posts': posts})
    return render(request,'index.html', {'posts': posts})


#Search functions 

def searchh(request):
    query = request.GET['query']
    if len(query)> 78:
        allqst = []
    else:
        allqst = history.objects.filter(qst__icontains = query)
    return render(request, 'search.html', {'allqst':allqst, 'query':query})

def searchg(request):
    query = request.GET['query']
    if len(query)> 78:
        allqst = []
    else:
        allqst = geography.objects.filter(qst__icontains = query)
    return render(request, 'search.html', {'allqst':allqst, 'query':query})

def searchp(request):
    query = request.GET['query']
    if len(query)> 78:
        allqst = []
    else:
        allqst = polity.objects.filter(qst__icontains = query)
    return render(request, 'search.html', {'allqst':allqst, 'query':query})

def searchgs(request):
    query = request.GET['query']
    if len(query)> 78:
        allqst = []
    else:
        allqst = generalscience.objects.filter(qst__icontains = query)
    return render(request, 'search.html', {'allqst':allqst, 'query':query})

def searchca(request):
    query = request.GET['query']
    if len(query)> 78:
        allqst = []
    else:
        allqst = currentaffairs.objects.filter(qst__icontains = query)
    return render(request, 'search.html', {'allqst':allqst, 'query':query})

def searchblog(request):
    query = request.GET['query']
    if len(query)> 78:
        blogs = []
    else:
        blogs = homepost.objects.filter(title__icontains = query)
    return render(request, 'blogsearch.html', {'posts':blogs, 'query':query})

def searchnotes(request):
    query = request.GET['query']
    if len(query)> 78:
        blogs = []
    else:
        blogs = newspaper.objects.filter(title__icontains = query)
    return render(request, 'searchnotes.html', {'file':blogs, 'query':query})

def searchpapers(request):
    query = request.GET['query']
    return render(request, 'Questionpapers.html', {'query':query})

def searchjobs(request):
    query = request.GET['query']
    if len(query)> 78:
        blogs = []
    else:
        blogs = gjobs.objects.filter(title__icontains = query)
    return render(request, 'gjobsearch.html', {'jobs':blogs, 'query':query})