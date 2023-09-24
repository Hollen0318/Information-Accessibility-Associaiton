from math import log
from time import time
import sys

def position_determination(values,RGB):
    match = {1:'Red',2:'Green',3:'Blue'}
    for i in range(0,len(RGB)):
        if values == RGB[i]:
            return match[i+1]
def RGB_to_HSV(RGB):
    field_value ={'Red':0,'Green':0,'Blue':0}
    fieds = ['Red','Green','Blue']
    for i in range(0,len(RGB)):
        field_value[fieds[i]] = RGB[i]
    HSV = []
    max_RGB = 0
    max_RGB_color = ''
    min_RGB = 0
    min_RGB_color = ''
    med_RGB = 0
    med_RGB_color = ''
    hues = 0
    saturation = 0
    brightness = 0
    if field_value[fieds[0]]==field_value[fieds[1]]==field_value[fieds[2]]:
        brightness = max(RGB)/255
        hues = 0
        saturation = 0
    elif field_value[fieds[0]]!=field_value[fieds[1]] and field_value[fieds[1]]!=field_value[fieds[2]] and field_value[fieds[0]]!=field_value[fieds[2]]:
        min_RGB = min(RGB)
        max_RGB = max(RGB)
        min_RGB_color = position_determination(min_RGB,RGB)
        max_RGB_color = position_determination(max_RGB, RGB)
        for item in RGB:
            if item!=min(RGB) and item!=max(RGB):
                med_RGB = item
                med_RGB_color = position_determination(med_RGB,RGB)
        saturation = (max_RGB-min_RGB)/max_RGB
        match = {'Red': 0, 'Green': 120, 'Blue': 240}
        hues += match[max_RGB_color]
        if med_RGB_color == 'Red' and max_RGB_color == 'Green':
            hues -= (med_RGB-min(RGB))/(max(RGB)-min(RGB))*60
        elif med_RGB_color == 'Green' and max_RGB_color == 'Blue':
            hues -= (med_RGB - min(RGB)) / (max(RGB) - min(RGB)) * 60
        elif med_RGB_color == 'Blue' and max_RGB_color == 'Red':
            hues -= (med_RGB - min(RGB)) / (max(RGB) - min(RGB)) * 60
        else:
            hues += (med_RGB - min(RGB)) / (max(RGB) - min(RGB)) * 60
        if hues <0:
            hues += 360
        brightness = max_RGB / 255
        saturation = (max_RGB - min_RGB) / max_RGB
    else:
        max_same = 0
        min_same = 0
        order_of_max_same = [0,0,0]
        order_of_min_same = [0,0,0]
        for item in range(0,len(RGB)):
            if RGB[item] == max(RGB):
                max_same += 1
                order_of_max_same[item] = 1
            if RGB[item] == min(RGB):
                min_same += 1
                order_of_min_same[item] = 1
        if min_same == 2:
            min_RGB = min(RGB)
            max_RGB = max(RGB)
            med_RGB = min(RGB)
            min_RGB_color = position_determination(min_RGB, RGB)
            max_RGB_color = position_determination(max_RGB, RGB)
            brightness = max_RGB/255
            for item in fieds:
                if item != min_RGB_color and item != max_RGB_color:
                    med_RGB_color = item
            saturation = (max_RGB - min_RGB) / max_RGB
            match = {'Red': 0, 'Green': 120, 'Blue': 240}
            hues += match[max_RGB_color]
        elif max_same == 2 and order_of_max_same.index(0)==1:
            med_RGB = RGB[0]
            med_RGB_color = 'Red'
            min_RGB = RGB[1]
            min_RGB_color = 'Green'
            max_RGB = RGB[2]
            max_RGB_color = 'Blue'
            match = {'Red': 0, 'Green': 120, 'Blue': 240}
            hues += match[max_RGB_color]+60
            saturation = (max_RGB - min_RGB) / max_RGB
            brightness = max_RGB / 255
        elif max_same == 2 and order_of_max_same.index(0) == 0:
            min_RGB = RGB[0]
            min_RGB_color = 'Red'
            med_RGB = RGB[1]
            med_RGB_color = 'Green'
            max_RGB = RGB[2]
            max_RGB_color = 'Blue'
            match = {'Red': 0, 'Green': 120, 'Blue': 240}
            hues += match[max_RGB_color] - 60
            saturation = (max_RGB - min_RGB) / max_RGB
            brightness = max_RGB / 255
        elif max_same == 2 and order_of_max_same.index(0) == 2:
            min_RGB = RGB[2]
            min_RGB_color = 'Blue'
            max_RGB = RGB[1]
            max_RGB_color = 'Green'
            med_RGB = RGB[0]
            med_RGB_color = 'Red'
            match = {'Red': 0, 'Green': 120, 'Blue': 240}
            hues += match[max_RGB_color] - 60
            saturation = (max_RGB - min_RGB) / max_RGB
            brightness = max_RGB / 255
    HSV.append(hues)
    HSV.append(saturation)
    HSV.append((brightness))
    return HSV
