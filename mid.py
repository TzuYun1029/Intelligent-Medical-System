import random
import food_list
import speech_recognition as sr
import os
import urllib
import socket
from gtts import gTTS
from record import record
import oled_2
import Adafruit_SSD1306
import ultrasonic
import time
import dcmotor

global choose_list
# cloose_list = []
global food 
global wheel
global input_text
global word
global add_choose
disp = Adafruit_SSD1306.SSD1306_128_32(rst = 0)


def chinese_recognize(wav_file): # 語音辨識
    r = sr.Recognizer()
    with sr.WavFile(wav_file) as source:
        audio = r.record(source)
    try:
        result = r.recognize_google(audio, language='zh-tw')
        return result
    except LookupError:
        print("Could not understand audio:" , wav_file)
        return None

def print_output(output_text):
    # time.sleep(0.1)
    output_text1 = output_text[0:8]
    output_text2 = output_text[8:]
    oled_2.display_text(output_text1,output_text2)
    output = gTTS(output_text,lang='zh-tw')
    output.save("test.mp3")
    os.system("mpg123 test.mp3")
    print(output_text)
    
    return True

def get_input():
    oled_2.display_text("   請說話"," _(:3」∠)_  ")
    record()
    input_text = chinese_recognize("recording.wav")
    # input_text = input()
    return input_text


