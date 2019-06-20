from django.shortcuts import render, get_object_or_404
from .models import Theme, RoomEscape


def main(request):
    roomescape = RoomEscape.objects.all()
    q = request.GET.get('q', '')
    return render(request, 'hint/main.html', {
        'roomescape': roomescape,
        'q': q
    })


def theme_list(request, room_escape):
    themes = Theme.objects.all()
    return render(request, 'hint/theme_list.html', {
        'themes': themes,
        'room_escape': room_escape
    })


def reset_code(request, room_escape, theme):
    roomescape = get_object_or_404(RoomEscape, name=room_escape)
    theme = get_object_or_404(Theme, name=theme)
    reset = get_object_or_404(RoomEscape, name=room_escape).reset
    q = request.GET.get('q', '')
    return render(request, 'hint/reset_code.html', {
        'reset': reset,
        'q': q,
        'theme': theme,
        'roomescape': roomescape
    })


def theme_detail(request, room_escape, theme):
    roomescape = get_object_or_404(RoomEscape, name=room_escape)
    password = roomescape.reset
    theme = get_object_or_404(Theme, name=theme)
    return render(request, 'hint/theme_detail.html', {
        'theme': theme,
        'password': password,
    })