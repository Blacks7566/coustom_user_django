from django.shortcuts import render, HttpResponseRedirect,HttpResponse,redirect
from accounts.forms import UserForm, UserEditForm,LoginForm
from django.contrib import messages
from accounts.validation import cheak_email, cheak_mobile
from accounts.models import User
from django.contrib.auth import login, logout, authenticate,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm,UserCreationForm
# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = UserForm(request.POST)
            if fm.is_valid():
                pass1 = fm.cleaned_data['password']
                pass2 = request.POST.get('comfirm_password')
                email = fm.cleaned_data['email']
                phone = fm.cleaned_data['phone']
                if pass1 == pass2:
                    if len(pass1) >= 6:
                        if len(phone) == 10:
                            if phone.isdigit():
                                if cheak_mobile(phone):
                                    if cheak_email(email):
                                        fm.save()
                                        messages.success(
                                            request, 'Register successfully ...')
                                    else:
                                        messages.error(
                                            request, "Please enter valid email address")
                                else:
                                    messages.error(
                                        request, "Please enter valid mobile number")
                            else:
                                messages.error(
                                    request, "mobile number should be numeric")
                        else:
                            messages.error(
                                request, "mobile number should be 10 digist")
                    else:
                        messages.error(
                            request, 'password should be greater then 6 charaters')
                else:
                    messages.error(request, "Both password should be same")
        else:
            fm = UserForm()

        return render(request, 'index.html', {'form': fm})
    else:
        return HttpResponseRedirect('/profile/')


# def login_view(request):
#     if request.method == 'POST':
#         fm = LoginForm(request.POST)
#         print(1)
#         if fm.is_valid():
#             print(1)
#             uname = fm.cleaned_data['email']
#             upass = fm.cleaned_data['password']
#             print(uname)
#             print(upass)
#             user = authenticate(request, username=uname, password=upass)
#             print(user)
#             if user is not None:
#                 login(request, user)
#                 messages.success(request,'Log in successfully')
#                 return HttpResponseRedirect('/profile/')
#     else:
#         fm = LoginForm()
#         return render(request, 'login.html', {'form': fm})







def login_view(request):
    # if request.user.is_authenticated:
        # return redirect('index')
    context ={}
    form=LoginForm(request.POST or None)
    if form.is_valid():
        email =form.data.get('email')
        password=form.data.get('password')
        matching =User.objects.filter(email=email)
        if not matching:
            messages.error(request, 'Email id Not Match in DB Please Signup First!.')
        else:
            user=authenticate(email=email,password=password)
            if user:
                login(request,user)
                return redirect('profile')
            else:
                messages.error(request, 'Email and Password incorrect.')
    context['form']=form
    return render(request,"login.html",context)










# def login_view(request):

#     if not request.user.is_authenticated:

#         if request.method == 'POST':
#             fm = AuthenticationForm(request=request, data=request.POST)
#             if fm.is_valid():
#                 uname = fm.cleaned_data['username']
#                 upass = fm.cleaned_data['password']

#                 print(uname)
#                 print(upass)
#                 user = authenticate(request, username=uname, password=upass)
#                 print(user)
#                 if user is not None:
#                     login(request, user)
#                     messages.success(request,'Log in successfully')
#                     return HttpResponseRedirect('/profile/')

#         else:
#             fm = AuthenticationForm()
#         return render(request, 'login.html', {'form': fm})
#     else:
#         return HttpResponseRedirect('/profile/')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def profile(request):

    if request.user.is_authenticated:

        user = request.user
        name = str(user).split('@')
        id = user.id
        context = {
            'name': name[0],
            'id': id
        }
        return render(request, 'profile.html', context)
    else:
        return HttpResponseRedirect('/login/')


def Edit_user(request, id):
    if request.user.is_authenticated:

        pro = User.objects.get(id=id)
        if request.method == 'POST':
            fm = UserEditForm(request.POST, request.FILES, instance=pro)
            if fm.is_valid():
                fm.save()
                messages.success(request, 'profile update successfully')
        fm = UserEditForm(instance=pro)
        return render(request, 'editProfile.html', {'form': fm, 'user': pro})
    else:
        return HttpResponseRedirect('/login/')

def pasword_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = PasswordChangeForm(user = request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request,'Password change successfully ')
                update_session_auth_hash(request,fm.user)
                return HttpResponseRedirect('/profile/')
            else:
                fm = PasswordChangeForm(user = request.user)
            return render(request,'changePassword.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')

def set_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = SetPasswordForm(user = request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request,'Password change successfully ')
                update_session_auth_hash(request,fm.user)
                return HttpResponseRedirect('/profile/')
            else:
                fm = SetPasswordForm(user = request.user)
            return render(request,'setPassword.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')