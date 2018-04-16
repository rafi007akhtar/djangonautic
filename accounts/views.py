from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as logi
from django.contrib.auth import logout

def signup(request):
    if request.method == "POST":
        # create the user-instance of UserCreationForm
        UCF = UserCreationForm(request.POST)
        if UCF.is_valid():
            UCF.save()

            # redirect to login page so that the user might enter their credentials to log in
            return redirect("accounts:login") 

    else: 
        # create a blank instance of UserCreationForm
        UCF = UserCreationForm()

    # pass on this instance in the render call
    return render(request, "accounts/signup.html", {"form": UCF})

def login(request):
    if request.method == "POST":
        # create a form with the user data
        loginForm = AuthenticationForm(data = request.POST)

        if loginForm.is_valid():
            # retrieve the user from the credentials entered in the login form
            user = loginForm.get_user()
            # log this user in
            logi(request, user)

            return redirect("articles:list") 
    
    else:
        # create a blank instance of login form
        loginForm = AuthenticationForm()
    
    # pass on the latest instance (GET / unvalidated POST) to the template
    return render(request, "accounts/login.html", {"form": loginForm})

def logout_view(request):
    # Logout the user if he hits the logout submit button
    if request.method == "POST":
        logout(request)
        return redirect("accounts:login")