def HSB_to_RGB(HSB):
    max_color_position = ''
    RGB = [0, 0, 0]
    if 0< HSB[0]<60 or 300<HSB[0]<360:
        max_color_position = 'Red'
    elif 60<HSB[0]<120 or 120<HSB[0]<180:
        max_color_position = 'Green'
    elif 180<HSB[0]<240 or 240<HSB[0]<300:
        max_color_position = 'Blue'
    elif HSB[0] == 0 and HSB[1] == 0:
        for i in range(0,len(RGB)):
            RGB[i] = round(HSB[2]*255)
        return RGB
    elif HSB[0] == 0 and HSB[1] != 0:
        max_color_position = 'Red'
        RGB[0] = round(HSB[2]*255)
        RGB[1] = round(HSB[2]*255*(1-HSB[1]))
        RGB[2] = RGB[1]
        return RGB
    elif HSB[0] == 120:
        max_color_position = 'Green'
        RGB[1] = round(HSB[2]*255)
        RGB[0] = round(HSB[2]*255*(1-HSB[1]))
        RGB[2] = RGB[0]
        return RGB
    elif HSB[0] == 240:
        max_color_position = 'Blue'
        RGB[2] = round(HSB[2]*255)
        RGB[0] = round(HSB[2]*255*(1-HSB[1]))
        RGB[1] = RGB[0]
        return RGB
    elif HSB[0] == 60:
        max_color_position = 'Green'
        RGB[1] = round(HSB[2]*255)
        RGB[0] = RGB[1]
        RGB[2] = round(HSB[2]*255*(1-HSB[1]))
        return RGB
    elif HSB[0] == 180:
        max_color_position = 'Blue'
        RGB[2] = round(HSB[2]*255)
        RGB[1] = RGB[2]
        RGB[0] = round(HSB[2]*255*(1-HSB[1]))
        return RGB
    elif HSB[0] == 300:
        max_color_position = 'Red'
        RGB[0] = round(HSB[2]*255)
        RGB[2] = RGB[0]
        RGB[1] = round(HSB[2]*255*(1-HSB[1]))
        return RGB
    position = {'Red': 0, 'Green': 1, 'Blue': 2}
    max_RGB = round(HSB[2]*255)
    min_RGB = max_RGB*(1-HSB[1])
    match = {'Red':0,'Green':120,'Blue':240}
    sign = '-'
    if HSB[0]-match[max_color_position]<0 and max_color_position == 'Red':
        med_color = 'Blue'
        min_color = 'Green'
    elif HSB[0]-match[max_color_position]<0 and max_color_position == 'Green':
        med_color = 'Red'
        min_color = 'Blue'
    elif HSB[0]-match[max_color_position]<0 and max_color_position == 'Blue':
        med_color = 'Green'
        min_color = 'Red'
    elif 0<HSB[0]-match[max_color_position]<60 and max_color_position == 'Red':
        sign = '+'
        med_color = 'Green'
        min_color = 'Blue'
    elif HSB[0]-match[max_color_position]>60 and max_color_position == 'Red':
        sign = '-'
        med_color = 'Blue'
        min_color = 'Green'
    elif HSB[0]-match[max_color_position]>0 and max_color_position == 'Green':
        sign='+'
        med_color = 'Blue'
        min_color = 'Red'
    elif HSB[0]-match[max_color_position]>0 and max_color_position == 'Blue':
        sign = '+'
        med_color = 'Red'
        min_color = 'Green'
    med_RGB = 0
    if sign == '-' and HSB[0]<300:
        med_RGB = (match[max_color_position] - HSB[0])*(max_RGB-min_RGB)/60+min_RGB
    elif sign == '-' and 300<HSB[0]<360:
        med_RGB = (match[max_color_position] - HSB[0]+360)*(max_RGB-min_RGB)/60+min_RGB
    else:
        med_RGB = (HSB[0] - match[max_color_position])*(max_RGB-min_RGB)/60+min_RGB
    position = {'Red':0,'Green':1,'Blue':2}
    RGB = [0,0,0]
    RGB[position[max_color_position]] = round(max_RGB)
    RGB[position[min_color]] = round(min_RGB)
    RGB[position[med_color]] = round(med_RGB)
    return RGB

