from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from movies.models import Movie
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


# Create your views here.
def register(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        password=request.POST["password"]
        if User.objects.filter(username=email).exists():
            messages.info(request,"Email already registered")
            return redirect("register")
        
        else:
            user=User.objects.create_user(username=email,first_name=first_name,last_name=last_name,email=email,password=password)
            user.save()
            return redirect("login_user")
    return render(request, "register.html")
    



def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("home")
        else:
            messages.info(request, "invalid username or password")
            return redirect("login_user")
    return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect("login_user")


def profile(request):
    movies = Movie.objects.all()
    return render(request, "profile.html",{'movies':movies} )

@login_required(login_url='login_user')
def edit_profile(request):
    user = request.user

    if request.method == "POST":
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')

        new_username = request.POST.get("username")
        if new_username:
            user.username = new_username

        # handle profile picture safely
        if hasattr(user, 'userprofile') and request.FILES.get('profile_pic'):
            user.userprofile.profile_pic = request.FILES['profile_pic']
            user.userprofile.save()

        user.save()

        auth.logout(request)
        messages.success(request, "Profile updated. Please login again.")
        return redirect('login_user')

    return render(request, "edit_profile.html")



@login_required(login_url='login_user')
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # keeps user logged in
            return redirect("profile")
    else:
        form = PasswordChangeForm(request.user)

    return render(request, "change_password.html", {"form": form})


