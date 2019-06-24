from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse, redirect
from .models import Theme
from django.contrib.auth.decorators import login_required
import sys
sys.path.append('..')
from accounts.models import Profile
from .forms import HintForm
count = 0

@login_required
def theme_list(request, user_id):
    themes = Theme.objects.all()
    themes = themes.filter(roomEscape=request.user)
    escape_room = get_object_or_404(Profile, user=request.user).escape_room
    return render(request, 'hint/theme_list.html', {
        'themes': themes,
        'escape_room': escape_room,
        'user_id': user_id
    })


@login_required
def reset_code(request, user_id, theme):
    global count
    reset = get_object_or_404(Profile, user=request.user).reset
    user_id = request.user.username
    theme = get_object_or_404(Theme, name=theme)
    escape_room = get_object_or_404(Profile, user=request.user).escape_room
    q = request.GET.get('q', '')
    if q == reset:
        count = 0
    return render(request, 'hint/reset_code.html', {
        'reset': reset,
        'q': q,
        'theme': theme,
        'user_id': user_id,
        'escape_room': escape_room,
    })


@login_required
def QR_code(request, user_id, theme):
    global count
    escape_room = get_object_or_404(Profile, user=request.user).escape_room
    hintCount = get_object_or_404(Theme, name=theme).hintCount
    q = request.GET.get('q', '')
    if q != "":
        if request.method == "GET":
            count += 1
            return redirect(q)
    else:
        pass
    print(count)
    if hintCount > count:
        return render(request, 'hint/qr.html', {
            'count': count,
            'theme': theme,
            'escape_room': escape_room,
            'user_id': user_id
        })
    else:
        return render(request, 'hint/not_hint.html')


@login_required
def theme_detail(request, user_id, theme):
    reset = get_object_or_404(Profile, user=request.user).reset
    theme = get_object_or_404(Theme, name=theme)
    return render(request, 'hint/theme_detail.html', {
        'theme': theme,
        'password': reset,
    })


@login_required
def theme_hint(request, user_id, theme, hint):
    global count
    theme = get_object_or_404(Theme, name=theme)
    return render(request, 'hint/theme_hint.html', {
        'hint': hint,
        'theme': theme,
        'count': count,
        'user_id': user_id,
    })


@login_required
def theme_edit(request, user_id, theme):
    theme = get_object_or_404(Theme, name=theme)
    if request.method == 'POST':
        form = HintForm(request.POST, request.FILES, instance=theme)
        if form.is_valid():
            theme = form.save(commit=False)
            theme.roomEscape = request.user
            theme.save()
            return HttpResponseRedirect(reverse('hint:theme_list', args=[request.user.username]))
        else:
            print(form.errors)
    else:
        form = HintForm(instance=theme)
    return render(request, 'hint/theme_edit.html', {
        'form': form,
    })