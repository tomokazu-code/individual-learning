import tkinter as tk
from PIL import Image,ImageTk
from tkinter import filedialog
import json
import requests
import base64
import pandas as pd

# EasyDL之图片分类API接口实现-基于python tkinter实现
# 打开图片文件

def OpenFile():
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    canvas.delete(tk.ALL)
    default_color = root.cget("bg")
    canvas.configure(bg=default_color)
    global file_path
    file_path = filedialog.askopenfilename()
    image = Image.open(file_path)
    
    width, height = image.size
    aspect_ratio = width / height
    target_width, target_height = (canvas_width, canvas_height)
    target_aspect_ratio = target_width / target_height

    # 计算调整后图像的实际大小
    if target_aspect_ratio < aspect_ratio:
        # 以目标宽度为准进行调整
        new_width = target_width
        new_height = int(target_width / aspect_ratio)
    else:
        # 以目标高度为准进行调整
        new_width = int(target_height * aspect_ratio)
        new_height = target_height

    # 调整图像的大小并保存
    resized_image = image.resize((new_width, new_height))
    
    global image_file
    image_file= ImageTk.PhotoImage(resized_image)  #注：如果显示图片这个功能定义在一个方法里，image_file  一定要申明为全局变量，窗口才会显示图片
    image = canvas.create_image(0,0,anchor='nw',image=image_file)