def position_determination(values,RGB):
    match = {1:'Red',2:'Green',3:'Blue'}
    for i in range(0,len(RGB)):
        if values == RGB[i]:
            return match[i+1]

def get_abstract_ratio_from_two_RGB_strings(color_1,color_2):
    list_1 = get_RGB(color_1)
    list_2 = get_RGB(color_2)
    return get_abstract_ratio(list_1,list_2)
def convert_RGB_to_String(RGB_list):
    RGB_String = ''
    for var in RGB_list:
        if var > 15:
            RGB_String += hex(var)[2:]
        else:
            RGB_String +='0'
            RGB_String += hex(var)[2:]
    return RGB_String
def get_RGB(color):
    list = []
    r_hex = int(color[0:2],16)
    g_hex = int(color[2:4],16)
    b_hex = int(color[4:6],16)
    list.append(r_hex)
    list.append(g_hex)
    list.append(b_hex)
    return list
def get_Rs(RGB):
    list=[]
    for a in range(0,len(RGB)):
        list.append(RGB[a]/255)
    return list
def get_R(RGBs):
    list = []
    for a in range(0, len(RGBs)):
        if RGBs[a] <= 0.03928:
            list.append(RGBs[a]/12.92)
        else:
            list.append(pow(((RGBs[a]+0.055)/1.055),2.4))
    return list
def get_luminance(RGB_R):
    return 0.2126 * RGB_R[0] + 0.7152 * RGB_R[1] + 0.0722 * RGB_R[2]

def get_abstract_ratio(RGB_1,RGB_2):
    RGB_1_s = get_Rs(RGB_1)
    RGB_2_s = get_Rs(RGB_2)
    RGB_1_R = get_R(RGB_1_s)
    RGB_2_R = get_R(RGB_2_s)
    pre_abstract = (get_luminance(RGB_1_R)+0.05)/(get_luminance(RGB_2_R)+0.05)
    if pre_abstract <1:
        return 1/pre_abstract
    else:
        return pre_abstract
def judge(b):
    result = []
    if (b*12.92)<=0.03928:
        b_RGB = int(b*12.92*255)
        result.append(b_RGB)
    if (log(b,2.4)*1.055-0.055)>0.03928:
        b_RGB = int((log(b,2.4)*1.055-0.055)*255)
        result.append(b_RGB)
    return result
def distance(color_1,color_2):
    return pow((pow((color_1[0]-color_2[0]),2)+pow((color_1[1]-color_2[1]),2)+pow((color_1[2]-color_2[2]),2)),(1/2))
#get_abstract_ratio(color_1,color_2)
def ahive_goal_via_HSV(color_var,color_cons,goal):
    print('??')
    goal = float(goal)
    hsv_color_var = RGB_to_HSV(color_var)
    hsv_color_var_h = hsv_color_var[0]
    see_goal = [hsv_color_var_h,0,0]
    min = 9999999999
    goal = [0,0,0]
    for s in range (0,1,0.1):
        see_goal[1] = s
        for v in range(0,1,0.1):
            see_goal[2] = v
            print(see_goal)
            if get_abstract_ratio(color_cons,HSB_to_RGB(see_goal)) == goal:
                if distance(HSB_to_RGB(see_goal),color_var)<min:
                    goal = HSB_to_RGB(see_goal)
    return goal

