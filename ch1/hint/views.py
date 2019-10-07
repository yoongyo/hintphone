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

code_list1 = []
code_list2 = []
code_list3 = []
code_list4 = []
code_list5 = []
code_list6 = []
code_list7 = []
code_list8 = []
code_list9 = []
code_list10 = []
code_list11 = []
code_list12 = []
code_list13 = []
code_list14 = []
code_list15 = []
code_list16 = []
code_list17 = []
code_list18 = []
code_list19 = []
code_list20 = []


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
    nation = get_object_or_404(Profile, user=request.user).nation
    return render(request, 'hint/theme_list.html', {
        'themes': themes,
        'escape_room': escape_room,
        'user_id': user_id,
        'nation': nation
    })


@login_required
def reset_code(request, user_id, theme):
    theme_number = get_object_or_404(Theme, name=theme, roomEscape=request.user).theme_number
    nation = get_object_or_404(Profile, user=request.user).nation
    if theme_number == 1:
        global count1
        global code_list1
    if theme_number == 2:
        global count2
        global code_list2
    if theme_number == 3:
        global count3
        global code_list3
    if theme_number == 4:
        global count4
        global code_list4
    if theme_number == 5:
        global count5
        global code_list5
    if theme_number == 6:
        global count6
        global code_list6
    if theme_number == 7:
        global count7
        global code_list7
    if theme_number == 8:
        global count8
        global code_list8
    if theme_number == 9:
        global count9
        global code_list9
    if theme_number == 10:
        global count10
        global code_list10
    if theme_number == 11:
        global count11
        global code_list11
    if theme_number == 12:
        global count12
        global code_list12
    if theme_number == 13:
        global count13
        global code_list13
    if theme_number == 14:
        global count14
        global code_list14
    if theme_number == 15:
        global count15
        global code_list15
    if theme_number == 16:
        global count16
        global code_list16
    if theme_number == 17:
        global count17
        global code_list17
    if theme_number == 18:
        global count18
        global code_list18
    if theme_number == 19:
        global count19
        global code_list19
    if theme_number == 20:
        global count20
        global code_list20

    reset = get_object_or_404(Profile, user=request.user).reset
    user_id = request.user.username
    theme = get_object_or_404(Theme, name=theme, roomEscape=request.user)
    escape_room = get_object_or_404(Profile, user=request.user).escape_room
    q = request.GET.get('q', '')
    if q == reset:
        if theme_number == 1:
            count1 = 0
            code_list1 = []
        if theme_number == 2:
            count2 = 0
            code_list2 = []
        if theme_number == 3:
            count3 = 0
            code_list3 = []
        if theme_number == 4:
            count4 = 0
            code_list4 = []
        if theme_number == 5:
            count5 = 0
            code_list5 = []
        if theme_number == 6:
            count6 = 0
            code_list6 = []
        if theme_number == 7:
            count7 = 0
            code_list7 = []
        if theme_number == 8:
            count8 = 0
            code_list8 = []
        if theme_number == 9:
            count9 = 0
            code_list9 = []
        if theme_number == 10:
            count10 = 0
            code_list10 = []
        if theme_number == 11:
            count11 = 0
            code_list11 = []
        if theme_number == 12:
            count12 = 0
            code_list12 = []
        if theme_number == 13:
            count13 = 0
            code_list13 = []
        if theme_number == 14:
            count14 = 0
            code_list14 = []
        if theme_number == 15:
            count15 = 0
            code_list15 = []
        if theme_number == 16:
            count16 = 0
            code_list16 = []
        if theme_number == 17:
            count17 = 0
            code_list17 = []
        if theme_number == 18:
            count18 = 0
            code_list18 = []
        if theme_number == 19:
            count19 = 0
            code_list19 = []
        if theme_number == 20:
            count20 = 0
            code_list20 = []
    return render(request, 'hint/reset_code.html', {
        'reset': reset,
        'q': q,
        'theme': theme,
        'user_id': user_id,
        'escape_room': escape_room,
        'nation': nation
    })