# 提交检测
def Submit():
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    # 有关介绍可以参考：https://blog.csdn.net/cyh0503/article/details/83796694
    API_KEY = "YG4scxWrMkRNWeZdX2DBMr3B"
    SECRET_KEY = "eS2dQSdayBOZ1UZV5tkRz1UUGNGiaPiL"
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials' \
           "&client_id={}&client_secret={}".format(API_KEY, SECRET_KEY)

    response = requests.get(host)
    content = response.json()
    access_token = content["access_token"]
 
    image = open(file_path, 'rb').read()
    data = {'image': base64.b64encode(image).decode()}
 
    request_url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/segmentation/010503"+"?access_token=" + access_token
    response = requests.post(request_url, data=json.dumps(data))
    content = response.json()

    df = pd.DataFrame(content)
    results = df['results']
    print(results)

    score_0 = 0
    score_1 = 0
    score_2=0
    score_3=0
    score_4=0
    score_5=0
    score_6=0
    score_7=0
    score_8=0
    score_9=0
    score_10=0
    score_11=0
    score_12=0
    score_13=0
    score_14=0
    score_15=0
    score_16=0
    score_17=0
    score_18=0
    score_19=0
    score_20=0
    score_21=0
    score_22=0
    score_23=0
    score_24=0
    score_25=0
    score_26=0
    score_27=0
    score_28=0
    score_29=0
    score_30=0
    score_31=0
    score_32=0
    score_33=0


    if results[0]['name'] == labelstr1:
        score_0 = results[0]['score']
        score_1 = results[1]['score']
        score_2 = results[1]['score']
        score_3=results[1]['score']
        score_4=results[1]['score']
        score_5=results[1]['score']
        score_6=results[1]['score']
        score_7=results[1]['score']
        score_8=results[1]['score']
        score_9=results[1]['score']
        score_10=results[1]['score']
        score_11=results[1]['score']
        score_12=results[1]['score']
        score_13=results[1]['score']
        score_14=results[1]['score']
        score_15=results[1]['score']
        score_16=results[1]['score']
        score_17=results[1]['score']
        score_18=results[1]['score']
        score_19=results[1]['score']
        score_20=results[1]['score']
        score_21=results[1]['score']
        score_22=results[1]['score']
        score_23=results[1]['score']
        score_24=results[1]['score']
        score_25=results[1]['score']
        score_26=results[1]['score']
        score_27=results[1]['score']
        score_28=results[1]['score']
        score_29=results[1]['score']
        score_30=results[1]['score']
        score_31=results[1]['score']
        score_32=results[1]['score']
        score_33=results[1]['score']

    elif results[0]['name']== labelstr2:
        score_0 = results[1]['score']
        score_1 = results[0]['score']
        score_2=results[1]['score']
        score_3=results[1]['score']
        score_4=results[1]['score']
        score_5=results[1]['score']
        score_6=results[1]['score']
        score_7=results[1]['score']
        score_8=results[1]['score']
        score_9=results[1]['score']
        score_10=results[1]['score']
        score_11=results[1]['score']
        score_12=results[1]['score']
        score_13=results[1]['score']
        score_14=results[1]['score']
        score_15=results[1]['score']
        score_16=results[1]['score']
        score_17=results[1]['score']
        score_18=results[1]['score']
        score_19=results[1]['score']
        score_20=results[1]['score']
        score_21=results[1]['score']
        score_22=results[1]['score']
        score_23=results[1]['score']
        score_24=results[1]['score']
        score_25=results[1]['score']
        score_26=results[1]['score']
        score_27=results[1]['score']
        score_28=results[1]['score']
        score_29=results[1]['score']
        score_30=results[1]['score']
        score_31=results[1]['score']
        score_32=results[1]['score']
        score_33=results[1]['score']

    elif results[0]['name']== labelstr3:
        score_0 = results[1]['score']
        score_1 = results[1]['score']
        score_2=results[0]['score']
        score_3=results[1]['score']
        score_4=results[1]['score']
        score_5=results[1]['score']
        score_6=results[1]['score']
        score_7=results[1]['score']
        score_8=results[1]['score']
        score_9=results[1]['score']
        score_10=results[1]['score']
        score_11=results[1]['score']
        score_12=results[1]['score']
        score_13=results[1]['score']
        score_14=results[1]['score']
        score_15=results[1]['score']
        score_16=results[1]['score']
        score_17=results[1]['score']
        score_18=results[1]['score']
        score_19=results[1]['score']
        score_20=results[1]['score']
        score_21=results[1]['score']
        score_22=results[1]['score']
        score_23=results[1]['score']
        score_24=results[1]['score']
        score_25=results[1]['score']
        score_26=results[1]['score']
        score_27=results[1]['score']
        score_28=results[1]['score']
        score_29=results[1]['score']
        score_30=results[1]['score']
        score_31=results[1]['score']
        score_32=results[1]['score']
        score_33=results[1]['score']

    elif results[0]['name']== labelstr4:
        score_0 = results[1]['score']
        score_1 = results[1]['score']
        score_2=results[1]['score']
        score_3=results[0]['score']
        score_4=results[1]['score']
        score_5=results[1]['score']
        score_6=results[1]['score']
        score_7=results[1]['score']
        score_8=results[1]['score']
        score_9=results[1]['score']
        score_10=results[1]['score']
        score_11=results[1]['score']
        score_12=results[1]['score']
        score_13=results[1]['score']
        score_14=results[1]['score']
        score_15=results[1]['score']
        score_16=results[1]['score']
        score_17=results[1]['score']
        score_18=results[1]['score']
        score_19=results[1]['score']
        score_20=results[1]['score']
        score_21=results[1]['score']
        score_22=results[1]['score']
        score_23=results[1]['score']
        score_24=results[1]['score']
        score_25=results[1]['score']
        score_26=results[1]['score']
        score_27=results[1]['score']
        score_28=results[1]['score']
        score_29=results[1]['score']
        score_30=results[1]['score']
        score_31=results[1]['score']
        score_32=results[1]['score']
        score_33=results[1]['score']

    elif results[0]['name']== labelstr5:
        score_0 = results[1]['score']
        score_1 = results[1]['score']
        score_2=results[1]['score']
        score_3=results[1]['score']
        score_4=results[0]['score']
        score_5=results[1]['score']
        score_6=results[1]['score']
        score_7=results[1]['score']
        score_8=results[1]['score']
        score_9=results[1]['score']
        score_10=results[1]['score']
        score_11=results[1]['score']
        score_12=results[1]['score']
        score_13=results[1]['score']
        score_14=results[1]['score']
        score_15=results[1]['score']
        score_16=results[1]['score']
        score_17=results[1]['score']
        score_18=results[1]['score']
        score_19=results[1]['score']
        score_20=results[1]['score']
        score_21=results[1]['score']
        score_22=results[1]['score']
        score_23=results[1]['score']
        score_24=results[1]['score']
        score_25=results[1]['score']
        score_26=results[1]['score']
        score_27=results[1]['score']
        score_28=results[1]['score']
        score_29=results[1]['score']
        score_30=results[1]['score']
        score_31=results[1]['score']
        score_32=results[1]['score']
        score_33=results[1]['score']

    elif results[0]['name']== labelstr6:
        score_0 = results[1]['score']
        score_1 = results[1]['score']
        score_2=results[1]['score']
        score_3=results[1]['score']
        score_4=results[1]['score']
        score_5=results[0]['score']
        score_6=results[1]['score']
        score_7=results[1]['score']
        score_8=results[1]['score']
        score_9=results[1]['score']
        score_10=results[1]['score']
        score_11=results[1]['score']
        score_12=results[1]['score']
        score_13=results[1]['score']
        score_14=results[1]['score']
        score_15=results[1]['score']
        score_16=results[1]['score']
        score_17=results[1]['score']
        score_18=results[1]['score']
        score_19=results[1]['score']
        score_20=results[1]['score']
        score_21=results[1]['score']
        score_22=results[1]['score']
        score_23=results[1]['score']
        score_24=results[1]['score']
        score_25=results[1]['score']
        score_26=results[1]['score']
        score_27=results[1]['score']
        score_28=results[1]['score']
        score_29=results[1]['score']
        score_30=results[1]['score']
        score_31=results[1]['score']
        score_32=results[1]['score']
        score_33=results[1]['score']
    elif results[0]['name']== labelstr7:
        score_0 = results[1]['score']
        score_1 = results[1]['score']
        score_2=results[1]['score']
        score_3=results[1]['score']
        score_4=results[1]['score']
        score_5=results[1]['score']
        score_6=results[0]['score']
        score_7=results[1]['score']
        score_8=results[1]['score']
        score_9=results[1]['score']
        score_10=results[1]['score']
        score_11=results[1]['score']
        score_12=results[1]['score']
        score_13=results[1]['score']
        score_14=results[1]['score']
        score_15=results[1]['score']
        score_16=results[1]['score']
        score_17=results[1]['score']
        score_18=results[1]['score']
        score_19=results[1]['score']
        score_20=results[1]['score']
        score_21=results[1]['score']
        score_22=results[1]['score']
        score_23=results[1]['score']
        score_24=results[1]['score']
        score_25=results[1]['score']
        score_26=results[1]['score']
        score_27=results[1]['score']
        score_28=results[1]['score']
        score_29=results[1]['score']
        score_30=results[1]['score']
        score_31=results[1]['score']
        score_32=results[1]['score']
        score_33=results[1]['score']

    elif results[0]['name']== labelstr8:
        score_0 = results[1]['score']
        score_1 = results[1]['score']
        score_2=results[1]['score']
        score_3=results[1]['score']
        score_4=results[1]['score']
        score_5=results[1]['score']
        score_6=results[1]['score']
        score_7=results[0]['score']
        score_8=results[1]['score']
        score_9=results[1]['score']
        score_10=results[1]['score']
        score_11=results[1]['score']
        score_12=results[1]['score']
        score_13=results[1]['score']
        score_14=results[1]['score']
        score_15=results[1]['score']
        score_16=results[1]['score']
        score_17=results[1]['score']
        score_18=results[1]['score']
        score_19=results[1]['score']
        score_20=results[1]['score']
        score_21=results[1]['score']
        score_22=results[1]['score']
        score_23=results[1]['score']
        score_24=results[1]['score']
        score_25=results[1]['score']
        score_26=results[1]['score']
        score_27=results[1]['score']
        score_28=results[1]['score']
        score_29=results[1]['score']
        score_30=results[1]['score']
        score_31=results[1]['score']
        score_32=results[1]['score']
        score_33=results[1]['score']

    elif results[0]['name']== labelstr9:
        score_0 = results[1]['score']
        score_1 = results[1]['score']
        score_2=results[1]['score']
        score_3=results[1]['score']
        score_4=results[1]['score']
        score_5=results[1]['score']
        score_6=results[1]['score']
        score_7=results[1]['score']
        score_8=results[0]['score']
        score_9=results[1]['score']
        score_10=results[1]['score']
        score_11=results[1]['score']
        score_12=results[1]['score']
        score_13=results[1]['score']
        score_14=results[1]['score']
        score_15=results[1]['score']
        score_16=results[1]['score']
        score_17=results[1]['score']
        score_18=results[1]['score']
        score_19=results[1]['score']
        score_20=results[1]['score']
        score_21=results[1]['score']
        score_22=results[1]['score']
        score_23=results[1]['score']
        score_24=results[1]['score']
        score_25=results[1]['score']
        score_26=results[1]['score']
        score_27=results[1]['score']
        score_28=results[1]['score']
        score_29=results[1]['score']
        score_30=results[1]['score']
        score_31=results[1]['score']
        score_32=results[1]['score']
        score_33=results[1]['score']

    elif results[0]['name']== labelstr10:
        score_0 = results[1]['score']
        score_1 = results[1]['score']
        score_2=results[1]['score']
        score_3=results[1]['score']
        score_4=results[1]['score']
        score_5=results[1]['score']
        score_6=results[1]['score']
        score_7=results[1]['score']
        score_8=results[1]['score']
        score_9=results[0]['score']
        score_10=results[1]['score']
        score_11=results[1]['score']
        score_12=results[1]['score']
        score_13=results[1]['score']
        score_14=results[1]['score']
        score_15=results[1]['score']
        score_16=results[1]['score']
        score_17=results[1]['score']
        score_18=results[1]['score']
        score_19=results[1]['score']
        score_20=results[1]['score']
        score_21=results[1]['score']
        score_22=results[1]['score']
        score_23=results[1]['score']
        score_24=results[1]['score']
        score_25=results[1]['score']
        score_26=results[1]['score']
        score_27=results[1]['score']
        score_28=results[1]['score']
        score_29=results[1]['score']
        score_30=results[1]['score']
        score_31=results[1]['score']
        score_32=results[1]['score']
        score_33=results[1]['score']

    elif results[0]['name']== labelstr11:
        score_0 = results[1]['score']
        score_1 = results[1]['score']
        score_2=results[1]['score']
        score_3=results[1]['score']
        score_4=results[1]['score']
        score_5=results[1]['score']
        score_6=results[1]['score']
        score_7=results[1]['score']
        score_8=results[1]['score']
        score_9=results[1]['score']
        score_10=results[0]['score']
        score_11=results[1]['score']
        score_12=results[1]['score']
        score_13=results[1]['score']
        score_14=results[1]['score']
        score_15=results[1]['score']
        score_16=results[1]['score']
        score_17=results[1]['score']
        score_18=results[1]['score']
        score_19=results[1]['score']
        score_20=results[1]['score']
        score_21=results[1]['score']
        score_22=results[1]['score']
        score_23=results[1]['score']
        score_24=results[1]['score']
        score_25=results[1]['score']
        score_26=results[1]['score']
        score_27=results[1]['score']
        score_28=results[1]['score']
        score_29=results[1]['score']
        score_30=results[1]['score']
        score_31=results[1]['score']
        score_32=results[1]['score']
        score_33=results[1]['score']

    elif results[0]['name']== labelstr12:
        score_0 = results[1]['score']
        score_1 = results[1]['score']
        score_2=results[1]['score']
        score_3=results[1]['score']
        score_4=results[1]['score']
        score_5=results[1]['score']
        score_6=results[1]['score']
        score_7=results[1]['score']
        score_8=results[1]['score']
        score_9=results[1]['score']
        score_10=results[1]['score']
        score_11=results[0]['score']
        score_12=results[1]['score']
        score_13=results[1]['score']
        score_14=results[1]['score']
        score_15=results[1]['score']
        score_16=results[1]['score']
        score_17=results[1]['score']
        score_18=results[1]['score']
        score_19=results[1]['score']
        score_20=results[1]['score']
        score_21=results[1]['score']
        score_22=results[1]['score']
        score_23=results[1]['score']
        score_24=results[1]['score']
        score_25=results[1]['score']
        score_26=results[1]['score']
        score_27=results[1]['score']
        score_28=results[1]['score']
        score_29=results[1]['score']
        score_30=results[1]['score']
        score_31=results[1]['score']
        score_32=results[1]['score']
        score_33=results[1]['score']

    elif results[0]['name']== labelstr13:
        score_0 = results[1]['score']
        score_1 = results[1]['score']
        score_2=results[1]['score']
        score_3=results[1]['score']
        score_4=results[1]['score']
        score_5=results[1]['score']
        score_6=results[1]['score']
        score_7=results[1]['score']
        score_8=results[1]['score']
        score_9=results[1]['score']
        score_10=results[1]['score']
        score_11=results[1]['score']
        score_12=results[0]['score']
        score_13=results[1]['score']
        score_14=results[1]['score']
        score_15=results[1]['score']
        score_16=results[1]['score']
        score_17=results[1]['score']
        score_18=results[1]['score']
        score_19=results[1]['score']
        score_20=results[1]['score']
        score_21=results[1]['score']
        score_22=results[1]['score']
        score_23=results[1]['score']
        score_24=results[1]['score']
        score_25=results[1]['score']
        score_26=results[1]['score']
        score_27=results[1]['score']
        score_28=results[1]['score']
        score_29=results[1]['score']
        score_30=results[1]['score']
        score_31=results[1]['score']
        score_32=results[1]['score']
        score_33=results[1]['score']

    elif results[0]['name']== labelstr14:
        score_0 = results[1]['score']
        score_1 = results[1]['score']
        score_2=results[1]['score']
        score_3=results[1]['score']
        score_4=results[1]['score']
        score_5=results[1]['score']
        score_6=results[1]['score']
        score_7=results[1]['score']
        score_8=results[1]['score']
        score_9=results[1]['score']
        score_10=results[1]['score']
        score_11=results[1]['score']
        score_12=results[1]['score']
        score_13=results[0]['score']
        score_14=results[1]['score']
        score_15=results[1]['score']
        score_16=results[1]['score']
        score_17=results[1]['score']
        score_18=results[1]['score']
        score_19=results[1]['score']
        score_20=results[1]['score']
        score_21=results[1]['score']
        score_22=results[1]['score']
        score_23=results[1]['score']
        score_24=results[1]['score']
        score_25=results[1]['score']
        score_26=results[1]['score']
        score_27=results[1]['score']
        score_28=results[1]['score']
        score_29=results[1]['score']
        score_30=results[1]['score']
        score_31=results[1]['score']
        score_32=results[1]['score']
        score_33=results[1]['score']
    elif results[0]['name']== labelstr15:
        score_0 = results[1]['score']
        score_1 = results[1]['score']
        score_2=results[1]['score']
        score_3=results[1]['score']
        score_4=results[1]['score']
        score_5=results[1]['score']
        score_6=results[1]['score']
        score_7=results[1]['score']
        score_8=results[1]['score']
        score_9=results[1]['score']
        score_10=results[1]['score']
        score_11=results[1]['score']
        score_12=results[1]['score']
        score_13=results[1]['score']
        score_14=results[0]['score']
        score_15=results[1]['score']
        score_16=results[1]['score']
        score_17=results[1]['score']
        score_18=results[1]['score']
        score_19=results[1]['score']
        score_20=results[1]['score']
        score_21=results[1]['score']
        score_22=results[1]['score']
        score_23=results[1]['score']
        score_24=results[1]['score']
        score_25=results[1]['score']
        score_26=results[1]['score']
        score_27=results[1]['score']
        score_28=results[1]['score']
        score_29=results[1]['score']
        score_30=results[1]['score']
        score_31=results[1]['score']
        score_32=results[1]['score']
        score_33=results[1]['score']
    elif results[0]['name']== labelstr16:
        score_0 = results[1]['score']
        score_1 = results[1]['score']
        score_2=results[1]['score']
        score_3=results[1]['score']
        score_4=results[1]['score']
        score_5=results[1]['score']
        score_6=results[1]['score']
        score_7=results[1]['score']
        score_8=results[1]['score']
        score_9=results[1]['score']
        score_10=results[1]['score']
        score_11=results[1]['score']
        score_12=results[1]['score']
        score_13=results[1]['score']
        score_14=results[1]['score']
        score_15=results[0]['score']
        score_16=results[1]['score']
        score_17=results[1]['score']
        score_18=results[1]['score']
        score_19=results[1]['score']
        score_20=results[1]['score']
        score_21=results[1]['score']
        score_22=results[1]['score']
        score_23=results[1]['score']
        score_24=results[1]['score']
        score_25=results[1]['score']
        score_26=results[1]['score']
        score_27=results[1]['score']
        score_28=results[1]['score']
        score_29=results[1]['score']
        score_30=results[1]['score']
        score_31=results[1]['score']
        score_32=results[1]['score']
        score_33=results[1]['score']
    elif results[0]['name']== labelstr17:
        score_0 = results[1]['score']
        score_1 = results[1]['score']
        score_2=results[1]['score']
        score_3=results[1]['score']
        score_4=results[1]['score']
        score_5=results[1]['score']
        score_6=results[1]['score']
        score_7=results[1]['score']
        score_8=results[1]['score']
        score_9=results[1]['score']
        score_10=results[1]['score']
        score_11=results[1]['score']
        score_12=results[1]['score']
        score_13=results[1]['score']
        score_14=results[1]['score']
        score_15=results[1]['score']
        score_16=results[0]['score']
        score_17=results[1]['score']
        score_18=results[1]['score']
        score_19=results[1]['score']
        score_20=results[1]['score']
        score_21=results[1]['score']
        score_22=results[1]['score']
        score_23=results[1]['score']
        score_24=results[1]['score']
        score_25=results[1]['score']
        score_26=results[1]['score']
        score_27=results[1]['score']
        score_28=results[1]['score']
        score_29=results[1]['score']
        score_30=results[1]['score']
        score_31=results[1]['score']
        score_32=results[1]['score']
        score_33=results[1]['score']

    elif results[0]['name']== labelstr18:
        score_0 = results[1]['score']
        score_1 = results[1]['score']
        score_2=results[1]['score']
        score_3=results[1]['score']
        score_4=results[1]['score']
        score_5=results[1]['score']
        score_6=results[1]['score']
        score_7=results[1]['score']
        score_8=results[1]['score']
        score_9=results[1]['score']
        score_10=results[1]['score']
        score_11=results[1]['score']
        score_12=results[1]['score']
        score_13=results[1]['score']
        score_14=results[1]['score']
        score_15=results[1]['score']
        score_16=results[1]['score']
        score_17=results[0]['score']
        score_18=results[1]['score']
        score_19=results[1]['score']
        score_20=results[1]['score']
        score_21=results[1]['score']
        score_22=results[1]['score']
        score_23=results[1]['score']
        score_24=results[1]['score']
        score_25=results[1]['score']
        score_26=results[1]['score']
        score_27=results[1]['score']
        score_28=results[1]['score']
        score_29=results[1]['score']
        score_30=results[1]['score']
        score_31=results[1]['score']
        score_32=results[1]['score']
        score_33=results[1]['score']

    elif results[0]['name']== labelstr19:
        score_0 = results[1]['score']
        score_1 = results[1]['score']
        score_2=results[1]['score']
        score_3=results[1]['score']
        score_4=results[1]['score']
        score_5=results[1]['score']
        score_6=results[1]['score']
        score_7=results[1]['score']
        score_8=results[1]['score']
        score_9=results[1]['score']
        score_10=results[1]['score']
        score_11=results[1]['score']
        score_12=results[1]['score']
        score_13=results[1]['score']
        score_14=results[1]['score']
        score_15=results[1]['score']
        score_16=results[1]['score']
        score_17=results[1]['score']
        score_18=results[0]['score']
        score_19=results[1]['score']
        score_20=results[1]['score']
        score_21=results[1]['score']
        score_22=results[1]['score']
        score_23=results[1]['score']
        score_24=results[1]['score']
        score_25=results[1]['score']
        score_26=results[1]['score']
        score_27=results[1]['score']
        score_28=results[1]['score']
        score_29=results[1]['score']
        score_30=results[1]['score']
        score_31=results[1]['score']
        score_32=results[1]['score']
        score_33=results[1]['score']

    elif results[0]['name']== labelstr20:
        score_0 = results[1]['score']
        score_1 = results[1]['score']
        score_2=results[1]['score']
        score_3=results[1]['score']
        score_4=results[1]['score']
        score_5=results[1]['score']
        score_6=results[1]['score']
        score_7=results[1]['score']
        score_8=results[1]['score']
        score_9=results[1]['score']
        score_10=results[1]['score']
        score_11=results[1]['score']
        score_12=results[1]['score']
        score_13=results[1]['score']
        score_14=results[1]['score']
        score_15=results[1]['score']
        score_16=results[1]['score']
        score_17=results[1]['score']
        score_18=results[1]['score']
        score_19=results[0]['score']
        score_20=results[1]['score']
        score_21=results[1]['score']
        score_22=results[1]['score']
        score_23=results[1]['score']
        score_24=results[1]['score']
        score_25=results[1]['score']
        score_26=results[1]['score']
        score_27=results[1]['score']
        score_28=results[1]['score']
        score_29=results[1]['score']
        score_30=results[1]['score']
        score_31=results[1]['score']
        score_32=results[1]['score']
        score_33=results[1]['score']

    elif results[0]['name']== labelstr21:
        score_0 = results[1]['score']
        score_1 = results[1]['score']
        score_2=results[1]['score']
        score_3=results[1]['score']
        score_4=results[1]['score']
        score_5=results[1]['score']
        score_6=results[1]['score']
        score_7=results[1]['score']
        score_8=results[1]['score']
        score_9=results[1]['score']
        score_10=results[1]['score']
        score_11=results[1]['score']
        score_12=results[1]['score']
        score_13=results[1]['score']
        score_14=results[1]['score']
        score_15=results[1]['score']
        score_16=results[1]['score']
        score_17=results[1]['score']
        score_18=results[1]['score']
        score_19=results[1]['score']
        score_20=results[0]['score']
        score_21=results[1]['score']
        score_22=results[1]['score']
        score_23=results[1]['score']
        score_24=results[1]['score']
        score_25=results[1]['score']
        score_26=results[1]['score']
        score_27=results[1]['score']
        score_28=results[1]['score']
        score_29=results[1]['score']
        score_30=results[1]['score']
        score_31=results[1]['score']
        score_32=results[1]['score']
        score_33=results[1]['score']

    elif results[0]['name']== labelstr22:
        score_0 = results[1]['score']
        score_1 = results[1]['score']
        score_2=results[1]['score']
        score_3=results[1]['score']
        score_4=results[1]['score']
        score_5=results[1]['score']
        score_6=results[1]['score']
        score_7=results[1]['score']
        score_8=results[1]['score']
        score_9=results[1]['score']
        score_10=results[1]['score']
        score_11=results[1]['score']
        score_12=results[1]['score']
        score_13=results[1]['score']
        score_14=results[1]['score']
        score_15=results[1]['score']
        score_16=results[1]['score']
        score_17=results[1]['score']
        score_18=results[1]['score']
        score_19=results[1]['score']
        score_20=results[1]['score']
        score_21=results[0]['score']
        score_22=results[1]['score']
        score_23=results[1]['score']
        score_24=results[1]['score']
        score_25=results[1]['score']
        score_26=results[1]['score']
        score_27=results[1]['score']
        score_28=results[1]['score']
        score_29=results[1]['score']
        score_30=results[1]['score']
        score_31=results[1]['score']
        score_32=results[1]['score']
        score_33=results[1]['score']

    elif results[0]['name']== labelstr23:
        score_0 = results[1]['score']
        score_1 = results[1]['score']
        score_2=results[1]['score']
        score_3=results[1]['score']
        score_4=results[1]['score']
        score_5=results[1]['score']
        score_6=results[1]['score']
        score_7=results[1]['score']
        score_8=results[1]['score']
        score_9=results[1]['score']
        score_10=results[1]['score']
        score_11=results[1]['score']
        score_12=results[1]['score']
        score_13=results[1]['score']
        score_14=results[1]['score']
        score_15=results[1]['score']
        score_16=results[1]['score']
        score_17=results[1]['score']
        score_18=results[1]['score']
        score_19=results[1]['score']
        score_20=results[1]['score']
        score_21=results[1]['score']
        score_22=results[0]['score']
        score_23=results[1]['score']
        score_24=results[1]['score']
        score_25=results[1]['score']
        score_26=results[1]['score']
        score_27=results[1]['score']
        score_28=results[1]['score']
        score_29=results[1]['score']
        score_30=results[1]['score']
        score_31=results[1]['score']
        score_32=results[1]['score']
        score_33=results[1]['score']

    elif results[0]['name']== labelstr24:
        score_0 = results[1]['score']
        score_1 = results[1]['score']
        score_2=results[1]['score']
        score_3=results[1]['score']
        score_4=results[1]['score']
        score_5=results[1]['score']
        score_6=results[1]['score']
        score_7=results[1]['score']
        score_8=results[1]['score']
        score_9=results[1]['score']
        score_10=results[1]['score']
        score_11=results[1]['score']
        score_12=results[1]['score']
        score_13=results[1]['score']
        score_14=results[1]['score']
        score_15=results[1]['score']
        score_16=results[1]['score']
        score_17=results[1]['score']
        score_18=results[1]['score']
        score_19=results[1]['score']
        score_20=results[1]['score']
        score_21=results[1]['score']
        score_22=results[1]['score']
        score_23=results[0]['score']
        score_24=results[1]['score']
        score_25=results[1]['score']
        score_26=results[1]['score']
        score_27=results[1]['score']
        score_28=results[1]['score']
        score_29=results[1]['score']
        score_30=results[1]['score']
        score_31=results[1]['score']
        score_32=results[1]['score']
        score_33=results[1]['score']

    elif results[0]['name']== labelstr25:
        score_0 = results[1]['score']
        score_1 = results[1]['score']
        score_2=results[1]['score']
        score_3=results[1]['score']
        score_4=results[1]['score']
        score_5=results[1]['score']
        score_6=results[1]['score']
        score_7=results[1]['score']
        score_8=results[1]['score']
        score_9=results[1]['score']
        score_10=results[1]['score']
        score_11=results[1]['score']
        score_12=results[1]['score']
        score_13=results[1]['score']
        score_14=results[1]['score']
        score_15=results[1]['score']
        score_16=results[1]['score']
        score_17=results[1]['score']
        score_18=results[1]['score']
        score_19=results[1]['score']
        score_20=results[1]['score']
        score_21=results[1]['score']
        score_22=results[1]['score']
        score_23=results[1]['score']
        score_24=results[0]['score']
        score_25=results[1]['score']
        score_26=results[1]['score']
        score_27=results[1]['score']
        score_28=results[1]['score']
        score_29=results[1]['score']
        score_30=results[1]['score']
        score_31=results[1]['score']
        score_32=results[1]['score']
        score_33=results[1]['score']

    elif results[0]['name']== labelstr26:
        score_0 = results[1]['score']
        score_1 = results[1]['score']
        score_2=results[1]['score']
        score_3=results[1]['score']
        score_4=results[1]['score']
        score_5=results[1]['score']
        score_6=results[1]['score']
        score_7=results[1]['score']
        score_8=results[1]['score']
        score_9=results[1]['score']
        score_10=results[1]['score']
        score_11=results[1]['score']
        score_12=results[1]['score']
        score_13=results[1]['score']
        score_14=results[1]['score']
        score_15=results[1]['score']
        score_16=results[1]['score']
        score_17=results[1]['score']
        score_18=results[1]['score']
        score_19=results[1]['score']
        score_20=results[1]['score']
        score_21=results[1]['score']
        score_22=results[1]['score']
        score_23=results[1]['score']
        score_24=results[1]['score']
        score_25=results[0]['score']
        score_26=results[1]['score']
        score_27=results[1]['score']
        score_28=results[1]['score']
        score_29=results[1]['score']
        score_30=results[1]['score']
        score_31=results[1]['score']
        score_32=results[1]['score']
        score_33=results[1]['score']

    elif results[0]['name']== labelstr27:
        score_0 = results[1]['score']
        score_1 = results[1]['score']
        score_2=results[1]['score']
        score_3=results[1]['score']
        score_4=results[1]['score']
        score_5=results[1]['score']
        score_6=results[1]['score']
        score_7=results[1]['score']
        score_8=results[1]['score']
        score_9=results[1]['score']
        score_10=results[1]['score']
        score_11=results[1]['score']
        score_12=results[1]['score']
        score_13=results[1]['score']
        score_14=results[1]['score']
        score_15=results[1]['score']
        score_16=results[1]['score']
        score_17=results[1]['score']
        score_18=results[1]['score']
        score_19=results[1]['score']
        score_20=results[1]['score']
        score_21=results[1]['score']
        score_22=results[1]['score']
        score_23=results[1]['score']
        score_24=results[1]['score']
        score_25=results[1]['score']
        score_26=results[0]['score']
        score_27=results[1]['score']
        score_28=results[1]['score']
        score_29=results[1]['score']
        score_30=results[1]['score']
        score_31=results[1]['score']
        score_32=results[1]['score']
        score_33=results[1]['score']

    elif results[0]['name']== labelstr28:
        score_0 = results[1]['score']
        score_1 = results[1]['score']
        score_2=results[1]['score']
        score_3=results[1]['score']
        score_4=results[1]['score']
        score_5=results[1]['score']
        score_6=results[1]['score']
        score_7=results[1]['score']
        score_8=results[1]['score']
        score_9=results[1]['score']
        score_10=results[1]['score']
        score_11=results[1]['score']
        score_12=results[1]['score']
        score_13=results[1]['score']
        score_14=results[1]['score']
        score_15=results[1]['score']
        score_16=results[1]['score']
        score_17=results[1]['score']
        score_18=results[1]['score']
        score_19=results[1]['score']
        score_20=results[1]['score']
        score_21=results[1]['score']
        score_22=results[1]['score']
        score_23=results[1]['score']
        score_24=results[1]['score']
        score_25=results[1]['score']
        score_26=results[1]['score']
        score_27=results[0]['score']
        score_28=results[1]['score']
        score_29=results[1]['score']
        score_30=results[1]['score']
        score_31=results[1]['score']
        score_32=results[1]['score']
        score_33=results[1]['score']

    elif results[0]['name']== labelstr29:
        score_0 = results[1]['score']
        score_1 = results[1]['score']
        score_2=results[1]['score']
        score_3=results[1]['score']
        score_4=results[1]['score']
        score_5=results[1]['score']
        score_6=results[1]['score']
        score_7=results[1]['score']
        score_8=results[1]['score']
        score_9=results[1]['score']
        score_10=results[1]['score']
        score_11=results[1]['score']
        score_12=results[1]['score']
        score_13=results[1]['score']
        score_14=results[1]['score']
        score_15=results[1]['score']
        score_16=results[1]['score']
        score_17=results[1]['score']
        score_18=results[1]['score']
        score_19=results[1]['score']
        score_20=results[1]['score']
        score_21=results[1]['score']
        score_22=results[1]['score']
        score_23=results[1]['score']
        score_24=results[1]['score']
        score_25=results[1]['score']
        score_26=results[1]['score']
        score_27=results[1]['score']
        score_28=results[0]['score']
        score_29=results[1]['score']
        score_30=results[1]['score']
        score_31=results[1]['score']
        score_32=results[1]['score']
        score_33=results[1]['score']

    elif results[0]['name']== labelstr30:
        score_0 = results[1]['score']
        score_1 = results[1]['score']
        score_2=results[1]['score']
        score_3=results[1]['score']
        score_4=results[1]['score']
        score_5=results[1]['score']
        score_6=results[1]['score']
        score_7=results[1]['score']
        score_8=results[1]['score']
        score_9=results[1]['score']
        score_10=results[1]['score']
        score_11=results[1]['score']
        score_12=results[1]['score']
        score_13=results[1]['score']
        score_14=results[1]['score']
        score_15=results[1]['score']
        score_16=results[1]['score']
        score_17=results[1]['score']
        score_18=results[1]['score']
        score_19=results[1]['score']
        score_20=results[1]['score']
        score_21=results[1]['score']
        score_22=results[1]['score']
        score_23=results[1]['score']
        score_24=results[1]['score']
        score_25=results[1]['score']
        score_26=results[1]['score']
        score_27=results[1]['score']
        score_28=results[1]['score']
        score_29=results[0]['score']
        score_30=results[1]['score']
        score_31=results[1]['score']
        score_32=results[1]['score']
        score_33=results[1]['score']

    elif results[0]['name']== labelstr31:
        score_0 = results[1]['score']
        score_1 = results[1]['score']
        score_2=results[1]['score']
        score_3=results[1]['score']
        score_4=results[1]['score']
        score_5=results[1]['score']
        score_6=results[1]['score']
        score_7=results[1]['score']
        score_8=results[1]['score']
        score_9=results[1]['score']
        score_10=results[1]['score']
        score_11=results[1]['score']
        score_12=results[1]['score']
        score_13=results[1]['score']
        score_14=results[1]['score']
        score_15=results[1]['score']
        score_16=results[1]['score']
        score_17=results[1]['score']
        score_18=results[1]['score']
        score_19=results[1]['score']
        score_20=results[1]['score']
        score_21=results[1]['score']
        score_22=results[1]['score']
        score_23=results[1]['score']
        score_24=results[1]['score']
        score_25=results[1]['score']
        score_26=results[1]['score']
        score_27=results[1]['score']
        score_28=results[1]['score']
        score_29=results[1]['score']
        score_30=results[0]['score']
        score_31=results[1]['score']
        score_32=results[1]['score']
        score_33=results[1]['score']

    elif results[0]['name']== labelstr32:
        score_0 = results[1]['score']
        score_1 = results[1]['score']
        score_2=results[1]['score']
        score_3=results[1]['score']
        score_4=results[1]['score']
        score_5=results[1]['score']
        score_6=results[1]['score']
        score_7=results[1]['score']
        score_8=results[1]['score']
        score_9=results[1]['score']
        score_10=results[1]['score']
        score_11=results[1]['score']
        score_12=results[1]['score']
        score_13=results[1]['score']
        score_14=results[1]['score']
        score_15=results[1]['score']
        score_16=results[1]['score']
        score_17=results[1]['score']
        score_18=results[1]['score']
        score_19=results[1]['score']
        score_20=results[1]['score']
        score_21=results[1]['score']
        score_22=results[1]['score']
        score_23=results[1]['score']
        score_24=results[1]['score']
        score_25=results[1]['score']
        score_26=results[1]['score']
        score_27=results[1]['score']
        score_28=results[1]['score']
        score_29=results[1]['score']
        score_30=results[1]['score']
        score_31=results[0]['score']
        score_32=results[1]['score']
        score_33=results[1]['score']

    elif results[0]['name']== labelstr33:
        score_0 = results[1]['score']
        score_1 = results[1]['score']
        score_2=results[1]['score']
        score_3=results[1]['score']
        score_4=results[1]['score']
        score_5=results[1]['score']
        score_6=results[1]['score']
        score_7=results[1]['score']
        score_8=results[1]['score']
        score_9=results[1]['score']
        score_10=results[1]['score']
        score_11=results[1]['score']
        score_12=results[1]['score']
        score_13=results[1]['score']
        score_14=results[1]['score']
        score_15=results[1]['score']
        score_16=results[1]['score']
        score_17=results[1]['score']
        score_18=results[1]['score']
        score_19=results[1]['score']
        score_20=results[1]['score']
        score_21=results[1]['score']
        score_22=results[1]['score']
        score_23=results[1]['score']
        score_24=results[1]['score']
        score_25=results[1]['score']
        score_26=results[1]['score']
        score_27=results[1]['score']
        score_28=results[1]['score']
        score_29=results[1]['score']
        score_30=results[1]['score']
        score_31=results[1]['score']
        score_32=results[0]['score']
        score_33=results[1]['score']

    elif results[0]['name']== labelstr34:
        score_0 = results[1]['score']
        score_1 = results[1]['score']
        score_2=results[1]['score']
        score_3=results[1]['score']
        score_4=results[1]['score']
        score_5=results[1]['score']
        score_6=results[1]['score']
        score_7=results[1]['score']
        score_8=results[1]['score']
        score_9=results[1]['score']
        score_10=results[1]['score']
        score_11=results[1]['score']
        score_12=results[1]['score']
        score_13=results[1]['score']
        score_14=results[1]['score']
        score_15=results[1]['score']
        score_16=results[1]['score']
        score_17=results[1]['score']
        score_18=results[1]['score']
        score_19=results[1]['score']
        score_20=results[1]['score']
        score_21=results[1]['score']
        score_22=results[1]['score']
        score_23=results[1]['score']
        score_24=results[1]['score']
        score_25=results[1]['score']
        score_26=results[1]['score']
        score_27=results[1]['score']
        score_28=results[1]['score']
        score_29=results[1]['score']
        score_30=results[1]['score']
        score_31=results[1]['score']
        score_32=results[1]['score']
        score_33=results[0]['score']



        
    res_1= '{:.2f}'.format(score_0 * 100)+"%"
    res_2= '{:.2f}'.format(score_1 * 100)+"%"
    res_3= '{:.2f}'.format(score_2 * 100)+"%"
    res_4= '{:.2f}'.format(score_3 * 100)+"%"
    res_5= '{:.2f}'.format(score_4 * 100)+"%"
    res_6= '{:.2f}'.format(score_5 * 100)+"%"
    res_7= '{:.2f}'.format(score_6 * 100)+"%"
    res_8= '{:.2f}'.format(score_7 * 100)+"%"
    res_9= '{:.2f}'.format(score_8 * 100)+"%"
    res_10= '{:.2f}'.format(score_9 * 100)+"%"
    res_11= '{:.2f}'.format(score_10 * 100)+"%"
    res_12= '{:.2f}'.format(score_11 * 100)+"%"
    res_13= '{:.2f}'.format(score_12 * 100)+"%"
    res_14= '{:.2f}'.format(score_13 * 100)+"%"
    res_15= '{:.2f}'.format(score_14 * 100)+"%"
    res_16= '{:.2f}'.format(score_15 * 100)+"%"
    res_17= '{:.2f}'.format(score_16 * 100)+"%"
    res_18= '{:.2f}'.format(score_17 * 100)+"%"
    res_19= '{:.2f}'.format(score_18 * 100)+"%"
    res_20= '{:.2f}'.format(score_19 * 100)+"%"
    res_21= '{:.2f}'.format(score_20 * 100)+"%"
    res_22= '{:.2f}'.format(score_21 * 100)+"%"
    res_23= '{:.2f}'.format(score_22 * 100)+"%"
    res_24= '{:.2f}'.format(score_23 * 100)+"%"
    res_25= '{:.2f}'.format(score_24 * 100)+"%"
    res_26= '{:.2f}'.format(score_25 * 100)+"%"
    res_27= '{:.2f}'.format(score_26 * 100)+"%"
    res_28= '{:.2f}'.format(score_27 * 100)+"%"
    res_29= '{:.2f}'.format(score_28 * 100)+"%"
    res_30= '{:.2f}'.format(score_29 * 100)+"%"
    res_31= '{:.2f}'.format(score_30 * 100)+"%"
    res_32= '{:.2f}'.format(score_31 * 100)+"%"
    res_33= '{:.2f}'.format(score_32 * 100)+"%"
    res_34= '{:.2f}'.format(score_33 * 100)+"%"

    label5.config(text=res_1)
    label7.config(text=res_2)
    label9.config(text=res_3)
    label11.config(text=res_4)
    label13.config(text=res_5)
    label15.config(text=res_6)
    label17.config(text=res_7)
    label19.config(text=res_8)
    label21.config(text=res_9)
    label23.config(text=res_10)
    label25.config(text=res_11)
    label27.config(text=res_12)
    label29.config(text=res_13)
    label31.config(text=res_14)
    label33.config(text=res_15)
    label35.config(text=res_16)
    label37.config(text=res_17)
    label39.config(text=res_18)
    label41.config(text=res_19)
    label43.config(text=res_20)
    label45.config(text=res_21)
    label47.config(text=res_22)
    label49.config(text=res_23)
    label51.config(text=res_24)
    label53.config(text=res_25)
    label55.config(text=res_26)
    label57.config(text=res_27)
    label59.config(text=res_28)
    label61.config(text=res_29)
    label63.config(text=res_30)
    label65.config(text=res_31)
    label67.config(text=res_32)
    label69.config(text=res_33)
    label71.config(text=res_34)