def achive_goal(color_var,color_cons,goal):
    goal = float(goal)
    color_var_Rs = get_Rs(color_var)
    color_var_R = get_R(color_var_Rs)
    color_cons_Rs = get_Rs(color_cons)
    color_cons_R = get_R(color_cons_Rs)
    #不变的颜色的L
    constant_luminancae = get_luminance(color_cons_R)
    # 变的颜色的L
    variable_luminancae = get_luminance(color_var_R)
    #print(color_var,variable_luminancae,color_cons,constant_luminancae)
    # 要达到的L
    if variable_luminancae > constant_luminancae:
        goal_luminance = goal*(constant_luminancae+0.05)-0.05
    else:
        goal_luminance = (constant_luminancae+0.05)/goal-0.05
    min = 442
    min_color = []
    if 0 < goal_luminance < 1:
        for r in range(0,256):
            for g in range (0,256):
                list = []
                list.append(r)
                list.append(g)
                list_Rs = get_Rs(list)
                list_R = get_R(list_Rs)
                b =(goal_luminance-0.2126*list_R[0]-0.7152*list_R[1])/0.0722
                if b > 0 and b<1 and len(judge(b)) != 0:
                    for var in judge(b):
                        list.append(var)
                        #print("选中颜色",list,'距离为',distance(list,color_var))
                        if distance(list,color_var)<min:
                            min = distance(list,color_var)
                            min_color = list
                else:
                    continue
    if min_color == []:
        new_goal = format(goal-0.1, '.2f')
        min_color = achive_goal(color_var, color_cons,new_goal)
    return min_color

print(RGB_to_HSV([244,111,110]))
'''color_1,color_2 = input("请输入两个颜色的RGB字符串如F0F0F0 000000并以空格隔开\n").split(' ')
print("{}与{}颜色的对比度为{}，需要调整对比度嘛？".format(color_1,color_2,format(get_abstract_ratio_from_two_RGB_strings(color_1,color_2),'.2f')))
goal_abstract_ratio = input("请输入需要的对比度，退出请输入【0】")
notice = False
#goal_abstract_rati = 4.5
if goal_abstract_ratio != '0':
    goal_abstract_ratio = format(float(goal_abstract_ratio), '.1f')
    start_time = time()
    target_color_string_1 = convert_RGB_to_String(achive_goal(get_RGB(color_2),get_RGB(color_1),goal_abstract_ratio)).upper()
    target_color_string_2 = convert_RGB_to_String(achive_goal(get_RGB(color_1), get_RGB(color_2),goal_abstract_ratio)).upper()
    scenario_failed = 0
    if get_abstract_ratio_from_two_RGB_strings(color_1,
        target_color_string_1) < float(goal_abstract_ratio)-0.1 or get_abstract_ratio_from_two_RGB_strings(color_2,
                target_color_string_2) < float(goal_abstract_ratio)-0.1 :
        notice = True
    if get_abstract_ratio_from_two_RGB_strings(color_1,
        target_color_string_1) < float(goal_abstract_ratio)-0.1:
            scenario_failed = 1
    else:
        scenario_failed = 2
    if notice == True:
        print("【注意】方案{}的颜色对比度调整超出阈值，无法获取！适当调整目标对比度。".format(scenario_failed))
    print("方案1：若保持{}颜色不变，可将{}调整至{}颜色，对比度为{}".
          format(color_1,color_2,target_color_string_1,get_abstract_ratio_from_two_RGB_strings(color_1,target_color_string_1)))
    print("该方案下的颜色对比可参考网址: https://contrast-ratio.com/#%23{}-on-%23{}。".format(color_1,target_color_string_1))
    print("方案2：若保持{}颜色不变，可将{}调整至{}颜色，对比度为{}。".
          format(color_2, color_1, target_color_string_2,
                 get_abstract_ratio_from_two_RGB_strings(color_2, target_color_string_2)))
    print("该方案下的颜色对比可参考网址: https://contrast-ratio.com/#%23{}-on-%23{}。".format(target_color_string_2,color_2))
    end_time = time()
    print("原颜色参考网址: https://contrast-ratio.com/#%23{}-on-%23{}\n共耗时{}秒。".format(color_1,color_2,format((end_time-start_time),'.7f')))
elif goal_abstract_ratio == '0':
    exit()
else:
    print("请输入1或0")
input("点击任意键退出")'''