@login_required
def QR_code(request, user_id, theme):
    theme_number = get_object_or_404(Theme, name=theme, roomEscape=request.user).theme_number
    interPhone_key = get_object_or_404(Theme, name=theme, roomEscape=request.user).interPhone_key
    interPhone_secret = get_object_or_404(Theme, name=theme, roomEscape=request.user).interPhone_secret
    interPhone_id = get_object_or_404(Theme, name=theme, roomEscape=request.user).interPhone_ID
    nation = get_object_or_404(Profile, user=request.user).nation
    interPhone = get_object_or_404(Profile, user=request.user).interPhone
    interPhone_call = get_object_or_404(Profile, user=request.user).interPhone_call
    hintCode = request.user.profile.hintCode
    if theme_number == 1:
        global count1
        global code_list1
        print(code_list1)
    if theme_number == 2:
        global count2
        global code_list2
    if theme_number == 3:
        global count3
        global code_list3
    if theme_number == 4:
        global count4
        global code_list4
    if theme_number == 5:
        global count5
        global code_list5
    if theme_number == 6:
        global count6
        global code_list6
    if theme_number == 7:
        global count7
        global code_list7
    if theme_number == 8:
        global count8
        global code_list8
    if theme_number == 9:
        global count9
        global code_list9
    if theme_number == 10:
        global count10
        global code_list10
    if theme_number == 11:
        global count11
        global code_list11
    if theme_number == 12:
        global count12
        global code_list12
    if theme_number == 13:
        global count13
        global code_list13
    if theme_number == 14:
        global count14
        global code_list14
    if theme_number == 15:
        global count15
        global code_list15
    if theme_number == 16:
        global count16
        global code_list16
    if theme_number == 17:
        global count17
        global code_list17
    if theme_number == 18:
        global count18
        global code_list18
    if theme_number == 19:
        global count19
        global code_list19
    if theme_number == 20:
        global count20
        global code_list20
    count = switch(theme_number)
    print("pk:", theme_number, 'count:', count)
    escape_room = get_object_or_404(Profile, user=request.user).escape_room
    hintCount = get_object_or_404(Theme, name=theme, roomEscape=request.user).hintCount
    if request.method == "POST":
        p = request.POST.get('p', '')
        if theme_number == 1:
            if p not in code_list1:
                code_list1.append(p)
                print(code_list1)
                count1 += 1
        if theme_number == 2:
            if p not in code_list2:
                code_list2.append(p)
                print(code_list2)
                count2 += 1
        if theme_number == 3:
            if p not in code_list3:
                code_list3.append(p)
                print(code_list3)
                count3 += 1
        if theme_number == 4:
            if p not in code_list4:
                code_list4.append(p)
                print(code_list4)
                count4 += 1
        if theme_number == 5:
            if p not in code_list5:
                code_list5.append(p)
                print(code_list5)
                count5 += 1
        if theme_number == 6:
            if p not in code_list6:
                code_list6.append(p)
                print(code_list6)
                count6 += 1
        if theme_number == 7:
            if p not in code_list7:
                code_list7.append(p)
                print(code_list7)
                count7 += 1
        if theme_number == 8:
            if p not in code_list8:
                code_list8.append(p)
                print(code_list8)
                count8 += 1
        if theme_number == 9:
            if p not in code_list9:
                code_list9.append(p)
                print(code_list9)
                count9 += 1
        if theme_number == 10:
            if p not in code_list10:
                code_list10.append(p)
                print(code_list10)
                count10 += 1
        if theme_number == 11:
            if p not in code_list11:
                code_list11.append(p)
                print(code_list11)
                count11 += 1
        if theme_number == 12:
            if p not in code_list12:
                code_list12.append(p)
                print(code_list12)
                count12 += 1
        if theme_number == 13:
            if p not in code_list13:
                code_list13.append(p)
                print(code_list13)
                count13 += 1
        if theme_number == 14:
            if p not in code_list14:
                code_list14.append(p)
                print(code_list14)
                count14 += 1
        if theme_number == 15:
            if p not in code_list15:
                code_list15.append(p)
                print(code_list15)
                count15 += 1
        if theme_number == 16:
            if p not in code_list16:
                code_list16.append(p)
                print(code_list16)
                count16 += 1
        if theme_number == 17:
            if p not in code_list17:
                code_list17.append(p)
                print(code_list17)
                count17 += 1
        if theme_number == 18:
            if p not in code_list18:
                code_list18.append(p)
                print(code_list18)
                count18 += 1
        if theme_number == 19:
            if p not in code_list19:
                code_list19.append(p)
                print(code_list19)
                count19 += 1
        if theme_number == 20:
            if p not in code_list20:
                code_list20.append(p)
                print(code_list20)
                count20 += 1
        return HttpResponseRedirect(reverse('hint:theme_hint', args=[user_id, theme, p]))
    q = request.GET.get('q', '')
    if q != "":
        if q[-1] == '/':
            change = q[:-1]
        else:
            change = q
        code = change.split('/')[-1]
        if request.method == "GET":
            if theme_number == 1:
                if code not in code_list1:
                    code_list1.append(code)
                    print(code_list1)
                    count1 += 1
            if theme_number == 2:
                if code not in code_list2:
                    code_list2.append(code)
                    print(code_list2)
                    count2 += 1
            if theme_number == 3:
                if code not in code_list3:
                    code_list3.append(code)
                    print(code_list3)
                    count3 += 1
            if theme_number == 4:
                if code not in code_list4:
                    code_list4.append(code)
                    print(code_list4)
                    count4 += 1
            if theme_number == 5:
                if code not in code_list5:
                    code_list5.append(code)
                    print(code_list5)
                    count5 += 1
            if theme_number == 6:
                if code not in code_list6:
                    code_list6.append(code)
                    print(code_list6)
                    count6 += 1
            if theme_number == 7:
                if code not in code_list7:
                    code_list7.append(code)
                    print(code_list7)
                    count7 += 1
            if theme_number == 8:
                if code not in code_list8:
                    code_list8.append(code)
                    print(code_list8)
                    count8 += 1
            if theme_number == 9:
                if code not in code_list9:
                    code_list9.append(code)
                    print(code_list9)
                    count9 += 1
            if theme_number == 10:
                if code not in code_list10:
                    code_list10.append(code)
                    print(code_list10)
                    count10 += 1
            if theme_number == 11:
                if code not in code_list11:
                    code_list11.append(code)
                    print(code_list11)
                    count11 += 1
            if theme_number == 12:
                if code not in code_list12:
                    code_list12.append(code)
                    print(code_list12)
                    count12 += 1
            if theme_number == 13:
                if code not in code_list13:
                    code_list13.append(code)
                    print(code_list13)
                    count13 += 1
            if theme_number == 14:
                if code not in code_list14:
                    code_list14.append(code)
                    print(code_list14)
                    count14 += 1
            if theme_number == 15:
                if code not in code_list15:
                    code_list15.append(code)
                    print(code_list15)
                    count15 += 1
            if theme_number == 16:
                if code not in code_list16:
                    code_list16.append(code)
                    print(code_list16)
                    count16 += 1
            if theme_number == 17:
                if code not in code_list17:
                    code_list17.append(code)
                    print(code_list17)
                    count17 += 1
            if theme_number == 18:
                if code not in code_list18:
                    code_list18.append(code)
                    print(code_list18)
                    count18 += 1
            if theme_number == 19:
                if code not in code_list19:
                    code_list19.append(code)
                    print(code_list19)
                    count19 += 1
            if theme_number == 20:
                if code not in code_list20:
                    code_list20.append(code)
                    print(code_list20)
                    count20 += 1
            return redirect(q)
    else:
        pass
    print(count)
    if hintCount > count:
        if hintCode:
            return render(request, 'hint/hint_code.html', {
                'hintCount': hintCount,
                'count': count,
                'theme': theme,
                'escape_room': escape_room,
                'user_id': user_id,
                'nation': nation,
                'interPhone_key': interPhone_key,
                'interPhone_secret': interPhone_secret,
                'interPhone_id': interPhone_id,
                'interPhone_call': interPhone_call,
                'interPhone': interPhone,
            })
        else:
            return render(request, 'hint/qr.html', {
                'hintCount': hintCount,
                'count': count,
                'theme': theme,
                'escape_room': escape_room,
                'user_id': user_id,
                'nation': nation,
                'interPhone_key': interPhone_key,
                'interPhone_secret': interPhone_secret,
                'interPhone_id': interPhone_id,
                'interPhone_call': interPhone_call,
                'interPhone': interPhone,
            })
    else:
        return render(request, 'hint/not_hint.html',{
            'hintCount': hintCount,
            'count': count,
            'theme': theme,
            'escape_room': escape_room,
            'user_id': user_id,
            'nation': nation,
            'interPhone_key': interPhone_key,
            'interPhone_secret': interPhone_secret,
            'interPhone_id': interPhone_id,
            'interPhone_call': interPhone_call,
            'interPhone': interPhone,
        })