def topic_food(choose_list,food,add_choose, wheel):
    # food = True
    add_choose = False
    choose_list = []
    print_output("想先問問你有特別喜歡吃的店嗎")
    input_text = get_input()
    print_output("原來如此我最喜歡吃潛艇堡了") 

    # if food == True:
    while True:
        choose_list = food_list.food_list_copy()
        print_output("你要吃正餐或其他")
        input_text = get_input()

        for i in range(len(input_text) - 1):
            word = input_text[i] + input_text[i + 1]
            if word == "正餐" or word == "其他" or word == "都不":
                break
        if word == "正餐":
            for element in choose_list[:]:
                if element[1] != "正餐" and element[1] != "速食" and element[1] != "自助" and element[1] != "都有":
                    choose_list.remove(element)
            while True:
                print_output("你想吃飯或是麵或其他或都可以")
                input_text = get_input()
                for i in range(len(input_text)):
                    word = input_text[i]
                    if word == "飯" or word == "麵" or word == "不" or word == "可" or word == "其":
                        break
                if word == "飯":
                    for element in choose_list[:]:
                        if element[2] != "飯" and element[2] != "都有":
                            choose_list.remove(element)
                    break
                elif word == "麵":
                    for element in choose_list[:]:
                        if element[2] != "麵" and element[2] != "都有":
                            choose_list.remove(element)
                    break
                elif word == "不":
                    print_output("欸認真一點")
                elif word == "可":
                    break
                elif word == "其":
                    for element in choose_list[:]:
                        if element[2] != "其他":
                            choose_list.remove(element)
                    break
                else:
                    print_output("請說正餐或其他")
            while True:
                print_output("好開心喔跟我一樣欸那你想吃中式或西式")
                input_text = get_input()
                for i in range(len(input_text)):
                    word = input_text[i]
                    if word == "中" or word == "西" or word == "不" or word == "可" or word == "其":
                        break
                if word == "中":
                    for element in choose_list[:]:
                        if element[3] != "中式" and element[3] != "都有":
                            choose_list.remove(element)
                    break
                elif word == "西":
                    for element in choose_list[:]:
                        if element[3] != "西式" and element[3] != "都有":
                            choose_list.remove(element)
                    break
                elif word == "不":
                    print_output("欸認真一點")
                elif word == "可":
                    break
                elif word == "其":
                    for element in choose_list[:]:
                        if element[3] != "其他":
                            choose_list.remove(element)
                    break
                else:
                    print_output("請說中式或西式或其他")
            while True:
                print_output("那你會吃辣嗎")
                input_text = get_input()
                for i in range(len(input_text)):
                    word = input_text[i]
                    if word == "不" or word == "會"or word == "都":
                        break
                if word == "不":
                    for element in choose_list[:]:
                        if element[4] != "都有" and element[4] != "不辣":
                            choose_list.remove(element)
                    break
                elif word == "會":
                    break
                elif word == "都":
                    break
                else:
                    print_output("請說會或不會")
            while True:
                print_output("你想吃平價或是貴的呢")
                input_text = get_input()
                for i in range(len(input_text)):
                    word = input_text[i]
                    if word == "平" or word == "評" or word == "貴" or word == "都":
                        break
                if word == "平" or word == "評":
                    for element in choose_list[:]:
                        if element[5] != "平價":
                            choose_list.remove(element)
                    break
                elif word == "貴":
                    for element in choose_list[:]:
                        if element[5] != "奢華":
                            choose_list.remove(element)
                    break
                elif word == "都":
                    break
                else:
                    print_output("請說平價或奢華或都可以喔")
            while True:
                if word == "奢華":
                    print_output("看來是還沒月底阿")
                print_output("那你想吃近一點的或是都可以呢")
                input_text = get_input()
                for i in range(len(input_text)):
                    word = input_text[i]
                    if word == "近" or word == "都":
                        break
                if word == "近":
                    for element in choose_list[:]:
                        if element[6] != "近":
                            choose_list.remove(element)
                    break
                elif word == "都":
                    break
                else:
                    print_output("請說近一點或都可以")
                
            break
        elif word == "其他":
            for element in choose_list[:]:
                if element[1] == "正餐" or element[1] == "自助":
                    choose_list.remove(element)
            while True:
                print_output("那你想吃甜點或飲料或宵夜")
                input_text = get_input()
                for i in range(len(input_text)):
                    word = input_text[i]
                    if word == "甜" or word == "宵" or word == "飲"or word == "不" or word == "可":
                        break
                if word == "甜":
                    for element in choose_list[:]:
                        if element[1] != "蛋糕" and element[1] != "冰":
                            choose_list.remove(element)
                    while True:
                        print_output("你想吃蛋糕或冰呢")
                        input_text = get_input()
                        for i in range(len(input_text)):
                            word = input_text[i]
                            if word == "蛋" or word == "冰" or word == "可":
                                break
                        if word == "蛋":
                            for element in choose_list[:]:
                                if element[1] != "蛋糕":
                                    choose_list.remove(element)
                            break
                        elif word == "冰":
                            for element in choose_list[:]:
                                if element[1] != "冰":
                                    choose_list.remove(element)
                            break
                        elif word == "可":
                            break
                        else:
                            print_output("請說蛋糕或冰或都可以喔")
                    break
                elif word == "宵":
                    for element in choose_list[:]:
                        if element[1] != "宵夜" and element[1] != "速食" and element[1] != "都有":
                            choose_list.remove(element)
                    break
                elif word == "飲":
                    for element in choose_list[:]:
                        if element[1] != "飲料" :
                            choose_list.remove(element)
                    break
                elif word == "不":
                    print_output("欸認真一點")
                elif word == "可":
                    break
                else:
                    print_output("請說甜點或飲料或宵夜喔")
            while True:
                print_output("那你想吃近一點的或是都可以呢")
                input_text = get_input()
                for i in range(len(input_text)):
                    word = input_text[i]
                    if word == "近" or word == "都":
                        break
                if word == "近":
                    for element in choose_list[:]:
                        if element[6] != "近":
                            choose_list.remove(element)
                    break
                elif word == "都":
                    break
                else:
                    print_output("請說近一點或都可以")
                        
            break

        elif word == "都不":
            print_output("欸認真一點")
        else:
            print_output("請再說一遍")

    # 篩選結束
    if wheel == False:
        food_choice = []
        print_output("好開心喔")
        print_output("我已經把篩選完的餐廳放進轉盤裡了")
        while True:
            if len(choose_list) == 0:
                print_output("好難過好像沒有符合的餐廳")
                print_output("不然我推薦你我很喜歡的潛艇堡")
                break
            else:
                # result = random.randint(0, len(choose_list)-1)
                # output_text = "那我推薦你吃" + choose_list[result][0]
                
                # print_output(output_text)
                print_output("你想玩命運轉盤來決定自己要吃什麼嗎")
                input_text = get_input()
                for i in range(len(input_text)):
                    word = input_text[i]
                    if word == "想" or word == "好"or word == "不":
                        break
                if word == "想" or word == "好":
                    food_choice = topic_wheel(choose_list,food,add_choose)
                    return food_choice
                    # break
                elif word == "不":
                    print_output("可是不玩的話我會難過欸")
                else:
                    print_output("請說想或不想喔")
            
    else:
        if len(choose_list) == 0:
            print_output("好難過好像沒有符合的餐廳")
            print_output("不然我推薦你我很喜歡的潛艇堡")
        else:
            result = random.randint(0, len(choose_list)-1)
            output_text = "那我推薦你吃" + choose_list[result][0]
            print_output(output_text)
            return choose_list[result]
    
