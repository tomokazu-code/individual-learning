from pyecharts.charts import Bar,Timeline
from pyecharts.options import *
from pyecharts.globals import *
f=open("D:/GDP数据.txt","r",encoding="GB2312")
date_line=f.readlines()

#把所有数据全部存放入字典中
date_dict={}



#遍历整个数据(1999,中国,132132131)
for i in date_line:
    year,country,GDP=int(i.split(",")[0]),i.split(",")[1],float(i.split(",")[2])
    #把所有数据放入字典，字典中可能没有相对应的年份，会报错
    try:
        date_dict[year].append([country,GDP])
    except:
        date_dict[year]=[]
        date_dict[year].append([country,GDP])

#创建时间线
#设置主题在时间线修改
timeline=Timeline({"theme":ThemeType.LIGHT})


#把年份排序，并且进行循环遍历
range_year_sort=sorted(date_dict.keys())
for year in range_year_sort:
    #把每一年所对应的数据取出来并且按照GDP排序，取出前八位
    date_dict[year].sort(key=lambda x:x[1])
    year_date=date_dict[year][0:8]

    #构建每一张柱状图的x，y轴
    x_date=[]
    y_date=[]

    #把数据放入x和y轴
    for country in year_date:
        x_date.append(country[0])
        y_date.append(country[1])


    #创建图表
    bar=Bar()
    bar.add_xaxis(x_date)
    bar.add_yaxis(y_date,label_opts=LabelOpts(position="right"))
    bar.reversal_axis()

    #设置标题

    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{year}年全球GDP排行")
    )

    #添加到时间线
    timeline.add(bar,str(year))


#设置播放格式
timeline.add_schema(
    play_interval=1000,   #循环每一张图的时间：1秒
    is_timeline_show=True,#显示时间
    is_auto_play=True,  #自动播放
    is_loop_play=True,    #循环播放


)


timeline.render()

