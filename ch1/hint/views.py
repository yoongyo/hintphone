from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse, redirect, HttpResponse
from .models import Theme
from django.contrib.auth.decorators import login_required
import sys
sys.path.append('..')
from accounts.models import Profile
from .forms import HintForm


@login_required
def theme_list(request, user_id):
    themes = Theme.objects.filter(roomEscape=request.user)
    escape_room = get_object_or_404(Profile, user=request.user).escape_room
    nation = get_object_or_404(Profile, user=request.user).nation
    user_id = request.user.username
    return render(request, 'hint/theme_list.html', {
        'themes': themes,
        'escape_room': escape_room,
        'user_id': user_id,
        'nation': nation
    })


@login_required
def reset_code(request, user_id, theme):
    nation = get_object_or_404(Profile, user=request.user).nation
    reset = get_object_or_404(Profile, user=request.user).reset
    user_id = request.user.username
    theme = Theme.objects.get(name=theme, roomEscape=request.user)
    escape_room = get_object_or_404(Profile, user=request.user).escape_room
    q = request.GET.get('q', '')
    okTimer = get_object_or_404(Profile, user=request.user).timer
    timer = get_object_or_404(Theme, name=theme, roomEscape=request.user).timer

    if q == reset:
        theme.currentHint = ''
        theme.currentCount = 0
        theme.save()
    return render(request, 'hint/reset_code.html', {
        'reset': reset,
        'q': q,
        'theme': theme,
        'user_id': user_id,
        'escape_room': escape_room,
        'nation': nation,
        'okTimer': okTimer,
        'timer': timer
    })


@login_required
def QR_code(request, user_id, theme):
    nation = get_object_or_404(Profile, user=request.user).nation
    escape_room = get_object_or_404(Profile, user=request.user).escape_room
    hintCount = get_object_or_404(Theme, name=theme, roomEscape=request.user).hintCount
    currentCount = get_object_or_404(Theme, name=theme, roomEscape=request.user).currentCount
    timer = get_object_or_404(Theme, name=theme, roomEscape=request.user).timer
    okTimer = get_object_or_404(Profile, user=request.user).timer
    pause = get_object_or_404(Profile, user=request.user).pause

    if request.method == "POST":
        p = request.POST.get('p', '')
        return HttpResponseRedirect(reverse('hint:theme_hint', args=[user_id, theme, p]))
    q = request.GET.get('q', '')
    if q != "":
        if request.method == "GET":
            return redirect(q)

    if hintCount > currentCount:
        return render(request, 'hint/hint_code.html', {
            'hintCount': hintCount,
            'count': currentCount,
            'theme': theme,
            'escape_room': escape_room,
            'user_id': user_id,
            'nation': nation,
            'timer': timer,
            'okTimer': okTimer,
            'pause': pause
        })
    else:
        return render(request, 'hint/not_hint.html', {
            'hintCount': hintCount,
            'count': currentCount,
            'theme': theme,
            'escape_room': escape_room,
            'user_id': user_id,
            'nation': nation,
            'timer': timer,
            'okTimer': okTimer,
            'pause': pause
        })