@login_required
def theme_hint(request, user_id, theme, hint):
    nation = get_object_or_404(Profile, user=request.user).nation
    theme = get_object_or_404(Theme, name=theme)
    return render(request, 'hint/theme_hint.html', {
        'hint': hint,
        'theme': theme,
        'user_id': user_id,
        'nation': nation
    })


@login_required
def theme_edit(request, user_id, theme):
    nation = get_object_or_404(Profile, user=request.user).nation
    escape_room = get_object_or_404(Profile, user=request.user).escape_room
    theme = get_object_or_404(Theme, name=theme, roomEscape=request.user)
    textHint = get_object_or_404(Profile, user=request.user).textHint
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
        'user_id': user_id,
        'nation': nation,
        'textHint': textHint
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


@login_required
def create(request, user_id):
    hintCode = request.user.profile.hintCode
    themes = Theme.objects.all()
    themes = themes.filter(roomEscape=request.user)
    theme = request.GET.get('theme', '')
    if hintCode:
        return render(request, 'hint/create_hintQR_code.html', {
            'user_id': user_id,
            'theme': theme,
            'themes': themes
        })
    else:
        return render(request, 'hint/create.html', {
            'user_id': user_id,
            'theme': theme,
            'themes': themes
        })


@login_required
def create2(request, user_id):
    hintCode = request.user.profile.hintCode
    themes = Theme.objects.all()
    themes = themes.filter(roomEscape=request.user)
    theme = request.GET.get('theme', '')
    if hintCode:
        return render(request, 'hint/create_hintQR2_code.html', {
            'user_id': user_id,
            'theme': theme,
            'themes': themes
        })
    else:
        return render(request, 'hint/create.html', {
            'user_id': user_id,
            'theme': theme,
            'themes': themes
        })


