from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse, redirect, HttpResponse
from .models import Theme
from django.contrib.auth.decorators import login_required
import sys
sys.path.append('..')
from accounts.models import Profile
from .forms import HintForm

count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0
count8 = 0
count9 = 0
count10 = 0
count11 = 0
count12 = 0
count13 = 0
count14 = 0
count15 = 0
count16 = 0
count17 = 0
count18 = 0
count19 = 0
count20 = 0


def switch(x):
    return {1: count1, 2: count2, 3: count3, 4: count4, 5: count5, 6: count6,
            7: count7, 8: count8, 9: count9, 10: count10, 11: count11, 12: count12,
            13: count13, 14: count14, 15: count15, 16: count16, 17: count17, 18: count18,
            19: count19, 20: count20}.get(x, 0)

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
    theme_number = get_object_or_404(Theme, name=theme).theme_number
    if theme_number == 1:
        global count1
    if theme_number == 2:
        global count2
    if theme_number == 3:
        global count3
    if theme_number == 4:
        global count4
    if theme_number == 5:
        global count5
    if theme_number == 6:
        global count6
    if theme_number == 7:
        global count7
    if theme_number == 8:
        global count8
    if theme_number == 9:
        global count9
    if theme_number == 10:
        global count10
    if theme_number == 11:
        global count11
    if theme_number == 12:
        global count12
    if theme_number == 13:
        global count13
    if theme_number == 14:
        global count14
    if theme_number == 15:
        global count15
    if theme_number == 16:
        global count16
    if theme_number == 17:
        global count17
    if theme_number == 18:
        global count18
    if theme_number == 19:
        global count19
    if theme_number == 20:
        global count20
    reset = get_object_or_404(Profile, user=request.user).reset
    user_id = request.user.username
    theme = get_object_or_404(Theme, name=theme)
    escape_room = get_object_or_404(Profile, user=request.user).escape_room
    q = request.GET.get('q', '')
    if q == reset:
        if theme_number == 1:
            count1 = 0
        if theme_number == 2:
            count2 = 0
        if theme_number == 3:
            count3 = 0
        if theme_number == 4:
            count4 = 0
        if theme_number == 5:
            count5 = 0
        if theme_number == 6:
            count6 = 0
        if theme_number == 7:
            count7 = 0
        if theme_number == 8:
            count8 = 0
        if theme_number == 9:
            count9 = 0
        if theme_number == 10:
            count10 = 0
        if theme_number == 11:
            count11 = 0
        if theme_number == 12:
            count12 = 0
        if theme_number == 13:
            count13 = 0
        if theme_number == 14:
            count14 = 0
        if theme_number == 15:
            count15 = 0
        if theme_number == 16:
            count16 = 0
        if theme_number == 17:
            count17 = 0
        if theme_number == 18:
            count18 = 0
        if theme_number == 19:
            count19 = 0
        if theme_number == 20:
            count20 = 0
    return render(request, 'hint/reset_code.html', {
        'reset': reset,
        'q': q,
        'theme': theme,
        'user_id': user_id,
        'escape_room': escape_room,
    })