@login_required
def theme_hint(request, user_id, theme, hint):
    nation = get_object_or_404(Profile, user=request.user).nation
    answer = get_object_or_404(Profile, user=request.user).answer
    theme = get_object_or_404(Theme, name=theme, roomEscape=request.user)

    if hint == '1':
        mainHint = theme.hint1
        subHint = theme.sub_hint1
        textHint = theme.textHint1
        sub_textHint = theme.sub_textHint1
    elif hint == '2':
        mainHint = theme.hint2
        subHint = theme.sub_hint2
        textHint = theme.textHint2
        sub_textHint = theme.sub_textHint2
    elif hint == '3':
        mainHint = theme.hint3
        subHint = theme.sub_hint3
        textHint = theme.textHint3
        sub_textHint = theme.sub_textHint3
    elif hint == '4':
        mainHint = theme.hint4
        subHint = theme.sub_hint4
        textHint = theme.textHint4
        sub_textHint = theme.sub_textHint4
    elif hint == '5':
        mainHint = theme.hint5
        subHint = theme.sub_hint5
        textHint = theme.textHint5
        sub_textHint = theme.sub_textHint5
    elif hint == '6':
        mainHint = theme.hint6
        subHint = theme.sub_hint6
        textHint = theme.textHint6
        sub_textHint = theme.sub_textHint6
    elif hint == '7':
        mainHint = theme.hint7
        subHint = theme.sub_hint7
        textHint = theme.textHint7
        sub_textHint = theme.sub_textHint7
    elif hint == '8':
        mainHint = theme.hint8
        subHint = theme.sub_hint8
        textHint = theme.textHint8
        sub_textHint = theme.sub_textHint8
    elif hint == '9':
        mainHint = theme.hint9
        subHint = theme.sub_hint9
        textHint = theme.textHint9
        sub_textHint = theme.sub_textHint9
    elif hint == '10':
        mainHint = theme.hint10
        subHint = theme.sub_hint10
        textHint = theme.textHint10
        sub_textHint = theme.sub_textHint10
    elif hint == '11':
        mainHint = theme.hint11
        subHint = theme.sub_hint11
        textHint = theme.textHint11
        sub_textHint = theme.sub_textHint11
    elif hint == '12':
        mainHint = theme.hint12
        subHint = theme.sub_hint12
        textHint = theme.textHint12
        sub_textHint = theme.sub_textHint12
    elif hint == '13':
        mainHint = theme.hint13
        subHint = theme.sub_hint13
        textHint = theme.textHint13
        sub_textHint = theme.sub_textHint13
    elif hint == '14':
        mainHint = theme.hint14
        subHint = theme.sub_hint14
        textHint = theme.textHint14
        sub_textHint = theme.sub_textHint14
    elif hint == '15':
        mainHint = theme.hint15
        subHint = theme.sub_hint15
        textHint = theme.textHint15
        sub_textHint = theme.sub_textHint15
    elif hint == '16':
        mainHint = theme.hint16
        subHint = theme.sub_hint16
        textHint = theme.textHint16
        sub_textHint = theme.sub_textHint16
    elif hint == '17':
        mainHint = theme.hint17
        subHint = theme.sub_hint17
        textHint = theme.textHint17
        sub_textHint = theme.sub_textHint17
    elif hint == '18':
        mainHint = theme.hint18
        subHint = theme.sub_hint18
        textHint = theme.textHint18
        sub_textHint = theme.sub_textHint18
    elif hint == '19':
        mainHint = theme.hint19
        subHint = theme.sub_hint19
        textHint = theme.textHint19
        sub_textHint = theme.sub_textHint19
    elif hint == '20':
        mainHint = theme.hint20
        subHint = theme.sub_hint20
        textHint = theme.textHint20
        sub_textHint = theme.sub_textHint20
    elif hint == '21':
        mainHint = theme.hint21
        subHint = theme.sub_hint21
        textHint = theme.textHint21
        sub_textHint = theme.sub_textHint21
    elif hint == '22':
        mainHint = theme.hint22
        subHint = theme.sub_hint22
        textHint = theme.textHint22
        sub_textHint = theme.sub_textHint22
    elif hint == '23':
        mainHint = theme.hint23
        subHint = theme.sub_hint23
        textHint = theme.textHint23
        sub_textHint = theme.sub_textHint23
    elif hint == '24':
        mainHint = theme.hint24
        subHint = theme.sub_hint24
        textHint = theme.textHint24
        sub_textHint = theme.sub_textHint24
    elif hint == '25':
        mainHint = theme.hint25
        subHint = theme.sub_hint25
        textHint = theme.textHint25
        sub_textHint = theme.sub_textHint25
    elif hint == '26':
        mainHint = theme.hint26
        subHint = theme.sub_hint26
        textHint = theme.textHint26
        sub_textHint = theme.sub_textHint26
    elif hint == '27':
        mainHint = theme.hint27
        subHint = theme.sub_hint27
        textHint = theme.textHint27
        sub_textHint = theme.sub_textHint27
    elif hint == '28':
        mainHint = theme.hint28
        subHint = theme.sub_hint28
        textHint = theme.textHint28
        sub_textHint = theme.sub_textHint28
    elif hint == '29':
        mainHint = theme.hint29
        subHint = theme.sub_hint29
        textHint = theme.textHint29
        sub_textHint = theme.sub_textHint29
    elif hint == '30':
        mainHint = theme.hint30
        subHint = theme.sub_hint30
        textHint = theme.textHint30
        sub_textHint = theme.sub_textHint30
    elif hint == '31':
        mainHint = theme.hint31
        subHint = theme.sub_hint31
        textHint = theme.textHint31
        sub_textHint = theme.sub_textHint31
    elif hint == '32':
        mainHint = theme.hint32
        subHint = theme.sub_hint32
        textHint = theme.textHint32
        sub_textHint = theme.sub_textHint32
    elif hint == '33':
        mainHint = theme.hint33
        subHint = theme.sub_hint33
        textHint = theme.textHint33
        sub_textHint = theme.sub_textHint33
    elif hint == '34':
        mainHint = theme.hint34
        subHint = theme.sub_hint34
        textHint = theme.textHint34
        sub_textHint = theme.sub_textHint34
    elif hint == '35':
        mainHint = theme.hint35
        subHint = theme.sub_hint35
        textHint = theme.textHint35
        sub_textHint = theme.sub_textHint35
    elif hint == '36':
        mainHint = theme.hint36
        subHint = theme.sub_hint36
        textHint = theme.textHint36
        sub_textHint = theme.sub_textHint36
    elif hint == '37':
        mainHint = theme.hint37
        subHint = theme.sub_hint37
        textHint = theme.textHint37
        sub_textHint = theme.sub_textHint37
    elif hint == '38':
        mainHint = theme.hint38
        subHint = theme.sub_hint38
        textHint = theme.textHint38
        sub_textHint = theme.sub_textHint38
    elif hint == '39':
        mainHint = theme.hint39
        subHint = theme.sub_hint39
        textHint = theme.textHint39
        sub_textHint = theme.sub_textHint39
    elif hint == '40':
        mainHint = theme.hint40
        subHint = theme.sub_hint40
        textHint = theme.textHint40
        sub_textHint = theme.sub_textHint40
    elif hint == '41':
        mainHint = theme.hint41
        subHint = theme.sub_hint41
        textHint = theme.textHint41
        sub_textHint = theme.sub_textHint41
    elif hint == '42':
        mainHint = theme.hint42
        subHint = theme.sub_hint42
        textHint = theme.textHint42
        sub_textHint = theme.sub_textHint42
    elif hint == '43':
        mainHint = theme.hint43
        subHint = theme.sub_hint43
        textHint = theme.textHint43
        sub_textHint = theme.sub_textHint43
    elif hint == '44':
        mainHint = theme.hint44
        subHint = theme.sub_hint44
        textHint = theme.textHint44
        sub_textHint = theme.sub_textHint44
    elif hint == '45':
        mainHint = theme.hint45
        subHint = theme.sub_hint45
        textHint = theme.textHint45
        sub_textHint = theme.sub_textHint45
    elif hint == '46':
        mainHint = theme.hint46
        subHint = theme.sub_hint46
        textHint = theme.textHint46
        sub_textHint = theme.sub_textHint46
    elif hint == '47':
        mainHint = theme.hint47
        subHint = theme.sub_hint47
        textHint = theme.textHint47
        sub_textHint = theme.sub_textHint47
    elif hint == '48':
        mainHint = theme.hint48
        subHint = theme.sub_hint48
        textHint = theme.textHint48
        sub_textHint = theme.sub_textHint48
    elif hint == '49':
        mainHint = theme.hint49
        subHint = theme.sub_hint49
        textHint = theme.textHint49
        sub_textHint = theme.sub_textHint49
    elif hint == '50':
        mainHint = theme.hint50
        subHint = theme.sub_hint50
        textHint = theme.textHint50
        sub_textHint = theme.sub_textHint50
    elif hint == '51':
        mainHint = theme.hint51
        subHint = theme.sub_hint51
        textHint = theme.textHint51
        sub_textHint = theme.sub_textHint51
    elif hint == '52':
        mainHint = theme.hint52
        subHint = theme.sub_hint52
        textHint = theme.textHint52
        sub_textHint = theme.sub_textHint52
    elif hint == '53':
        mainHint = theme.hint53
        subHint = theme.sub_hint53
        textHint = theme.textHint53
        sub_textHint = theme.sub_textHint53
    elif hint == '54':
        mainHint = theme.hint54
        subHint = theme.sub_hint54
        textHint = theme.textHint54
        sub_textHint = theme.sub_textHint54
    elif hint == '55':
        mainHint = theme.hint55
        subHint = theme.sub_hint55
        textHint = theme.textHint55
        sub_textHint = theme.sub_textHint55
    elif hint == '56':
        mainHint = theme.hint56
        subHint = theme.sub_hint56
        textHint = theme.textHint56
        sub_textHint = theme.sub_textHint56
    elif hint == '57':
        mainHint = theme.hint57
        subHint = theme.sub_hint57
        textHint = theme.textHint57
        sub_textHint = theme.sub_textHint57
    elif hint == '58':
        mainHint = theme.hint58
        subHint = theme.sub_hint58
        textHint = theme.textHint58
        sub_textHint = theme.sub_textHint58
    elif hint == '59':
        mainHint = theme.hint59
        subHint = theme.sub_hint59
        textHint = theme.textHint59
        sub_textHint = theme.sub_textHint59
    elif hint == '60':
        mainHint = theme.hint60
        subHint = theme.sub_hint60
        textHint = theme.textHint60
        sub_textHint = theme.sub_textHint60
    elif hint == '61':
        mainHint = theme.hint61
        subHint = theme.sub_hint61
        textHint = theme.textHint61
        sub_textHint = theme.sub_textHint61
    elif hint == '62':
        mainHint = theme.hint62
        subHint = theme.sub_hint62
        textHint = theme.textHint62
        sub_textHint = theme.sub_textHint62
    elif hint == '63':
        mainHint = theme.hint63
        subHint = theme.sub_hint63
        textHint = theme.textHint63
        sub_textHint = theme.sub_textHint63
    elif hint == '64':
        mainHint = theme.hint64
        subHint = theme.sub_hint64
        textHint = theme.textHint64
        sub_textHint = theme.sub_textHint64
    elif hint == '65':
        mainHint = theme.hint65
        subHint = theme.sub_hint65
        textHint = theme.textHint65
        sub_textHint = theme.sub_textHint65
    elif hint == '66':
        mainHint = theme.hint66
        subHint = theme.sub_hint66
        textHint = theme.textHint66
        sub_textHint = theme.sub_textHint66
    elif hint == '67':
        mainHint = theme.hint67
        subHint = theme.sub_hint67
        textHint = theme.textHint67
        sub_textHint = theme.sub_textHint67
    elif hint == '68':
        mainHint = theme.hint68
        subHint = theme.sub_hint68
        textHint = theme.textHint68
        sub_textHint = theme.sub_textHint68
    elif hint == '69':
        mainHint = theme.hint69
        subHint = theme.sub_hint69
        textHint = theme.textHint69
        sub_textHint = theme.sub_textHint69
    elif hint == '70':
        mainHint = theme.hint70
        subHint = theme.sub_hint70
        textHint = theme.textHint70
        sub_textHint = theme.sub_textHint70
    elif hint == '71':
        mainHint = theme.hint71
        subHint = theme.sub_hint71
        textHint = theme.textHint71
        sub_textHint = theme.sub_textHint71
    elif hint == '72':
        mainHint = theme.hint72
        subHint = theme.sub_hint72
        textHint = theme.textHint72
        sub_textHint = theme.sub_textHint72
    elif hint == '73':
        mainHint = theme.hint73
        subHint = theme.sub_hint73
        textHint = theme.textHint73
        sub_textHint = theme.sub_textHint73
    elif hint == '74':
        mainHint = theme.hint74
        subHint = theme.sub_hint74
        textHint = theme.textHint74
        sub_textHint = theme.sub_textHint74
    elif hint == '75':
        mainHint = theme.hint75
        subHint = theme.sub_hint75
        textHint = theme.textHint75
        sub_textHint = theme.sub_textHint75
    elif hint == '76':
        mainHint = theme.hint76
        subHint = theme.sub_hint76
        textHint = theme.textHint76
        sub_textHint = theme.sub_textHint76
    elif hint == '77':
        mainHint = theme.hint77
        subHint = theme.sub_hint77
        textHint = theme.textHint77
        sub_textHint = theme.sub_textHint77
    elif hint == '78':
        mainHint = theme.hint78
        subHint = theme.sub_hint78
        textHint = theme.textHint78
        sub_textHint = theme.sub_textHint78
    elif hint == '79':
        mainHint = theme.hint79
        subHint = theme.sub_hint79
        textHint = theme.textHint79
        sub_textHint = theme.sub_textHint79
    elif hint == '80':
        mainHint = theme.hint80
        subHint = theme.sub_hint80
        textHint = theme.textHint80
        sub_textHint = theme.sub_textHint80
    else:
        mainHint = False
        subHint = False
        textHint = False
        sub_textHint = False

    theme = Theme.objects.get(name=theme, roomEscape=request.user)
    currentHint = theme.currentHint.split(',')
    okTimer = get_object_or_404(Profile, user=request.user).timer
    if hint not in currentHint:
        theme.currentHint = theme.currentHint + (hint+',')
        theme.currentCount = theme.currentCount + 1
        theme.save()

    return render(request, 'hint/theme_hint.html', {
        'hint': hint,
        'theme': theme,
        'user_id': user_id,
        'nation': nation,
        'mainHint': mainHint,
        'subHint': subHint,
        'textHint': textHint,
        'sub_textHint': sub_textHint,
        'answer': answer,
        'okTimer': okTimer
    })


