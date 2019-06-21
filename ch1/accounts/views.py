from django.shortcuts import render, HttpResponse, reverse, HttpResponseRedirect
from .forms import LoginForm
from django.contrib.auth import login, authenticate


def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('hint:theme_list', args=[user.username]))
        else:
            return HttpResponse('로그인 실패. 다시 시도 해보세요.')
    else:
        form = LoginForm()
        return render(request, 'accounts/login.html', {
            'form': form
        })


