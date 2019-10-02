from django.shortcuts import render, HttpResponse, reverse, HttpResponseRedirect,redirect
from .forms import LoginForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import (
    logout as django_logout,
)


def signin(request):
    if request.COOKIES.get('username') is not None:
        username = request.COOKIES.get('username')
        password = request.COOKIES.get('password')
        method = request.COOKIES.get('method')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if method == "pc":
                return HttpResponseRedirect(reverse('hint:admin', args=[user.username]))
            else:
                return HttpResponseRedirect(reverse('hint:theme_list', args=[user.username]))
        else:
            return render(request, 'accounts/login_fail.html')

    elif request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        method = request.POST['method']
        print(method)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)

            if method == "pc":
                response = HttpResponseRedirect(reverse('hint:admin', args=[user.username]))
                response.set_cookie('username', username)
                response.set_cookie('password', password)
                response.set_cookie('method', method)
                return response

            else:
                response = HttpResponseRedirect(reverse('hint:theme_list', args=[user.username]))
                response.set_cookie('username', username)
                response.set_cookie('password', password)
                response.set_cookie('method', method)
                return response
        else:
            return render(request, 'accounts/login_fail.html')
    else:
        form = LoginForm()
        return render(request, 'accounts/login.html', {
            'form': form
        })


def logout(request):
    # django_logout(request)
    response = HttpResponseRedirect(reverse('accounts:login'))
    response.delete_cookie('username')
    response.delete_cookie('password')
    response.delete_cookie('method')
    return response



