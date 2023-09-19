from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from django.contrib.auth import login, authenticate,logout
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from App_Login.forms import SignUpForm,UserProfileChangeForm,UserProfileForm



def sign_up(request):
    form=SignUpForm()
    registered=False
    if request.method=='POST':
        form=SignUpForm(data=request.POST)

        if form.is_valid():
            form.save()
            registered=True
    dict={'form':form,'registered':registered}
    return render(request,'signup.html',context=dict)



def login_page(request):
    form=AuthenticationForm()
    if request.method == 'POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            username= form.cleaned_data.get('username')
            password= form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)

            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse("App_Blog:blog_list"))
    return render(request,'login.html',context={"form":form})


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse("App_Blog:blog_list"))





@login_required
def profile(request):
    return render(request, "profile.html")





@login_required
def user_chance(request):
    current_user=request.user
    form=UserProfileChangeForm(instance=current_user)
    if request.method=='POST':
        form=UserProfileChangeForm(request.POST,instance=current_user)
        if form.is_valid():
            form.save()
            form=UserProfileChangeForm(instance=current_user)
            return HttpResponseRedirect(reverse('App_Login:profile'))
    return render(request,'change_profile.html',context={'form':form})




@login_required
def pass_change(request):
    currenr_user=request.user
    changed=False
    form=PasswordChangeForm(currenr_user)
    if request.method=="POST":
        form=PasswordChangeForm(currenr_user,data=request.POST)
        if form.is_valid():
            form.save()
            changed=True
    return render(request,'change_pass.html',context={'form':form,'changed':changed})





# from django.shortcuts import render, redirect
# from .forms import UserProfileForm

@login_required

def upload_profile_picture(request):
    form = UserProfileForm()

    if request.method == 'POST':
        form=UserProfileForm(request.POST,request.FILES)


        if form.is_valid():
            user_obj=form.save(commit=False)
            user_obj.user=request.user
            user_obj.save()
            return HttpResponseRedirect(reverse("App_Login:profile"))


    else:
        form = UserProfileForm()

    return render(request, 'profile_pic_add.html', {'form': form})




@login_required
def change_profile_pic(request):
    form=UserProfileForm(instance=request.user.profile_picture)
    if request.method=='POST':
        form=UserProfileForm(request.POST,request.FILES,instance=request.user.profile_picture)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('App_Login:profile'))
    return render(request,'profile_pic_add.html',context={'form':form})