def topic_wheel(choose_list,food,add_choose):
    print_output("歡迎來到命運轉盤")
    # if food == True:
        # print_output("我們已經把篩選完的餐廳放進轉盤裡了")
        # print_output("想新增選項嗎")
        # while True:
        #     add_choose = False
        #     input_text = get_input()
        #     for i in range(len(input_text)):
        #         word = input_text[i]
        #         if word == "想" or word == "好"or word == "不":
        #             break
        #     if word == "想" or word == "好":
        #         add_choose = True
        #         break
        #     elif word == "不":
        #         add_choose = False
        #         break
        #     else:
        #         print_output("請說想或不想喔")

    if add_choose == True:
        print_output("那第一個要新增甚麼選項呢")
        print_output("想結束新增的話可以說離開喔")
        while add_choose == True:
            input_text = get_input()
            for i in range(len(input_text)):
                word = input_text[i]
                if word == "離":
                    break
            if word == "離":
                add_choose = False
                break
            else:
                a = []
                a.append(input_text)
                choose_list.append(a)
                reply_list = ['哇聽起來很棒呢', '喔喔這個有料欸', '唉呦這個不錯喔']
                print_output(reply_list[random.randint(0, len(reply_list) - 1)])
                print_output("那下一個新增甚麼選項呢")

    
    print_output("太好了轉盤設置已完成")    
    print_output("請將你的手放到感應器前")
    print_output("手離開後轉盤就會停止喔")
    while True:
        print_output("準備好了嗎")
        input_text = get_input()
        for i in range(len(input_text)):
            word = input_text[i]
            if word == "好":
                break
        if word == "好":
            print_output("太好了")
            break
        else:
            print_output("請將手靠近喔")


    # choose_list = [['喝水'],['上廁所'],['滑手機'],['睡覺']]
    # wheel start
    final = []
    i = 0
    while True:
        i = i + 1
        oled_2.display_text(choose_list[i%len(choose_list)][0])
        # time.sleep(ultrasonic.distance()*100)
        final = choose_list[i%len(choose_list)]
        print(ultrasonic.distance())
        if ultrasonic.distance() > 10:
            break
    # for i in range(random.randint(3,6)):
    #     i = i + 1
    #     oled_2.display_text(choose_list[i%len(choose_list)][0])
    #     time.sleep(0.2)
    #     final = choose_list[i%len(choose_list)]
    #     print(ultrasonic.distance())

    # for i in range(random.randint(1,4)):
    #     i = i + 1
    #     oled_2.display_text(choose_list[i%len(choose_list)][0])
    #     time.sleep(0.5)
    #     final = choose_list[i%len(choose_list)]
    #     print(ultrasonic.distance())
            

    # final = random.randint(0,len(choose_list)-1)
    output_text = "我覺得"+final[0]+"感覺比較棒"
    print_output(output_text)
    print_output("喜歡這個答案嗎")
    input_text = get_input()
    for i in range(len(input_text)):
        word = input_text[i]
        if word == "喜" or word == "是" or word == "否" or word == "不":
            break
    if word == "喜" or word == "是":
        print_output("太好了很開心能幫到你")
    elif word == "否" or word == "不":
        print_output("往自己不喜歡的反方向走也很棒呢")    
    # else:
    #     print_output("咩噗")


    if food == False:
        print_output("在煩惱之餘也要補充能量")
        print_output("讓我來幫你決定要吃什麼吧")
        final = topic_food(choose_list,food,add_choose, wheel)
        return final
    else:
        return final

