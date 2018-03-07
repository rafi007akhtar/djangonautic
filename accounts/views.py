from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    if request.method == "POST":
        # create the user-instance of UserCreationForm
        UCF = UserCreationForm(request.POST)
        if UCF.is_valid():
            UCF.save()
            # TODO: log the user in
            return redirect("articles:list")

    else: 
        # create a blank instance of UserCreationForm
        UCF = UserCreationForm()

    # pass on this instance in the render call
    return render(request, "accounts/signup.html", {"form": UCF})
