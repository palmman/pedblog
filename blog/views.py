from django.shortcuts import render, get_object_or_404, redirect
from .forms import RegistrationForm
from django.contrib import messages, auth
from .models import Post, Account

# Create your views here.

def home(request):
    current_user = request.user
    post = Post.objects.filter().order_by('-created')
    if current_user.is_authenticated:
        if request.method == 'POST':
            title = request.POST['title']
            content = request.POST['content']
            post = Post.objects.create(title=title, content=content,user=current_user)
            post.save()
            messages.success(request, 'Posted')
            return redirect('home')
        else:
            pass

    post = Post.objects.filter().order_by('-created')
    context = {
        'post' : post,
    }
    return render(request, 'home.html', context)

def single_post(request, post_slug):
    
    single_post = get_object_or_404(Post, slug=post_slug)

    context = {

        'single_post' : single_post,
    }
    
    return render(request, 'singlepost.html', context)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']       
            user = Account.objects.create_user( username=username, email=email, password=password)
            user.save()
        
        messages.success(request, 'Thank you for registering with us.')
        return redirect('home')

    else:
        form = RegistrationForm()

    context = {
        'form' : form,
    }
    return render(request, 'register.html', context)

def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are Logged in.')
            return redirect('login')
        else:
            messages.error(request, 'The username or password is incorrect')
            return redirect('login')
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    messages.success(request, 'You are logged out.')
    return redirect('login')
            