@login_required
def theme_edit(request, user_id, theme):
    nation = get_object_or_404(Profile, user=request.user).nation
    escape_room = get_object_or_404(Profile, user=request.user).escape_room
    theme = get_object_or_404(Theme, name=theme, roomEscape=request.user)
    textHint = get_object_or_404(Profile, user=request.user).textHint
    manyHint = theme.manyHint
    timer = get_object_or_404(Profile, user=request.user).timer

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
        'textHint': textHint,
        'manyHint': manyHint,
        'timer': timer,
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


@login_required
def create(request, user_id):
    themes = Theme.objects.all()
    themes = themes.filter(roomEscape=request.user)
    theme = request.GET.get('theme', '')
    return render(request, 'hint/create_hintQR_code.html', {
        'user_id': user_id,
        'theme': theme,
        'themes': themes
    })


@login_required
def create2(request, user_id):
    themes = Theme.objects.all()
    themes = themes.filter(roomEscape=request.user)
    theme = request.GET.get('theme', '')
    return render(request, 'hint/create_hintQR2_code.html', {
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
    timer = get_object_or_404(Theme, roomEscape=request.user, name=theme).timer
    okTimer = get_object_or_404(Profile, user=request.user).timer

    q = request.GET.get('q', '')
    return render(request, 'hint/enterKey.html', {
        'enterKey': enterKey,
        'escape_room': escape_room,
        'user_id': user_id,
        'q': q,
        'theme': theme,
        'timer': timer,
        'okTimer': okTimer
    })


def laurentia(request):
    theme = get_object_or_404(Theme, name='로렌시아')
    if request.method == 'POST':
        form = HintForm(request.POST, request.FILES, instance=theme)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('hint:laurentia_complete'))
        else:
            print(form.errors)
    else:
        form = HintForm(instance=theme)
    return render(request, 'hint/laurentia.html', {
        'form': form
    })


def laurentia_complete(request):
    return render(request, 'hint/laurentia_complete.html')


def ordinary(request):
    theme = get_object_or_404(Theme, name='평범한하루')
    if request.method == 'POST':
        form = HintForm(request.POST, request.FILES, instance=theme)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('hint:ordinary_complete'))
        else:
            print(form.errors)
    else:
        form = HintForm(instance=theme)
    return render(request, 'hint/ordinary.html', {
        'form': form
    })


def ordinary_complete(request):
    return render(request, 'hint/ordinary_complete.html')