# 创建窗口
# tkinter介绍可参考：https://c.biancheng.net/tkinter/what-is-gui.html    
root = tk.Tk()
root.title("静态物体分类")
root.geometry("800x600")

# 创建画布用于图片显示
canvas_height=400
canvas_width=600
canvas = tk.Canvas(root, bg='#CCE8CF', height=canvas_height,width=canvas_width)
canvas.grid(row=0,column =0,columnspan = 2)

# 创建按钮并排列
button1 = tk.Button(root, text="打开图片文件",command=OpenFile)
button1.grid(row=1, column=0)

button2 = tk.Button(root, text="提交检测",command=Submit)
button2.grid(row=1, column=1)


# 创建标签用于显示结果
label1 = tk.Label(root, text="识别结果：")
label1.grid(row=2, column=0)


label2 = tk.Label(root, text="名称")
label2.grid(row=3, column=0)

label3 = tk.Label(root, text="置信度")
label3.grid(row=3, column=1)

labelstr1 = "白萝卜"
labelstr2 = "辣椒"
labelstr3="韭菜"
labelstr4="黑芝麻"
labelstr5="黑豆"
labelstr6="黑米"
labelstr7="红豆"
labelstr8="青椒"
labelstr9="花椒"
labelstr10="莲子"
labelstr11="荷兰豆"
labelstr12="豌豆"
labelstr13="大豆黄豆"
labelstr14="薏米"
labelstr15="黄瓜"
labelstr16="藜麦"
labelstr17="山药"
labelstr18="糙米"
labelstr19="大麦"
labelstr20="高粱米"
labelstr21="红薯"
labelstr22="奇亚籽"
labelstr23="杏仁"
labelstr24="荞麦"
labelstr25="小米"
labelstr26="芋头"
labelstr27="紫米"
labelstr28="玉米糁子"
labelstr29="玉米"
labelstr30="土豆"
labelstr31="葱"
labelstr32="白菜"
labelstr33="巴旦木"
labelstr34="大米"



