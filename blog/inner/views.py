from django.shortcuts import render, redirect
from .models import Blog, Comment, Popular
from .forms import Blogs
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import EditProfile
# Create your views here.
def home(request):
    if request.method=='GET':
        q=request.GET.get('query')
        if q is None:
            post=Blog.objects.all()
            populars=Popular.objects.all()
        else:
            populars=Popular.objects.filter(description__icontains=q)
            post=Blog.objects.filter(description__icontains=q)
            messages.warning(request, 'Here are the search results : ')
    else:
        populars=Popular.objects.all()
        post=Blog.objects.all()
    return render(request, 'home.html',{'post':post, 'populars':populars})


def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method=='POST':
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        usernames=User.objects.filter(username=username)
        emails=User.objects.filter(email=email)

        if usernames:
            messages.warning(request, "username alredy exists !")
            return redirect('/signup')
        
        if emails:
            messages.warning(request,'Email alredy exists !')
            return redirect('/signup')

        if pass1 != pass2:
            messages.warning(request,'Password Does not Match !')
            return redirect('/signup')

        if len(request.POST['pass1'])<=5:
            messages.warning(request,'Password should be more that 5 digit !')
            return redirect('/signup')
        
        user_obj=User.objects.create_user(username, email, pass1)
        user_obj.first_name=fname
        user_obj.last_name=lname
        user_obj.save()
        return redirect('/login')

    return render(request, 'signup.html')

def signin(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method=='POST':
        username=request.POST['uname']
        password=request.POST['psw']

        user=authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.warning(request, "Welcome Home !")
            return redirect('/')
        
        else:
            messages.warning(request, "Given credentials does not match !")
            return redirect('/login')
    else:
        return render(request, 'login.html')

def logouts(request):
    logout(request)
    return redirect('/login')

def settings(request):
	if request.user.is_authenticated:
		if request.method=='POST':
		    form=EditProfile(request.POST, instance=request.user)

		    if form.is_valid():
		    	form.save()
		    	messages.warning(request, 'Profile Saved Sucessfully !')
		else:
			form=EditProfile(instance=request.user)
		return render(request,'settings.html',{'form':form})
	else:
		return redirect('/login')

def userblogs(request):
    user=request.user
    userblogs=Blog.objects.filter(author=user)
    return render(request,'userblogs.html', {'userblogs':userblogs})

def blog(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            title=request.POST['title']
            desc=request.POST['desc']
            images=request.FILES['images']
            author=request.user

            user_blog=Blog(author=author,title=title, description=desc, images=images)
            user_blog.save()
            return redirect('/')
        else:
            return render(request, 'blogpost.html')
    else:
        return redirect('/login')

def delete_post(request, pk):
    if request.user.is_authenticated:
        Blog.objects.filter(id=pk).delete()
        return redirect('/userblogs')
    else:
        return redirect('/login')

def edit_blogs(request, id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi=Blog.objects.get(pk=id)
            editblogs=Blogs(request.POST, instance=pi)
            if editblogs.is_valid():
                editblogs.save()
                messages.warning(request, 'Update sucessfully')
                return redirect('/')
            else:
                messages.warning(request, 'something wrong')
        else:
            pi=Blog.objects.get(pk=id)
            editblogs=Blogs(instance=pi)
        return render(request, 'editblogs.html', {'editblogs':editblogs})

def readmore(request,id):
    if request.method=='POST':
        post=Blog.objects.get(id=id)
        name=request.POST['name']
        body=request.POST['body']
        cmnt_obj=Comment(comment=post, name=name, body=body)
        cmnt_obj.save()
        return redirect('/')
        messages.warning(request, 'comment added sucessfully ')
    else:
        post=Blog.objects.get(id=id)
        comment=Comment.objects.filter(comment=post)
    return render(request, 'readmore.html',{'post':post, 'comment':comment})