# def height_to_num(input_text, chinese_list):
#     num = ""
#     for i in range(len(input_text)):
#         if input_text[i] == "點":
#             break
#         for j in range(10):
#             if input_text[i] == chinese_list[j]:
#                 num += str(j)
#                 break
#     if len(num)  == 2: # 一百五
#         num += "0"
#     if len(num) == 0: # default case
#         num += "1"
#     return int(num)

# def weight_to_num(input_text, chinese_list):
#     num = ""
#     for i in range(len(input_text)):
#         if input_text[i] == "點":
#             break
#         for j in range(10):
#             if input_text[i] == chinese_list[j]:
#                 num += str(j)
#                 break
#     if len(num) == 1: # 五十、六十
#         num += "0"
#     if len(num) == 0: # default case
#         num += "1"
#     return int(num)

def get_num(input_text):
    num_list = "0123456789."
    num = ""
    for i in range(len(input_text)):
        for j in range(len(num_list)):
            if input_text[i] == num_list[j]:
                num += input_text[i]
                break
    return int(num)


def bmi_cal():
    # chinese_list = "零一二三四五六七八九"
    print_output("請問你的身高是幾公分呢")
    input_text = get_input()
    # height = height_to_num(input_text, chinese_list)/100
    height = get_num(input_text)/100
    print_output("那請問你的體重是幾公斤呢")
    input_text = get_input()
    # weight = weight_to_num(input_text, chinese_list)
    weight = get_num(input_text)
    bmi = round(weight/pow(height, 2), 1)
    if bmi < 0 or bmi > 100:
        print_output("哎呀我的BMI計算機好像壞掉了")
        print_output("但還是要記得多運動喔")
    else:
        output_text = "你的BMI是" + str(bmi)
        print_output(output_text)
        if bmi < 18.5:
            print_output("嗚嗚有點過輕")
            print_output("要記得飲食均衡喔")
        elif bmi >= 18.5 and bmi < 24:
            print_output("太好了體重剛剛好")
            print_output("請繼續保持喔")
        elif bmi >= 24:
            print_output("嗚嗚有點過重")
            print_output("要記得多運動喔")


