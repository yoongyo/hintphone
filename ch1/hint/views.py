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
count21 = 0
count22 = 0
count23 = 0
count24 = 0
count25 = 0
count26 = 0
count27 = 0
count28 = 0
count29 = 0
count30 = 0
count31 = 0
count32 = 0
count33 = 0
count34 = 0
count35 = 0
count36 = 0
count37 = 0
count38 = 0
count39 = 0
count40 = 0
count41 = 0
count42 = 0
count43 = 0
count44 = 0
count45 = 0
count46 = 0
count47 = 0
count48 = 0
count49 = 0
count50 = 0
count51 = 0
count52 = 0
count53 = 0
count54 = 0
count55 = 0
count56 = 0
count57 = 0
count58 = 0
count59 = 0
count60 = 0

count101 = 0
count102 = 0
count103 = 0
count104 = 0
count105 = 0
count106 = 0
count107 = 0
count108 = 0
count109 = 0
count110 = 0
count111 = 0
count112 = 0
count113 = 0
count114 = 0
count115 = 0
count116 = 0
count117 = 0
count118 = 0
count119 = 0
count120 = 0
count121 = 0
count122 = 0
count123 = 0
count124 = 0
count125 = 0
count126 = 0
count127 = 0
count128 = 0
count129 = 0
count130 = 0
count131 = 0
count132 = 0
count133 = 0
count134 = 0
count135 = 0
count136 = 0
count137 = 0
count138 = 0
count139 = 0
count140 = 0
count141 = 0
count142 = 0
count143 = 0
count144 = 0
count145 = 0
count146 = 0
count147 = 0
count148 = 0
count149 = 0
count150 = 0
count151 = 0
count152 = 0
count153 = 0
count154 = 0
count155 = 0
count156 = 0
count157 = 0
count158 = 0
count159 = 0
count160 = 0

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
code_list21 = []
code_list22 = []
code_list23 = []
code_list24 = []
code_list25 = []
code_list26 = []
code_list27 = []
code_list28 = []
code_list29 = []
code_list30 = []
code_list31 = []
code_list32 = []
code_list33 = []
code_list34 = []
code_list35 = []
code_list36 = []
code_list37 = []
code_list38 = []
code_list39 = []
code_list40 = []
code_list41 = []
code_list42 = []
code_list43 = []
code_list44 = []
code_list45 = []
code_list46 = []
code_list47 = []
code_list48 = []
code_list49 = []
code_list50 = []
code_list51 = []
code_list52 = []
code_list53 = []
code_list54 = []
code_list55 = []
code_list56 = []
code_list57 = []
code_list58 = []
code_list59 = []
code_list60 = []

code_list101 = []
code_list102 = []
code_list103 = []
code_list104 = []
code_list105 = []
code_list106 = []
code_list107 = []
code_list108 = []
code_list109 = []
code_list110 = []
code_list111 = []
code_list112 = []
code_list113 = []
code_list114 = []
code_list115 = []
code_list116 = []
code_list117 = []
code_list118 = []
code_list119 = []
code_list120 = []
code_list121 = []
code_list122 = []
code_list123 = []
code_list124 = []
code_list125 = []
code_list126 = []
code_list127 = []
code_list128 = []
code_list129 = []
code_list130 = []
code_list131 = []
code_list132 = []
code_list133 = []
code_list134 = []
code_list135 = []
code_list136 = []
code_list137 = []
code_list138 = []
code_list139 = []
code_list140 = []
code_list141 = []
code_list142 = []
code_list143 = []
code_list144 = []
code_list145 = []
code_list146 = []
code_list147 = []
code_list148 = []
code_list149 = []
code_list150 = []
code_list151 = []
code_list152 = []
code_list153 = []
code_list154 = []
code_list155 = []
code_list156 = []
code_list157 = []
code_list158 = []
code_list159 = []
code_list160 = []