def personal_information(request):
    return render(request, 'hint/personal_information.html')


@login_required
def admin(request, user_id):
    themes = Theme.objects.all()
    themes = themes.filter(roomEscape=request.user)
    escape_room = get_object_or_404(Profile, user=request.user).escape_room
    return render(request, 'hint/admin.html', {
        'themes': themes,
        'escape_room': escape_room,
        'user_id': user_id
    })


@login_required
def admin_confirm(request, user_id, theme):
    nation = get_object_or_404(Profile, user=request.user).nation
    reset = get_object_or_404(Profile, user=request.user).reset
    escape_room = get_object_or_404(Profile, user=request.user).escape_room
    q = request.GET.get('q', '')

    return render(request, 'hint/admin_confirm.html', {
        'nation': nation,
        'q': q,
        'escape_room': escape_room,
        'reset': reset,
        'user_id': user_id,
        'theme': theme
    })


def enter_key(request, user_id, theme):
    enterKey = get_object_or_404(Theme, roomEscape=request.user, name=theme).enterKey
    escape_room = get_object_or_404(Profile, user=request.user).escape_room
    q = request.GET.get('q', '')
    return render(request, 'hint/enterKey.html', {
        'enterKey': enterKey,
        'escape_room': escape_room,
        'user_id': user_id,
        'q': q,
        'theme': theme
    })