label4 = tk.Label(root, text=labelstr1)
label4.grid(row=4, column=0)

label5 = tk.Label(root, text="0%")
label5.grid(row=4, column=1)

label6 = tk.Label(root, text=labelstr2)
label6.grid(row=5, column=0)

label7 = tk.Label(root, text="0%")
label7.grid(row=5, column=1)

label8 = tk.Label(root, text=labelstr3)
label8.grid(row=6, column=0)

label9 = tk.Label(root, text="0%")
label9.grid(row=6, column=1)

label10 = tk.Label(root, text=labelstr4)
label10.grid(row=7, column=0)

label11 = tk.Label(root, text="0%")
label11.grid(row=7, column=1)

label12 = tk.Label(root, text=labelstr5)
label12.grid(row=8, column=0)

label13 = tk.Label(root, text="0%")
label13.grid(row=8, column=1)

label14 = tk.Label(root, text=labelstr6)
label14.grid(row=9, column=0)

label15 = tk.Label(root, text="0%")
label15.grid(row=9, column=1)


label16 = tk.Label(root, text=labelstr7)
label16.grid(row=10, column=0)
label17 = tk.Label(root, text="0%")
label17.grid(row=10, column=1)

label18 = tk.Label(root, text=labelstr8)
label18.grid(row=11, column=0)
label19 = tk.Label(root, text="0%")
label19.grid(row=11, column=1)