def switch(x):
    return {1: count1, 2: count2, 3: count3, 4: count4, 5: count5, 6: count6,
            7: count7, 8: count8, 9: count9, 10: count10, 11: count11, 12: count12,
            13: count13, 14: count14, 15: count15, 16: count16, 17: count17, 18: count18,
            19: count19, 20: count20, 21: count12, 22: count22, 23: count23, 24: count24, 25: count25, 26: count26,
            27: count27, 28: count28, 29: count29, 30: count30, 31: count31, 32: count32,
            33: count33, 34: count34, 35: count35, 36: count36, 37: count37, 38: count38,
            39: count39, 40: count40, 41: count41, 42: count42, 43: count43, 44: count44, 45: count45, 46: count46,
            47: count47, 48: count48, 49: count49, 50: count50, 51: count51, 52: count52,
            53: count53, 54: count54, 55: count55, 56: count56, 57: count57, 58: count58,
            59: count59, 60: count60, 101: count101, 102: count102, 103: count103, 104: count104, 105: count105, 106: count106,
            107: count107, 108: count108, 109: count109, 110: count110, 111: count111, 112: count112,
            113: count113, 114: count114, 115: count115, 116: count116, 117: count117, 118: count118,
            119: count119, 120: count120, 121: count112, 122: count122, 123: count123, 124: count124, 125: count125, 126: count126,
            127: count127, 128: count128, 129: count129, 130: count130, 131: count131, 132: count132,
            133: count133, 134: count134, 135: count135, 136: count136, 137: count137, 138: count138,
            139: count139, 140: count140, 141: count141, 142: count142, 143: count143, 144: count144, 145: count145, 146: count146,
            147: count147, 148: count148, 149: count149, 150: count150, 151: count151, 152: count152,
            153: count153, 154: count154, 155: count155, 156: count156, 157: count157, 158: count158,
            159: count159, 160: count160}.get(x, 0)


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
    if theme_number == 21:
        global count21
        global code_list21
    if theme_number == 22:
        global count22
        global code_list22
    if theme_number == 23:
        global count23
        global code_list23
    if theme_number == 24:
        global count24
        global code_list24
    if theme_number == 25:
        global count25
        global code_list25
    if theme_number == 26:
        global count26
        global code_list26
    if theme_number == 27:
        global count27
        global code_list27
    if theme_number == 28:
        global count28
        global code_list28
    if theme_number == 29:
        global count29
        global code_list29
    if theme_number == 30:
        global count30
        global code_list30
    if theme_number == 31:
        global count31
        global code_list31
    if theme_number == 32:
        global count32
        global code_list32
    if theme_number == 33:
        global count33
        global code_list33
    if theme_number == 34:
        global count34
        global code_list34
    if theme_number == 35:
        global count35
        global code_list35
    if theme_number == 36:
        global count36
        global code_list36
    if theme_number == 37:
        global count37
        global code_list37
    if theme_number == 38:
        global count38
        global code_list38
    if theme_number == 39:
        global count39
        global code_list39
    if theme_number == 40:
        global count40
        global code_list40
    if theme_number == 41:
        global count41
        global code_list41
    if theme_number == 42:
        global count42
        global code_list42
    if theme_number == 43:
        global count43
        global code_list43
    if theme_number == 44:
        global count44
        global code_list44
    if theme_number == 45:
        global count45
        global code_list45
    if theme_number == 46:
        global count46
        global code_list46
    if theme_number == 47:
        global count47
        global code_list47
    if theme_number == 48:
        global count48
        global code_list48
    if theme_number == 49:
        global count49
        global code_list49
    if theme_number == 50:
        global count50
        global code_list50
    if theme_number == 51:
        global count51
        global code_list51
    if theme_number == 52:
        global count52
        global code_list52
    if theme_number == 53:
        global count53
        global code_list53
    if theme_number == 54:
        global count54
        global code_list54
    if theme_number == 55:
        global count55
        global code_list55
    if theme_number == 56:
        global count56
        global code_list56
    if theme_number == 57:
        global count57
        global code_list57
    if theme_number == 58:
        global count58
        global code_list58
    if theme_number == 59:
        global count59
        global code_list59
    if theme_number == 60:
        global count60
        global code_list60

    if theme_number == 101:
        global count101
        global code_list101
    if theme_number == 102:
        global count102
        global code_list102
    if theme_number == 103:
        global count103
        global code_list103
    if theme_number == 104:
        global count104
        global code_list104
    if theme_number == 105:
        global count105
        global code_list105
    if theme_number == 106:
        global count106
        global code_list106
    if theme_number == 107:
        global count107
        global code_list107
    if theme_number == 108:
        global count108
        global code_list108
    if theme_number == 109:
        global count109
        global code_list109
    if theme_number == 110:
        global count110
        global code_list110
    if theme_number == 111:
        global count111
        global code_list111
    if theme_number == 112:
        global count112
        global code_list112
    if theme_number == 113:
        global count113
        global code_list113
    if theme_number == 114:
        global count114
        global code_list114
    if theme_number == 115:
        global count115
        global code_list115
    if theme_number == 116:
        global count116
        global code_list116
    if theme_number == 117:
        global count117
        global code_list117
    if theme_number == 118:
        global count118
        global code_list118
    if theme_number == 119:
        global count119
        global code_list119
    if theme_number == 120:
        global count120
        global code_list120
    if theme_number == 121:
        global count121
        global code_list121
    if theme_number == 122:
        global count122
        global code_list122
    if theme_number == 123:
        global count123
        global code_list123
    if theme_number == 124:
        global count124
        global code_list124
    if theme_number == 125:
        global count125
        global code_list125
    if theme_number == 126:
        global count126
        global code_list126
    if theme_number == 127:
        global count127
        global code_list127
    if theme_number == 128:
        global count128
        global code_list128
    if theme_number == 129:
        global count129
        global code_list129
    if theme_number == 130:
        global count130
        global code_list130
    if theme_number == 131:
        global count131
        global code_list131
    if theme_number == 132:
        global count132
        global code_list132
    if theme_number == 133:
        global count133
        global code_list133
    if theme_number == 134:
        global count134
        global code_list134
    if theme_number == 135:
        global count135
        global code_list135
    if theme_number == 136:
        global count136
        global code_list136
    if theme_number == 137:
        global count137
        global code_list137
    if theme_number == 138:
        global count138
        global code_list138
    if theme_number == 139:
        global count139
        global code_list139
    if theme_number == 140:
        global count140
        global code_list140
    if theme_number == 141:
        global count141
        global code_list141
    if theme_number == 142:
        global count142
        global code_list142
    if theme_number == 143:
        global count143
        global code_list143
    if theme_number == 144:
        global count144
        global code_list144
    if theme_number == 145:
        global count145
        global code_list145
    if theme_number == 146:
        global count146
        global code_list146
    if theme_number == 147:
        global count147
        global code_list147
    if theme_number == 148:
        global count148
        global code_list148
    if theme_number == 149:
        global count149
        global code_list149
    if theme_number == 150:
        global count150
        global code_list150
    if theme_number == 151:
        global count151
        global code_list151
    if theme_number == 152:
        global count152
        global code_list152
    if theme_number == 153:
        global count153
        global code_list153
    if theme_number == 154:
        global count154
        global code_list154
    if theme_number == 155:
        global count155
        global code_list155
    if theme_number == 156:
        global count156
        global code_list156
    if theme_number == 157:
        global count157
        global code_list157
    if theme_number == 158:
        global count158
        global code_list158
    if theme_number == 159:
        global count159
        global code_list159
    if theme_number == 160:
        global count160
        global code_list160

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
        if theme_number == 21:
            count21 = 0
            code_list21 = []
        if theme_number == 22:
            count22 = 0
            code_list22 = []
        if theme_number == 23:
            count23 = 0
            code_list23 = []
        if theme_number == 24:
            count24 = 0
            code_list24 = []
        if theme_number == 25:
            count25 = 0
            code_list25 = []
        if theme_number == 26:
            count26 = 0
            code_list26 = []
        if theme_number == 27:
            count27 = 0
            code_list27 = []
        if theme_number == 28:
            count28 = 0
            code_list28 = []
        if theme_number == 29:
            count29 = 0
            code_list29 = []
        if theme_number == 30:
            count30 = 0
            code_list30 = []
        if theme_number == 31:
            count31 = 0
            code_list31 = []
        if theme_number == 32:
            count32 = 0
            code_list32 = []
        if theme_number == 33:
            count33 = 0
            code_list33 = []
        if theme_number == 34:
            count34 = 0
            code_list34 = []
        if theme_number == 35:
            count35 = 0
            code_list35 = []
        if theme_number == 36:
            count36 = 0
            code_list36 = []
        if theme_number == 37:
            count37 = 0
            code_list37 = []
        if theme_number == 38:
            count38 = 0
            code_list38 = []
        if theme_number == 39:
            count39 = 0
            code_list39 = []
        if theme_number == 40:
            count40 = 0
            code_list40 = []
        if theme_number == 41:
            count41 = 0
            code_list41 = []
        if theme_number == 42:
            count42 = 0
            code_list42 = []
        if theme_number == 43:
            count43 = 0
            code_list43 = []
        if theme_number == 44:
            count44 = 0
            code_list44 = []
        if theme_number == 45:
            count45 = 0
            code_list45 = []
        if theme_number == 46:
            count46 = 0
            code_list46 = []
        if theme_number == 47:
            count47 = 0
            code_list47 = []
        if theme_number == 48:
            count48 = 0
            code_list48 = []
        if theme_number == 49:
            count49 = 0
            code_list49 = []
        if theme_number == 50:
            count50 = 0
            code_list50 = []
        if theme_number == 51:
            count51 = 0
            code_list51 = []
        if theme_number == 52:
            count52 = 0
            code_list52 = []
        if theme_number == 53:
            count53 = 0
            code_list53 = []
        if theme_number == 54:
            count54 = 0
            code_list54 = []
        if theme_number == 55:
            count55 = 0
            code_list55 = []
        if theme_number == 56:
            count56 = 0
            code_list56 = []
        if theme_number == 57:
            count57 = 0
            code_list57 = []
        if theme_number == 58:
            count58 = 0
            code_list58 = []
        if theme_number == 59:
            count59 = 0
            code_list59 = []
        if theme_number == 60:
            count60 = 0
            code_list60 = []

        if theme_number == 101:
            count101 = 0
            code_list101 = []
        if theme_number == 102:
            count102 = 0
            code_list102 = []
        if theme_number == 103:
            count103 = 0
            code_list103 = []
        if theme_number == 104:
            count104 = 0
            code_list104 = []
        if theme_number == 105:
            count105 = 0
            code_list105 = []
        if theme_number == 106:
            count106 = 0
            code_list106 = []
        if theme_number == 107:
            count107 = 0
            code_list107 = []
        if theme_number == 108:
            count108 = 0
            code_list108 = []
        if theme_number == 109:
            count109 = 0
            code_list109 = []
        if theme_number == 110:
            count110 = 0
            code_list110 = []
        if theme_number == 111:
            count111 = 0
            code_list111 = []
        if theme_number == 112:
            count112 = 0
            code_list112 = []
        if theme_number == 113:
            count113 = 0
            code_list113 = []
        if theme_number == 114:
            count114 = 0
            code_list114 = []
        if theme_number == 115:
            count115 = 0
            code_list115 = []
        if theme_number == 116:
            count116 = 0
            code_list116 = []
        if theme_number == 117:
            count117 = 0
            code_list117 = []
        if theme_number == 118:
            count118 = 0
            code_list118 = []
        if theme_number == 119:
            count119 = 0
            code_list119 = []
        if theme_number == 120:
            count120 = 0
            code_list120 = []
        if theme_number == 121:
            count121 = 0
            code_list121 = []
        if theme_number == 122:
            count122 = 0
            code_list122 = []
        if theme_number == 123:
            count123 = 0
            code_list123 = []
        if theme_number == 124:
            count124 = 0
            code_list124 = []
        if theme_number == 125:
            count125 = 0
            code_list125 = []
        if theme_number == 126:
            count126 = 0
            code_list126 = []
        if theme_number == 127:
            count127 = 0
            code_list127 = []
        if theme_number == 128:
            count128 = 0
            code_list128 = []
        if theme_number == 129:
            count129 = 0
            code_list129 = []
        if theme_number == 130:
            count130 = 0
            code_list130 = []
        if theme_number == 131:
            count131 = 0
            code_list131 = []
        if theme_number == 132:
            count132 = 0
            code_list132 = []
        if theme_number == 133:
            count133 = 0
            code_list133 = []
        if theme_number == 134:
            count134 = 0
            code_list134 = []
        if theme_number == 135:
            count135 = 0
            code_list135 = []
        if theme_number == 136:
            count136 = 0
            code_list136 = []
        if theme_number == 137:
            count137 = 0
            code_list137 = []
        if theme_number == 138:
            count138 = 0
            code_list138 = []
        if theme_number == 139:
            count139 = 0
            code_list139 = []
        if theme_number == 140:
            count140 = 0
            code_list140 = []
        if theme_number == 141:
            count141 = 0
            code_list141 = []
        if theme_number == 142:
            count142 = 0
            code_list142 = []
        if theme_number == 143:
            count143 = 0
            code_list143 = []
        if theme_number == 144:
            count144 = 0
            code_list144 = []
        if theme_number == 145:
            count145 = 0
            code_list145 = []
        if theme_number == 146:
            count146 = 0
            code_list146 = []
        if theme_number == 147:
            count147 = 0
            code_list147 = []
        if theme_number == 148:
            count148 = 0
            code_list148 = []
        if theme_number == 149:
            count149 = 0
            code_list149 = []
        if theme_number == 150:
            count150 = 0
            code_list150 = []
        if theme_number == 151:
            count151 = 0
            code_list151 = []
        if theme_number == 152:
            count152 = 0
            code_list152 = []
        if theme_number == 153:
            count153 = 0
            code_list153 = []
        if theme_number == 154:
            count154 = 0
            code_list154 = []
        if theme_number == 155:
            count155 = 0
            code_list155 = []
        if theme_number == 156:
            count156 = 0
            code_list156 = []
        if theme_number == 157:
            count157 = 0
            code_list157 = []
        if theme_number == 158:
            count158 = 0
            code_list158 = []
        if theme_number == 159:
            count159 = 0
            code_list159 = []
        if theme_number == 160:
            count160 = 0
            code_list160 = []
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
    if theme_number == 21:
        global count21
        global code_list21
    if theme_number == 22:
        global count22
        global code_list22
    if theme_number == 23:
        global count23
        global code_list23
    if theme_number == 24:
        global count24
        global code_list24
    if theme_number == 25:
        global count25
        global code_list25
    if theme_number == 26:
        global count26
        global code_list26
    if theme_number == 27:
        global count27
        global code_list27
    if theme_number == 28:
        global count28
        global code_list28
    if theme_number == 29:
        global count29
        global code_list29
    if theme_number == 30:
        global count30
        global code_list30
    if theme_number == 31:
        global count31
        global code_list31
    if theme_number == 32:
        global count32
        global code_list32
    if theme_number == 33:
        global count33
        global code_list33
    if theme_number == 34:
        global count34
        global code_list34
    if theme_number == 35:
        global count35
        global code_list35
    if theme_number == 36:
        global count36
        global code_list36
    if theme_number == 37:
        global count37
        global code_list37
    if theme_number == 38:
        global count38
        global code_list38
    if theme_number == 39:
        global count39
        global code_list39
    if theme_number == 40:
        global count40
        global code_list40
    if theme_number == 41:
        global count41
        global code_list41
    if theme_number == 42:
        global count42
        global code_list42
    if theme_number == 43:
        global count43
        global code_list43
    if theme_number == 44:
        global count44
        global code_list44
    if theme_number == 45:
        global count45
        global code_list45
    if theme_number == 46:
        global count46
        global code_list46
    if theme_number == 47:
        global count47
        global code_list47
    if theme_number == 48:
        global count48
        global code_list48
    if theme_number == 49:
        global count49
        global code_list49
    if theme_number == 50:
        global count50
        global code_list50
    if theme_number == 51:
        global count51
        global code_list51
    if theme_number == 52:
        global count52
        global code_list52
    if theme_number == 53:
        global count53
        global code_list53
    if theme_number == 54:
        global count54
        global code_list54
    if theme_number == 55:
        global count55
        global code_list55
    if theme_number == 56:
        global count56
        global code_list56
    if theme_number == 57:
        global count57
        global code_list57
    if theme_number == 58:
        global count58
        global code_list58
    if theme_number == 59:
        global count59
        global code_list59
    if theme_number == 60:
        global count60
        global code_list60

    if theme_number == 101:
        global count101
        global code_list101
    if theme_number == 102:
        global count102
        global code_list102
    if theme_number == 103:
        global count103
        global code_list103
    if theme_number == 104:
        global count104
        global code_list104
    if theme_number == 105:
        global count105
        global code_list105
    if theme_number == 106:
        global count106
        global code_list106
    if theme_number == 107:
        global count107
        global code_list107
    if theme_number == 108:
        global count108
        global code_list108
    if theme_number == 109:
        global count109
        global code_list109
    if theme_number == 110:
        global count110
        global code_list110
    if theme_number == 111:
        global count111
        global code_list111
    if theme_number == 112:
        global count112
        global code_list112
    if theme_number == 113:
        global count113
        global code_list113
    if theme_number == 114:
        global count114
        global code_list114
    if theme_number == 115:
        global count115
        global code_list115
    if theme_number == 116:
        global count116
        global code_list116
    if theme_number == 117:
        global count117
        global code_list117
    if theme_number == 118:
        global count118
        global code_list118
    if theme_number == 119:
        global count119
        global code_list119
    if theme_number == 120:
        global count120
        global code_list120
    if theme_number == 121:
        global count121
        global code_list121
    if theme_number == 122:
        global count122
        global code_list122
    if theme_number == 123:
        global count123
        global code_list123
    if theme_number == 124:
        global count124
        global code_list124
    if theme_number == 125:
        global count125
        global code_list125
    if theme_number == 126:
        global count126
        global code_list126
    if theme_number == 127:
        global count127
        global code_list127
    if theme_number == 128:
        global count128
        global code_list128
    if theme_number == 129:
        global count129
        global code_list129
    if theme_number == 130:
        global count130
        global code_list130
    if theme_number == 131:
        global count131
        global code_list131
    if theme_number == 132:
        global count132
        global code_list132
    if theme_number == 133:
        global count133
        global code_list133
    if theme_number == 134:
        global count134
        global code_list134
    if theme_number == 135:
        global count135
        global code_list135
    if theme_number == 136:
        global count136
        global code_list136
    if theme_number == 137:
        global count137
        global code_list137
    if theme_number == 138:
        global count138
        global code_list138
    if theme_number == 139:
        global count139
        global code_list139
    if theme_number == 140:
        global count140
        global code_list140
    if theme_number == 141:
        global count141
        global code_list141
    if theme_number == 142:
        global count142
        global code_list142
    if theme_number == 143:
        global count143
        global code_list143
    if theme_number == 144:
        global count144
        global code_list144
    if theme_number == 145:
        global count145
        global code_list145
    if theme_number == 146:
        global count146
        global code_list146
    if theme_number == 147:
        global count147
        global code_list147
    if theme_number == 148:
        global count148
        global code_list148
    if theme_number == 149:
        global count149
        global code_list149
    if theme_number == 150:
        global count150
        global code_list150
    if theme_number == 151:
        global count151
        global code_list151
    if theme_number == 152:
        global count152
        global code_list152
    if theme_number == 153:
        global count153
        global code_list153
    if theme_number == 154:
        global count154
        global code_list154
    if theme_number == 155:
        global count155
        global code_list155
    if theme_number == 156:
        global count156
        global code_list156
    if theme_number == 157:
        global count157
        global code_list157
    if theme_number == 158:
        global count158
        global code_list158
    if theme_number == 159:
        global count159
        global code_list159
    if theme_number == 160:
        global count160
        global code_list160
    count = switch(theme_number)
    print("pk:", theme_number, 'count:', count)
    escape_room = get_object_or_404(Profile, user=request.user).escape_room
    hintCount = get_object_or_404(Theme, name=theme, roomEscape=request.user).hintCount
    if request.method == "POST":
        p = request.POST.get('p', '')
        if theme_number == 1:
            if p not in code_list1:
                code_list1.append(p)
                count1 += 1
        if theme_number == 2:
            if p not in code_list2:
                code_list2.append(p)
                count2 += 1
        if theme_number == 3:
            if p not in code_list3:
                code_list3.append(p)
                count3 += 1
        if theme_number == 4:
            if p not in code_list4:
                code_list4.append(p)
                count4 += 1
        if theme_number == 5:
            if p not in code_list5:
                code_list5.append(p)
                count5 += 1
        if theme_number == 6:
            if p not in code_list6:
                code_list6.append(p)
                count6 += 1
        if theme_number == 7:
            if p not in code_list7:
                code_list7.append(p)
                count7 += 1
        if theme_number == 8:
            if p not in code_list8:
                code_list8.append(p)
                count8 += 1
        if theme_number == 9:
            if p not in code_list9:
                code_list9.append(p)
                count9 += 1
        if theme_number == 10:
            if p not in code_list10:
                code_list10.append(p)
                count10 += 1
        if theme_number == 11:
            if p not in code_list11:
                code_list11.append(p)
                count11 += 1
        if theme_number == 12:
            if p not in code_list12:
                code_list12.append(p)
                count12 += 1
        if theme_number == 13:
            if p not in code_list13:
                code_list13.append(p)
                count13 += 1
        if theme_number == 14:
            if p not in code_list14:
                code_list14.append(p)
                count14 += 1
        if theme_number == 15:
            if p not in code_list15:
                code_list15.append(p)
                count15 += 1
        if theme_number == 16:
            if p not in code_list16:
                code_list16.append(p)
                count16 += 1
        if theme_number == 17:
            if p not in code_list17:
                code_list17.append(p)
                count17 += 1
        if theme_number == 18:
            if p not in code_list18:
                code_list18.append(p)
                count18 += 1
        if theme_number == 19:
            if p not in code_list19:
                code_list19.append(p)
                count19 += 1
        if theme_number == 20:
            if p not in code_list20:
                code_list20.append(p)
                count20 += 1
        if theme_number == 21:
            if p not in code_list21:
                code_list21.append(p)
                count21 += 1
        if theme_number == 22:
            if p not in code_list22:
                code_list22.append(p)
                count22 += 1
        if theme_number == 23:
            if p not in code_list23:
                code_list23.append(p)
                count23 += 1
        if theme_number == 24:
            if p not in code_list24:
                code_list24.append(p)
                count24 += 1
        if theme_number == 25:
            if p not in code_list25:
                code_list25.append(p)
                count25 += 1
        if theme_number == 26:
            if p not in code_list26:
                code_list26.append(p)
                count26 += 1
        if theme_number == 27:
            if p not in code_list27:
                code_list27.append(p)
                count27 += 1
        if theme_number == 28:
            if p not in code_list28:
                code_list28.append(p)
                count28 += 1
        if theme_number == 29:
            if p not in code_list29:
                code_list29.append(p)
                count29 += 1
        if theme_number == 30:
            if p not in code_list30:
                code_list30.append(p)
                count30 += 1
        if theme_number == 31:
            if p not in code_list31:
                code_list31.append(p)
                count31 += 1
        if theme_number == 32:
            if p not in code_list32:
                code_list32.append(p)
                count32 += 1
        if theme_number == 33:
            if p not in code_list33:
                code_list33.append(p)
                count33 += 1
        if theme_number == 34:
            if p not in code_list34:
                code_list34.append(p)
                count34 += 1
        if theme_number == 35:
            if p not in code_list35:
                code_list35.append(p)
                count35 += 1
        if theme_number == 36:
            if p not in code_list36:
                code_list36.append(p)
                count36 += 1
        if theme_number == 37:
            if p not in code_list37:
                code_list37.append(p)
                count37 += 1
        if theme_number == 38:
            if p not in code_list38:
                code_list38.append(p)
                count38 += 1
        if theme_number == 39:
            if p not in code_list39:
                code_list39.append(p)
                count39 += 1
        if theme_number == 40:
            if p not in code_list40:
                code_list40.append(p)
                count40 += 1
        if theme_number == 41:
            if p not in code_list41:
                code_list41.append(p)
                count41 += 1
        if theme_number == 42:
            if p not in code_list42:
                code_list42.append(p)
                count42 += 1
        if theme_number == 43:
            if p not in code_list43:
                code_list43.append(p)
                count43 += 1
        if theme_number == 44:
            if p not in code_list44:
                code_list44.append(p)
                count44 += 1
        if theme_number == 45:
            if p not in code_list45:
                code_list45.append(p)
                count45 += 1
        if theme_number == 46:
            if p not in code_list46:
                code_list46.append(p)
                count46 += 1
        if theme_number == 47:
            if p not in code_list47:
                code_list47.append(p)
                count47 += 1
        if theme_number == 48:
            if p not in code_list48:
                code_list48.append(p)
                count48 += 1
        if theme_number == 49:
            if p not in code_list49:
                code_list49.append(p)
                count49 += 1
        if theme_number == 50:
            if p not in code_list50:
                code_list50.append(p)
                count50 += 1
        if theme_number == 51:
            if p not in code_list51:
                code_list51.append(p)
                count51 += 1
        if theme_number == 52:
            if p not in code_list52:
                code_list52.append(p)
                count52 += 1
        if theme_number == 53:
            if p not in code_list53:
                code_list53.append(p)
                count53 += 1
        if theme_number == 54:
            if p not in code_list54:
                code_list54.append(p)
                count54 += 1
        if theme_number == 55:
            if p not in code_list55:
                code_list55.append(p)
                count55 += 1
        if theme_number == 56:
            if p not in code_list56:
                code_list56.append(p)
                count56 += 1
        if theme_number == 57:
            if p not in code_list57:
                code_list57.append(p)
                count57 += 1
        if theme_number == 58:
            if p not in code_list58:
                code_list58.append(p)
                count58 += 1
        if theme_number == 59:
            if p not in code_list59:
                code_list59.append(p)
                count59 += 1
        if theme_number == 60:
            if p not in code_list60:
                code_list60.append(p)
                count60 += 1

        if theme_number == 101:
            if p not in code_list101:
                code_list101.append(p)
                count101 += 1
        if theme_number == 102:
            if p not in code_list102:
                code_list102.append(p)
                count102 += 1
        if theme_number == 103:
            if p not in code_list103:
                code_list103.append(p)
                count103 += 1
        if theme_number == 104:
            if p not in code_list104:
                code_list104.append(p)
                count104 += 1
        if theme_number == 105:
            if p not in code_list105:
                code_list105.append(p)
                count105 += 1
        if theme_number == 106:
            if p not in code_list106:
                code_list106.append(p)
                count106 += 1
        if theme_number == 107:
            if p not in code_list107:
                code_list107.append(p)
                count107 += 1
        if theme_number == 108:
            if p not in code_list108:
                code_list108.append(p)
                count108 += 1
        if theme_number == 109:
            if p not in code_list109:
                code_list109.append(p)
                count109 += 1
        if theme_number == 110:
            if p not in code_list110:
                code_list110.append(p)
                count110 += 1
        if theme_number == 111:
            if p not in code_list111:
                code_list111.append(p)
                count111 += 1
        if theme_number == 112:
            if p not in code_list112:
                code_list112.append(p)
                count112 += 1
        if theme_number == 113:
            if p not in code_list113:
                code_list113.append(p)
                count113 += 1
        if theme_number == 114:
            if p not in code_list114:
                code_list114.append(p)
                count114 += 1
        if theme_number == 115:
            if p not in code_list115:
                code_list115.append(p)
                count115 += 1
        if theme_number == 116:
            if p not in code_list116:
                code_list116.append(p)
                count116 += 1
        if theme_number == 117:
            if p not in code_list117:
                code_list117.append(p)
                count117 += 1
        if theme_number == 118:
            if p not in code_list118:
                code_list118.append(p)
                count118 += 1
        if theme_number == 119:
            if p not in code_list119:
                code_list119.append(p)
                count119 += 1
        if theme_number == 120:
            if p not in code_list120:
                code_list120.append(p)
                count120 += 1
        if theme_number == 121:
            if p not in code_list121:
                code_list121.append(p)
                count121 += 1
        if theme_number == 122:
            if p not in code_list122:
                code_list122.append(p)
                count122 += 1
        if theme_number == 123:
            if p not in code_list123:
                code_list123.append(p)
                count123 += 1
        if theme_number == 124:
            if p not in code_list124:
                code_list124.append(p)
                count124 += 1
        if theme_number == 125:
            if p not in code_list125:
                code_list125.append(p)
                count125 += 1
        if theme_number == 126:
            if p not in code_list126:
                code_list126.append(p)
                count126 += 1
        if theme_number == 127:
            if p not in code_list127:
                code_list127.append(p)
                count127 += 1
        if theme_number == 128:
            if p not in code_list128:
                code_list128.append(p)
                count128 += 1
        if theme_number == 129:
            if p not in code_list129:
                code_list129.append(p)
                count129 += 1
        if theme_number == 130:
            if p not in code_list130:
                code_list130.append(p)
                count130 += 1
        if theme_number == 131:
            if p not in code_list131:
                code_list131.append(p)
                count131 += 1
        if theme_number == 132:
            if p not in code_list132:
                code_list132.append(p)
                count132 += 1
        if theme_number == 133:
            if p not in code_list133:
                code_list133.append(p)
                count133 += 1
        if theme_number == 134:
            if p not in code_list134:
                code_list134.append(p)
                count134 += 1
        if theme_number == 135:
            if p not in code_list135:
                code_list135.append(p)
                count135 += 1
        if theme_number == 136:
            if p not in code_list136:
                code_list136.append(p)
                count136 += 1
        if theme_number == 137:
            if p not in code_list137:
                code_list137.append(p)
                count137 += 1
        if theme_number == 138:
            if p not in code_list138:
                code_list138.append(p)
                count138 += 1
        if theme_number == 139:
            if p not in code_list139:
                code_list139.append(p)
                count139 += 1
        if theme_number == 140:
            if p not in code_list140:
                code_list140.append(p)
                count140 += 1
        if theme_number == 141:
            if p not in code_list141:
                code_list141.append(p)
                count141 += 1
        if theme_number == 142:
            if p not in code_list142:
                code_list142.append(p)
                count142 += 1
        if theme_number == 143:
            if p not in code_list143:
                code_list143.append(p)
                count143 += 1
        if theme_number == 144:
            if p not in code_list144:
                code_list144.append(p)
                count144 += 1
        if theme_number == 145:
            if p not in code_list145:
                code_list145.append(p)
                count145 += 1
        if theme_number == 146:
            if p not in code_list146:
                code_list146.append(p)
                count146 += 1
        if theme_number == 147:
            if p not in code_list147:
                code_list147.append(p)
                count147 += 1
        if theme_number == 148:
            if p not in code_list148:
                code_list148.append(p)
                count148 += 1
        if theme_number == 149:
            if p not in code_list149:
                code_list149.append(p)
                count149 += 1
        if theme_number == 150:
            if p not in code_list150:
                code_list150.append(p)
                count150 += 1
        if theme_number == 151:
            if p not in code_list151:
                code_list151.append(p)
                count151 += 1
        if theme_number == 152:
            if p not in code_list152:
                code_list152.append(p)
                count152 += 1
        if theme_number == 153:
            if p not in code_list153:
                code_list153.append(p)
                count153 += 1
        if theme_number == 154:
            if p not in code_list154:
                code_list154.append(p)
                count154 += 1
        if theme_number == 155:
            if p not in code_list155:
                code_list155.append(p)
                count155 += 1
        if theme_number == 156:
            if p not in code_list156:
                code_list156.append(p)
                count156 += 1
        if theme_number == 157:
            if p not in code_list157:
                code_list157.append(p)
                count157 += 1
        if theme_number == 158:
            if p not in code_list158:
                code_list158.append(p)
                count158 += 1
        if theme_number == 159:
            if p not in code_list159:
                code_list159.append(p)
                count159 += 1
        if theme_number == 160:
            if p not in code_list160:
                code_list160.append(p)
                count160 += 1
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
                    count1 += 1
            if theme_number == 2:
                if code not in code_list2:
                    code_list2.append(code)
                    count2 += 1
            if theme_number == 3:
                if code not in code_list3:
                    code_list3.append(code)
                    count3 += 1
            if theme_number == 4:
                if code not in code_list4:
                    code_list4.append(code)
                    count4 += 1
            if theme_number == 5:
                if code not in code_list5:
                    code_list5.append(code)
                    count5 += 1
            if theme_number == 6:
                if code not in code_list6:
                    code_list6.append(code)
                    count6 += 1
            if theme_number == 7:
                if code not in code_list7:
                    code_list7.append(code)
                    count7 += 1
            if theme_number == 8:
                if code not in code_list8:
                    code_list8.append(code)
                    count8 += 1
            if theme_number == 9:
                if code not in code_list9:
                    code_list9.append(code)
                    count9 += 1
            if theme_number == 10:
                if code not in code_list10:
                    code_list10.append(code)
                    count10 += 1
            if theme_number == 11:
                if code not in code_list11:
                    code_list11.append(code)
                    count11 += 1
            if theme_number == 12:
                if code not in code_list12:
                    code_list12.append(code)
                    count12 += 1
            if theme_number == 13:
                if code not in code_list13:
                    code_list13.append(code)
                    count13 += 1
            if theme_number == 14:
                if code not in code_list14:
                    code_list14.append(code)
                    count14 += 1
            if theme_number == 15:
                if code not in code_list15:
                    code_list15.append(code)
                    count15 += 1
            if theme_number == 16:
                if code not in code_list16:
                    code_list16.append(code)
                    count16 += 1
            if theme_number == 17:
                if code not in code_list17:
                    code_list17.append(code)
                    count17 += 1
            if theme_number == 18:
                if code not in code_list18:
                    code_list18.append(code)
                    count18 += 1
            if theme_number == 19:
                if code not in code_list19:
                    code_list19.append(code)
                    count19 += 1
            if theme_number == 20:
                if code not in code_list20:
                    code_list20.append(code)
                    count20 += 1
            if theme_number == 21:
                if code not in code_list21:
                    code_list21.append(code)
                    count21 += 1
            if theme_number == 22:
                if code not in code_list22:
                    code_list22.append(code)
                    count22 += 1
            if theme_number == 23:
                if code not in code_list23:
                    code_list23.append(code)
                    count23 += 1
            if theme_number == 24:
                if code not in code_list24:
                    code_list24.append(code)
                    count24 += 1
            if theme_number == 25:
                if code not in code_list25:
                    code_list25.append(code)
                    count25 += 1
            if theme_number == 26:
                if code not in code_list26:
                    code_list26.append(code)
                    count26 += 1
            if theme_number == 27:
                if code not in code_list27:
                    code_list27.append(code)
                    count27 += 1
            if theme_number == 28:
                if code not in code_list28:
                    code_list28.append(code)
                    count28 += 1
            if theme_number == 29:
                if code not in code_list29:
                    code_list29.append(code)
                    count29 += 1
            if theme_number == 30:
                if code not in code_list30:
                    code_list30.append(code)
                    count30 += 1
            if theme_number == 31:
                if code not in code_list31:
                    code_list31.append(code)
                    count31 += 1
            if theme_number == 32:
                if code not in code_list32:
                    code_list32.append(code)
                    count32 += 1
            if theme_number == 33:
                if code not in code_list33:
                    code_list33.append(code)
                    count33 += 1
            if theme_number == 34:
                if code not in code_list34:
                    code_list34.append(code)
                    count34 += 1
            if theme_number == 35:
                if code not in code_list35:
                    code_list35.append(code)
                    count35 += 1
            if theme_number == 36:
                if code not in code_list36:
                    code_list36.append(code)
                    count36 += 1
            if theme_number == 37:
                if code not in code_list37:
                    code_list37.append(code)
                    count37 += 1
            if theme_number == 38:
                if code not in code_list38:
                    code_list38.append(code)
                    count38 += 1
            if theme_number == 39:
                if code not in code_list39:
                    code_list39.append(code)
                    count39 += 1
            if theme_number == 40:
                if code not in code_list40:
                    code_list40.append(code)
                    count40 += 1
            if theme_number == 41:
                if code not in code_list41:
                    code_list41.append(code)
                    count41 += 1
            if theme_number == 42:
                if code not in code_list42:
                    code_list42.append(code)
                    count42 += 1
            if theme_number == 43:
                if code not in code_list43:
                    code_list43.append(code)
                    count43 += 1
            if theme_number == 44:
                if code not in code_list44:
                    code_list44.append(code)
                    count44 += 1
            if theme_number == 45:
                if code not in code_list45:
                    code_list45.append(code)
                    count45 += 1
            if theme_number == 46:
                if code not in code_list46:
                    code_list46.append(code)
                    count46 += 1
            if theme_number == 47:
                if code not in code_list47:
                    code_list47.append(code)
                    count47 += 1
            if theme_number == 48:
                if code not in code_list48:
                    code_list48.append(code)
                    count48 += 1
            if theme_number == 49:
                if code not in code_list49:
                    code_list49.append(code)
                    count49 += 1
            if theme_number == 50:
                if code not in code_list50:
                    code_list50.append(code)
                    count50 += 1
            if theme_number == 51:
                if code not in code_list51:
                    code_list51.append(code)
                    count51 += 1
            if theme_number == 52:
                if code not in code_list52:
                    code_list52.append(code)
                    count52 += 1
            if theme_number == 53:
                if code not in code_list53:
                    code_list53.append(code)
                    count53 += 1
            if theme_number == 54:
                if code not in code_list54:
                    code_list54.append(code)
                    count54 += 1
            if theme_number == 55:
                if code not in code_list55:
                    code_list55.append(code)
                    count55 += 1
            if theme_number == 56:
                if code not in code_list56:
                    code_list56.append(code)
                    count56 += 1
            if theme_number == 57:
                if code not in code_list57:
                    code_list57.append(code)
                    count57 += 1
            if theme_number == 58:
                if code not in code_list58:
                    code_list58.append(code)
                    count58 += 1
            if theme_number == 59:
                if code not in code_list59:
                    code_list59.append(code)
                    count59 += 1
            if theme_number == 60:
                if code not in code_list60:
                    code_list60.append(code)
                    count60 += 1

            if theme_number == 101:
                if code not in code_list101:
                    code_list101.append(code)
                    count101 += 1
            if theme_number == 102:
                if code not in code_list102:
                    code_list102.append(code)
                    count102 += 1
            if theme_number == 103:
                if code not in code_list103:
                    code_list103.append(code)
                    count103 += 1
            if theme_number == 104:
                if code not in code_list104:
                    code_list104.append(code)
                    count104 += 1
            if theme_number == 105:
                if code not in code_list105:
                    code_list105.append(code)
                    count105 += 1
            if theme_number == 106:
                if code not in code_list106:
                    code_list106.append(code)
                    count106 += 1
            if theme_number == 107:
                if code not in code_list107:
                    code_list107.append(code)
                    count107 += 1
            if theme_number == 108:
                if code not in code_list108:
                    code_list108.append(code)
                    count108 += 1
            if theme_number == 109:
                if code not in code_list109:
                    code_list109.append(code)
                    count109 += 1
            if theme_number == 110:
                if code not in code_list110:
                    code_list110.append(code)
                    count10 += 1
            if theme_number == 111:
                if code not in code_list111:
                    code_list111.append(code)
                    count111 += 1
            if theme_number == 112:
                if code not in code_list112:
                    code_list112.append(code)
                    count112 += 1
            if theme_number == 113:
                if code not in code_list113:
                    code_list113.append(code)
                    count113 += 1
            if theme_number == 114:
                if code not in code_list114:
                    code_list114.append(code)
                    count114 += 1
            if theme_number == 115:
                if code not in code_list115:
                    code_list115.append(code)
                    count115 += 1
            if theme_number == 116:
                if code not in code_list116:
                    code_list116.append(code)
                    count116 += 1
            if theme_number == 117:
                if code not in code_list117:
                    code_list117.append(code)
                    count117 += 1
            if theme_number == 118:
                if code not in code_list118:
                    code_list118.append(code)
                    count118 += 1
            if theme_number == 119:
                if code not in code_list119:
                    code_list119.append(code)
                    count119 += 1
            if theme_number == 120:
                if code not in code_list120:
                    code_list120.append(code)
                    count120 += 1
            if theme_number == 121:
                if code not in code_list121:
                    code_list121.append(code)
                    count121 += 1
            if theme_number == 122:
                if code not in code_list122:
                    code_list122.append(code)
                    count122 += 1
            if theme_number == 123:
                if code not in code_list123:
                    code_list123.append(code)
                    count123 += 1
            if theme_number == 124:
                if code not in code_list124:
                    code_list124.append(code)
                    count124 += 1
            if theme_number == 125:
                if code not in code_list125:
                    code_list125.append(code)
                    count125 += 1
            if theme_number == 126:
                if code not in code_list126:
                    code_list126.append(code)
                    count126 += 1
            if theme_number == 127:
                if code not in code_list127:
                    code_list127.append(code)
                    count127 += 1
            if theme_number == 128:
                if code not in code_list128:
                    code_list128.append(code)
                    count128 += 1
            if theme_number == 129:
                if code not in code_list129:
                    code_list129.append(code)
                    count129 += 1
            if theme_number == 130:
                if code not in code_list130:
                    code_list130.append(code)
                    count130 += 1
            if theme_number == 131:
                if code not in code_list131:
                    code_list131.append(code)
                    count131 += 1
            if theme_number == 132:
                if code not in code_list132:
                    code_list132.append(code)
                    count132 += 1
            if theme_number == 133:
                if code not in code_list133:
                    code_list133.append(code)
                    count133 += 1
            if theme_number == 134:
                if code not in code_list134:
                    code_list134.append(code)
                    count134 += 1
            if theme_number == 135:
                if code not in code_list135:
                    code_list135.append(code)
                    count135 += 1
            if theme_number == 136:
                if code not in code_list136:
                    code_list136.append(code)
                    count136 += 1
            if theme_number == 137:
                if code not in code_list137:
                    code_list137.append(code)
                    count137 += 1
            if theme_number == 138:
                if code not in code_list138:
                    code_list138.append(code)
                    count138 += 1
            if theme_number == 139:
                if code not in code_list139:
                    code_list139.append(code)
                    count139 += 1
            if theme_number == 140:
                if code not in code_list140:
                    code_list140.append(code)
                    count140 += 1
            if theme_number == 141:
                if code not in code_list141:
                    code_list141.append(code)
                    count141 += 1
            if theme_number == 142:
                if code not in code_list142:
                    code_list142.append(code)
                    count142 += 1
            if theme_number == 143:
                if code not in code_list143:
                    code_list143.append(code)
                    count143 += 1
            if theme_number == 144:
                if code not in code_list144:
                    code_list144.append(code)
                    count144 += 1
            if theme_number == 145:
                if code not in code_list145:
                    code_list145.append(code)
                    count145 += 1
            if theme_number == 146:
                if code not in code_list146:
                    code_list146.append(code)
                    count146 += 1
            if theme_number == 147:
                if code not in code_list147:
                    code_list147.append(code)
                    count147 += 1
            if theme_number == 148:
                if code not in code_list148:
                    code_list148.append(code)
                    count148 += 1
            if theme_number == 149:
                if code not in code_list149:
                    code_list149.append(code)
                    count149 += 1
            if theme_number == 150:
                if code not in code_list150:
                    code_list150.append(code)
                    count150 += 1
            if theme_number == 151:
                if code not in code_list151:
                    code_list151.append(code)
                    count151 += 1
            if theme_number == 152:
                if code not in code_list152:
                    code_list152.append(code)
                    count152 += 1
            if theme_number == 153:
                if code not in code_list153:
                    code_list153.append(code)
                    count153 += 1
            if theme_number == 154:
                if code not in code_list154:
                    code_list154.append(code)
                    count154 += 1
            if theme_number == 155:
                if code not in code_list155:
                    code_list155.append(code)
                    count155 += 1
            if theme_number == 156:
                if code not in code_list156:
                    code_list156.append(code)
                    count156 += 1
            if theme_number == 157:
                if code not in code_list157:
                    code_list157.append(code)
                    count157 += 1
            if theme_number == 158:
                if code not in code_list158:
                    code_list158.append(code)
                    count158 += 1
            if theme_number == 159:
                if code not in code_list159:
                    code_list159.append(code)
                    count159 += 1
            if theme_number == 160:
                if code not in code_list160:
                    code_list160.append(code)
                    count160 += 1
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
        return render(request, 'hint/not_hint.html', {
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

    return render(request, 'hint/theme_hint.html', {
        'hint': hint,
        'theme': theme,
        'user_id': user_id,
        'nation': nation,
        'mainHint': mainHint,
        'subHint': subHint,
        'textHint': textHint,
        'sub_textHint': sub_textHint,
        'answer': answer
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