# main
if __name__ == "__main__":
    food = False
    wheel = False
    add_choose = False
    choose_list = []
    food_choice = []
    # while True:
    #     print(ultrasonic.distance())
    oled_2.display_text("我正在揮手")
    dcmotor.wave(500, 500)
    print_output("你好")
    print_output("我是一個可以幫你解決選擇障礙的機器人")
    print_output("你最近會有很煩惱的事嗎")
    print_output("或是三餐不知道要吃什麼嗎")
    input_text = get_input()
    for i in range(len(input_text)):
        word = input_text[i]
        if word == "吃" or word == "餐" or word == "其":
            break
    if word == "吃" or word == "餐":
        food = True
        food_choice = topic_food(choose_list,food,add_choose, wheel)
    else:
        print_output("聽起來真的很煩惱呢")
        print_output("你目前有哪些選擇在猶豫呢")
        input_text = get_input()
        print_output("聽起來都可以試試看欸")
        print_output("心中有特別喜歡的答案嗎")
        input_text = get_input()
        for i in range(len(input_text)):
            word = input_text[i]
            if word == "有" or word == "沒":
                break
        if word == "有":
            print_output("那可以照著自己的心走阿")
        elif word == "沒":
            print_output("原來如此")
            print_output("猶豫真的很令人苦惱")
        
        print_output("那不然我們來玩命運轉盤")
        print_output("可將選項放到命運轉盤中替你決定")
        while True:
            print_output("請問你想要使用嗎")
            # choose_list = [['喝水'],['上廁所'],['滑手機'],['睡覺']]
            input_text = get_input()
            for i in range(len(input_text)):
                word = input_text[i]
                if word == "不" or word == "好" or word == "想":
                    break
            if word == "好" or word == "想":
                wheel = True
                add_choose = True
                food_choice = topic_wheel(choose_list,food,add_choose)
                break
            else:
                print_output("可是不玩的話我會難過欸")


    output_text = "說到"+food_choice[0]
    print_output(output_text)
    
    #養生
    if food_choice[1] == "速食":
        print_output("你正餐常吃速食嗎")
        input_text = get_input()
        for i in range(len(input_text)):
            word = input_text[i]
            if word == "有" or word == "常" or word == "不" or word == "沒":
                break
        if word == "有" or word == "常":
            print_output("建議營養要均衡喔")
        else:
            print_output("偶爾一次沒有關係的")
    elif food_choice[1] == "自助": # 吃到飽
        print_output("你平常會常去吃吃到飽的餐廳嗎")
        input_text = get_input()
        for i in range(len(input_text)):
            word = input_text[i]
            if word == "有" or word == "常" or word == "不" or word == "沒":
                break
        if word == "有" or word == "常":
            print_output("常吃這麼大份量對身體是一種負擔喔")
        else:
            print_output("那這次可以稍微放縱一下")
    elif food_choice[1] == "宵夜":
        print_output("你平常有熬夜的習慣嗎")
        input_text = get_input()
        for i in range(len(input_text)):
            word = input_text[i]
            if word == "有" or word == "常" or word == "不" or word == "沒":
                break
        if word == "有" or word == "常":
            print_output("常熬夜對身體不好喔")
        else:
            print_output("希望你能一直保持良好的作息喔")
    elif food_choice[1] == "飲料":
        print_output("你時常喝飲料嗎")
        input_text = get_input()
        for i in range(len(input_text)):
            word = input_text[i]
            if word == "有" or word == "常" or word == "不" or word == "沒":
                break
        if word == "有" or word == "常":
            print_output("可以的話盡量多喝水喔")
        else:
            print_output("偶爾一杯解饞沒問題的")
    elif food_choice[1] == "冰":
        print_output("你時常吃冰嗎")
        input_text = get_input()
        for i in range(len(input_text)):
            word = input_text[i]
            if word == "有" or word == "常" or word == "不" or word == "沒":
                break
        if word == "有" or word == "常":
            print_output("最近天冷可以多吃熱食喔")
        else:
            print_output("很注意身體健康很棒喔")
    else:
        print_output("你覺得這間健康嗎")
        input_text = get_input()
        for i in range(len(input_text)):
            word = input_text[i]
            if word == "否" or word == "健" or word == "不" or word == "是" or word == "沒":
                break
        if word == "健" or word == "是":
            print_output("喔喔那我改天也去吃吃看")
        elif word == "否" or word == "不":
            print_output("那你還吃")
        else:
            print_output("ok努力更新食物資料庫")

    print_output("對了你有常運動嗎")
    input_text = get_input()
    for i in range(len(input_text)):
        word = input_text[i]
        if word == "沒" or word == "有" or word == "常":
            break
    if word == "有" or word == "常":
        print_output("那你都做甚麼運動呢")
        input_text = get_input()
        print_output("我也是")
        print_output("好開心跟你一樣")

    else:
        print_output("要多運動啦")
    print_output("我來幫你算算看BMI好了")
    bmi_cal() #cal bmi

    print_output("最近身體有哪裡不舒服嗎")
    input_text = get_input()
    for i in range(len(input_text)):
        word = input_text[i]
        if word == "沒" or word == "有" or word == "是" or word == "痛":
            break
    if word == "有" or word == "是" or word == "痛":
        print_output("會到很不舒服嗎")
        input_text = get_input()
        for i in range(len(input_text)):
            word = input_text[i]
            if word == "不" or word == "會" or word == "是":
                break
        if word == "會" or word == "是":
            print_output("那要去看醫生才行")
        else:
            print_output("那要多觀察喔")

    else:
        print_output("太棒了")
    print_output("最近天氣冷要多穿一點喔")
    print_output("今天很開心跟你聊天")
    print_output("掰掰!")
    dcmotor.wave(500, 500)
    