label20 = tk.Label(root, text=labelstr9)
label20.grid(row=12, column=0)
label21 = tk.Label(root, text="0%")
label21.grid(row=12, column=1)

label22 = tk.Label(root, text=labelstr10)
label22.grid(row=13, column=0)
label23 = tk.Label(root, text="0%")
label23.grid(row=13, column=1)

label24 = tk.Label(root, text=labelstr11)
label24.grid(row=14, column=0)
label25 = tk.Label(root, text="0%")
label25.grid(row=14, column=1)

label26 = tk.Label(root, text=labelstr12)
label26.grid(row=15, column=0)
label27 = tk.Label(root, text="0%")
label27.grid(row=15, column=1)

label28 = tk.Label(root, text=labelstr13)
label28.grid(row=16, column=0)
label29 = tk.Label(root, text="0%")
label29.grid(row=16, column=1)

label30 = tk.Label(root, text=labelstr14)
label30.grid(row=17, column=0)
label31 = tk.Label(root, text="0%")
label31.grid(row=17, column=1)

label32 = tk.Label(root, text=labelstr15)
label32.grid(row=18, column=0)
label33 = tk.Label(root, text="0%")
label33.grid(row=18, column=1)

label34 = tk.Label(root, text=labelstr16)
label34.grid(row=19, column=0)
label35 = tk.Label(root, text="0%")
label35.grid(row=19, column=1)

