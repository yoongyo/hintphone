from django.shortcuts import render, HttpResponse, reverse, HttpResponseRedirect
from .forms import LoginForm
from django.contrib.auth import login, authenticate


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
            return HttpResponse('로그인 실패. 다시 시도 해보세요.')

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
            return HttpResponse('로그인 실패. 다시 시도 해보세요.')
    else:
        form = LoginForm()
        return render(request, 'accounts/login.html', {
            'form': form
        })


