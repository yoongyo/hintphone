from django.shortcuts import render, get_object_or_404
from .models import Theme
from django.contrib.auth.decorators import login_required
import sys
sys.path.append('..')
from accounts.models import Profile


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
    reset = get_object_or_404(Profile, user=request.user).reset
    user_id = request.user.username
    theme = get_object_or_404(Theme, name=theme)
    q = request.GET.get('q', '')
    return render(request, 'hint/reset_code.html', {
        'reset': reset,
        'q': q,
        'theme': theme,
        'user_id': user_id
    })


def QR_code(request):
    return render(request, 'hint/QR_code.html')


@login_required
def theme_detail(request, user_id, theme):
    reset = get_object_or_404(Profile, user=request.user).reset
    theme = get_object_or_404(Theme, name=theme)
    return render(request, 'hint/theme_detail.html', {
        'theme': theme,
        'password': reset,
    })