label36 = tk.Label(root, text=labelstr17)
label36.grid(row=20, column=0)
label37 = tk.Label(root, text="0%")
label37.grid(row=20, column=1)

label38 = tk.Label(root, text=labelstr18)
label38.grid(row=21, column=0)
label39 = tk.Label(root, text="0%")
label39.grid(row=21, column=1)

label40 = tk.Label(root, text=labelstr19)
label40.grid(row=22, column=0)
label41 = tk.Label(root, text="0%")
label41.grid(row=22, column=1)

label42 = tk.Label(root, text=labelstr20)
label42.grid(row=23, column=0)
label43 = tk.Label(root, text="0%")
label43.grid(row=23, column=1)

label44 = tk.Label(root, text=labelstr21)
label44.grid(row=24, column=0)
label45 = tk.Label(root, text="0%")
label45.grid(row=24, column=1)

label46 = tk.Label(root, text=labelstr22)
label46.grid(row=25, column=0)
label47 = tk.Label(root, text="0%")
label47.grid(row=25, column=1)

label48 = tk.Label(root, text=labelstr23)
label48.grid(row=26, column=0)
label49 = tk.Label(root, text="0%")
label49.grid(row=26, column=1)

label50 = tk.Label(root, text=labelstr24)
label50.grid(row=27, column=0)
label51 = tk.Label(root, text="0%")
label51.grid(row=27, column=1)

