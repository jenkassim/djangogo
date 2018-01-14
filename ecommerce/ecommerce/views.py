from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ContactForm, LoginForm

def home_page(request):
      context = {
            "title":"Hello world homepage!",
            "content": "Welcome to the home page"
      }
      return render(request, "home_page.html", context)

def about_page(request):
      context = {
            "title":"About Page",
            "content": "Welcome to the about page"
      }
      return render(request, "home_page.html", context)

def contact_page(request):
      contact_form = ContactForm(request.POST or None)
      context = {
            "title":"Contact Page",
            "content": "Welcome to the contact page",
            "form": contact_form
      }

      if contact_form.is_valid():
            print(contact_form.cleaned_data)

      # if request.method == "POST":
      #       print(request.POST)
      #       print(request.POST.get('fullname'))
      #       print(request.POST.get('email'))
      #       print(request.POST.get('content'))

      return render(request, "contact/view.html", context)


def login_page(request):
      form = LoginForm(request.POST or None)
      context = {
            "form": form
      }

      print("User logged in: ")
      print(request.user.is_authenticated())

      if form.is_valid():
            print(form.cleaned_data)
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            print(request.user.is_authenticated())

            user =authenticate(request, username=username, password=password)
            if user is not None:
                  login(request, user)
                  print(request.user.is_authenticated())

                  # Redirect to a success page.
                  return redirect("/about")
            else:
                  # Return an 'invalid login' error message.
                  print("Error")


      return render(request, "auth/login.html", context)

def register_page(request):
      form = LoginForm(request.Post or None)
      if form.is_valid():
            print(form.cleaned_data)

      return render(request, "auth/login.html", {})


def home_page_old(request):
    html_ = """
    <!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.3/css/bootstrap.min.css" integrity="sha384-Zug+QiDoJOrZ5t4lssLdxGhVrurbmBWopoEl+M6BdEfwnCJZtKxi1KgxUyJq13dy" crossorigin="anonymous">

    <title>Hello, world!</title>
  </head>
  <body>
    <div class='text-center'>
    <h1>Hello, world!</h1>
    </div>
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.3/js/bootstrap.min.js" integrity="sha384-a5N7Y/aK3qNeh15eJKGWxsqtnX/wWdSZSKp+81YjTmS15nvnvxKHuzaWwXHDli+4" crossorigin="anonymous"></script>
  </body>
</html>
"""
    return HttpResponse(html_)