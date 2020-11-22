from django.shortcuts import render,redirect,get_object_or_404
from django.shortcuts import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile,Friend
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from  .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm


def register(request):
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Account created Login Now!')
                return redirect('login')
        else:
            form = UserRegisterForm()
        return render(request,'users/signup.html',{'form':form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Profile Updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {'u_form': u_form,'p_form': p_form}
    return render(request,'users/profile.html',context)

def people(request):
    users = User.objects.all()
    return render(request,'users/people.html',{'users':users})

@login_required
def change_friends(request, operation, pk):
    friend = User.objects.get(pk=pk)
    p1 = Profile.objects.get(user=friend)
    p2 = Profile.objects.get(user=request.user)
    f1 = Friend.objects.get(current_user=request.user)
    for user in f1.users.all():
        print(user.username)
    followers = p2.followers.all()
    followings = p2.following.all()
   # for follow in followings:
    #    print(follow.username)
    if operation == 'add':
        p2.following.add(friend)
        p1.followers.add(request.user)
        p1.save()
        p2.save()
        Friend.make_friend(request.user, friend)
    return redirect('profile')

def remove_friends(request,pk):
    friend = User.objects.get(pk=pk)
    p1 = Profile.objects.get(user=friend)
    p2 = Profile.objects.get(user=request.user)
    f1 = Friend.objects.get(current_user=request.user)
    for user in f1.users.all():
        print(user.username)
    p2.following.remove(friend)
    p1.followers.remove(request.user)
    p1.save()
    p2.save()
    Friend.lose_friend(request.user, friend)
    return redirect('profile')

@login_required
def friends(request):
    p2 = Profile.objects.get(user=request.user)
    followers = p2.followers.all()
    followings = p2.following.all()
    return render(request,'users/friends.html',{'followers':followers,'followings':followings})

@login_required
def view_profile(request,pk):
    u1 = User.objects.get(pk=pk)
    user = Profile.objects.get(user=u1)
    followers  = user.followers.all()
    followings = user.following.all()
    return render(request,'users/view_profile.html',{'user':user,'u1':u1,'followers':followers,'followings':followings})