label52 = tk.Label(root, text=labelstr25)
label52.grid(row=28, column=0)
label53 = tk.Label(root, text="0%")
label53.grid(row=28, column=1)

label54 = tk.Label(root, text=labelstr26)
label54.grid(row=29, column=0)
label55 = tk.Label(root, text="0%")
label55.grid(row=29, column=1)

label56 = tk.Label(root, text=labelstr27)
label56.grid(row=30, column=0)
label57 = tk.Label(root, text="0%")
label57.grid(row=30, column=1)

label58 = tk.Label(root, text=labelstr28)
label58.grid(row=31, column=0)
label59 = tk.Label(root, text="0%")
label59.grid(row=31, column=1)

label60 = tk.Label(root, text=labelstr29)
label60.grid(row=32, column=0)
label61 = tk.Label(root, text="0%")
label61.grid(row=32, column=1)

label62 = tk.Label(root, text=labelstr30)
label62.grid(row=33, column=0)
label63 = tk.Label(root, text="0%")
label63.grid(row=33, column=1)

label64 = tk.Label(root, text=labelstr31)
label64.grid(row=34, column=0)
label65= tk.Label(root, text="0%")
label65.grid(row=34, column=1)

label66 = tk.Label(root, text=labelstr32)
label66.grid(row=35, column=0)
label67 = tk.Label(root, text="0%")
label67.grid(row=35, column=1)

label68 = tk.Label(root, text=labelstr33)
label68.grid(row=36, column=0)
label69 = tk.Label(root, text="0%")
label69.grid(row=36, column=1)

label70 = tk.Label(root, text=labelstr34)
label70.grid(row=37, column=0)
label71 = tk.Label(root, text="0%")
label71.grid(row=37, column=1)


# 运行窗口
root.mainloop()