@login_required
def QR_code(request, user_id, theme):
    theme_number = get_object_or_404(Theme, name=theme).theme_number
    if theme_number == 1:
        global count1
    if theme_number == 2:
        global count2
    if theme_number == 3:
        global count3
    if theme_number == 4:
        global count4
    if theme_number == 5:
        global count5
    if theme_number == 6:
        global count6
    if theme_number == 7:
        global count7
    if theme_number == 8:
        global count8
    if theme_number == 9:
        global count9
    if theme_number == 10:
        global count10
    if theme_number == 11:
        global count11
    if theme_number == 12:
        global count12
    if theme_number == 13:
        global count13
    if theme_number == 14:
        global count14
    if theme_number == 15:
        global count15
    if theme_number == 16:
        global count16
    if theme_number == 17:
        global count17
    if theme_number == 18:
        global count18
    if theme_number == 19:
        global count19
    if theme_number == 20:
        global count20
    count = switch(theme_number)
    print("pk:", theme_number, 'count:', count)
    escape_room = get_object_or_404(Profile, user=request.user).escape_room
    hintCount = get_object_or_404(Theme, name=theme).hintCount
    q = request.GET.get('q', '')
    if q != "":
        if request.method == "GET":
            print("fuck")
            if theme_number == 1:
                count1 += 1
            if theme_number == 2:
                count2 += 1
            if theme_number == 3:
                count3 += 1
            if theme_number == 4:
                count4 += 1
            if theme_number == 5:
                count5 += 1
            if theme_number == 6:
                count6 += 1
            if theme_number == 7:
                count7 += 1
            if theme_number == 8:
                count8 += 1
            if theme_number == 9:
                count9 += 1
            if theme_number == 10:
                count10 += 1
            if theme_number == 11:
                count11 += 1
            if theme_number == 12:
                count12 += 1
            if theme_number == 13:
                count13 += 1
            if theme_number == 14:
                count14 += 1
            if theme_number == 15:
                count15 += 1
            if theme_number == 16:
                count16 += 1
            if theme_number == 17:
                count17 += 1
            if theme_number == 18:
                count18 += 1
            if theme_number == 19:
                count19 += 1
            if theme_number == 20:
                count20 += 1
    else:
        pass
    print(count)
    if hintCount > count:
        return render(request, 'hint/qr.html', {
            'hintCount': hintCount,
            'count': count,
            'theme': theme,
            'escape_room': escape_room,
            'user_id': user_id
        })
    else:
        return render(request, 'hint/not_hint.html',{
            'hintCount': hintCount,
            'count': count,
            'theme': theme,
            'escape_room': escape_room,
            'user_id': user_id
        })


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
    theme = get_object_or_404(Theme, name=theme)
    return render(request, 'hint/theme_hint.html', {
        'hint': hint,
        'theme': theme,
        'user_id': user_id,
    })


@login_required
def theme_edit(request, user_id, theme):
    escape_room = get_object_or_404(Profile, user=request.user).escape_room
    theme = get_object_or_404(Theme, name=theme)
    if request.method == 'POST':
        form = HintForm(request.POST, request.FILES, instance=theme)
        if form.is_valid():
            theme = form.save(commit=False)
            theme.roomEscape = request.user
            theme.save()
            return HttpResponseRedirect(reverse('hint:admin', args=[request.user.username]))
        else:
            print(form.errors)
    else:
        form = HintForm(instance=theme)
    return render(request, 'hint/theme_edit.html', {
        'form': form,
        'theme': theme,
        'escape_room': escape_room,
        'user_id': user_id
    })


def ajax(request, user_id, theme):
    theme = get_object_or_404(Theme, name=theme, roomEscape=request.user)
    print(theme)
    data = request.GET['msg']
    if data == '1':
        theme.sub_hint1.delete()
    elif data == '2':
        theme.sub_hint2.delete()
    elif data == '3':
        theme.sub_hint3.delete()
    elif data == '4':
        theme.sub_hint4.delete()
    elif data == '5':
        theme.sub_hint5.delete()
    elif data == '6':
        theme.sub_hint6.delete()
    elif data == '7':
        theme.sub_hint7.delete()
    elif data == '8':
        theme.sub_hint8.delete()
    elif data == '9':
        theme.sub_hint9.delete()
    elif data == '10':
        theme.sub_hint10.delete()
    elif data == '11':
        theme.sub_hint11.delete()
    elif data == '12':
        theme.sub_hint12.delete()
    elif data == '13':
        theme.sub_hint13.delete()
    elif data == '14':
        theme.sub_hint14.delete()
    elif data == '15':
        theme.sub_hint15.delete()
    elif data == '16':
        theme.sub_hint16.delete()
    elif data == '17':
        theme.sub_hint17.delete()
    elif data == '18':
        theme.sub_hint18.delete()
    elif data == '19':
        theme.sub_hint19.delete()
    elif data == '20':
        theme.sub_hint20.delete()

    return HttpResponse(data)


def create_qr_code(request):
    id = request.GET.get('id', '')
    theme = request.GET.get('theme', '')
    hint = request.GET.get('hint', '')
    return render(request, 'hint/create_qr_code.html', {
        'id': id,
        'theme': theme,
        'hint': hint,
    })


def personal_information(request):
    return render(request, 'hint/personal_information.html')


def admin(request, user_id):
    themes = Theme.objects.all()
    themes = themes.filter(roomEscape=request.user)
    escape_room = get_object_or_404(Profile, user=request.user).escape_room
    return render(request, 'hint/admin.html', {
        'themes': themes,
        'escape_room': escape_room,
        'user_id': user_id
    })


