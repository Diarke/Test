from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout
from django.views.generic import UpdateView, DeleteView

# Create your views here.
def base(request):
    news = News.objects.all()
    comments = Review.objects.all()
    return render(request, 'base.html', {'news':news, 'comments':comments})


def news_form(request):
    form = NewsForm()
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'news_form.html', {'form':form})


def news_detail(request, pk):
    news = News.objects.filter(id=pk)
    return render(request, 'news_detail.html', {'news':news})


class NewsUpdateView(UpdateView):
    model = News
    template_name = 'news_form.html'
    form_class = NewsForm


class NewsDeleteView(DeleteView):
    model = News
    success_url = '/'
    template_name = 'news_delete_form.html'


def index(request):
    subjects = Subject.objects.all()
    return render(request, 'index.html', {'subjects':subjects})


def history(request):
    history = History.objects.filter(user=request.user).order_by('-created_at')[:5]
    return render(request, 'history.html', {'history':history})


def test_view(request, pk):
    subject = Subject.objects.get(id=pk)
    questions = Questions.objects.filter(subject_id=subject)

    if request.method == 'POST':
        score = 0
        for question in questions:
            selected_answer = request.POST.get(str(question.id))
            if selected_answer:
                answer = Answers.objects.get(id=selected_answer)
                if answer.is_correct:
                    score += 1
        
        History.objects.create(user=request.user, subject=subject, total=questions.count(), score=score)
        return render(request, 'result.html', {'score': score, 'total': questions.count()})

    return render(request, 'test.html', {'subject': subject, 'questions': questions})  


def Register(request):
    if request.method == 'post':
        form = UserForm(request.post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserForm()
    return render(request, 'register.html', {'form':form})


def Login(request):
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if User is not None:
            auth.login(request, user)
            return redirect('home')
    return render(request, 'login.html', {'form':form})


def Logout(request):
    logout(request)
    return redirect('home')


@login_required
def otzv(request):
    comments = Review.objects.all()
    form = ReviewForm()
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'otzv.html', {'form':form, 'comments':comments})


