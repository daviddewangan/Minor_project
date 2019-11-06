from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Question, Choice
from django.http.response import HttpResponse
from blog.forms import ChoiceForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views import generic
from rest_framework import viewsets
from django.db.models import Q
from blog.serializer import ChoiceSerializer
from django.views.generic.detail import DetailView
import operator

from django.db.models import Q
from _functools import reduce
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth.views import login

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:10]
    context = {'latest_question_list':latest_question_list}
    return render(request,'index.html',context)

def categories(request):
    latest_question_list = Question.objects.all()
    context = {'latest_question_list':latest_question_list}
    return render(request,'sidebar.html',context)

def detail(request,id):
    question = get_object_or_404(Question,pk=id)
    return render(request,'detail.html',{'question':question})
    paginate_by = 5

def result(request,id):
    response = "You are looking at the result of question %s."
    return HttpResponse(response % id)




@login_required(login_url='/login')
def addChoice(request):
    form = ChoiceForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        profile = form.save(commit=False)
        
        profile.user = request.user
        profile.save()

        messages.success(request,"suuccessfull added")
        return redirect("home")
    return render(request,"form.html",{"form":form})


def choices(request):
    keyword = request.GET.get("keyword")
    
    if keyword:
        choices = Choice.objects.filter(title=keyword)
        return render(request,"feed.html",{"choices":choices})
    choices = Choice.objects.all()
    
    return render(request,"feed.html",{"choices":choices})
@login_required()
def dashboard(request):
    choices = Choice.objects.filter(user = request.user)
    context = {
        "choices":choices
        
    }
    return render(request,"dashboard.html",context)



def choiceDetail(request,id):
    choice = Choice.objects.filter(id = id).first()   
    choice = get_object_or_404(Choice,id = id)

    comments = choice.comments.all()
    return render(request,"postdetail.html",{"choice":choice,"comments":comments})

class PostList(generic.ListView):
    queryset = Choice.objects.order_by('-pub_date')
    template_name = 'feed.html'
    paginate_by = 5
    
class PostDetail(generic.DetailView):
    model = Choice
    template_name = 'postdetail.html'
    
    
def signup(authenticate):
    if authenticate.method == 'POST':
        form = UserCreationForm(authenticate.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_date.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(authenticate, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(authenticate, 'registration_form.html', {'form': form})
    

