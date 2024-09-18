from file__define import *
from data_define import *
from pyecharts.charts import *
from pyecharts.options import *
from pyecharts.globals import ThemeType
from pyecharts import options as opts
from pyecharts.charts import Calendar

textreder = TextFileReader("E:/2011年1月销售数据.txt")
jsonreder = JsonFileReader("E:/2011年2月销售数据JSON.txt")

jan_date:list[Recode] = textreder.read_data()
feb_date:list[Recode]= jsonreder.read_data()
all_date:list[Recode]=jan_date+feb_date
"""
#生成柱状图
all_date_dict={}
for recode_date in all_date:
    if recode_date.date in all_date_dict.keys():
        all_date_dict[recode_date.date]+=recode_date.money
    else:
        all_date_dict[recode_date.date]=recode_date.money


bar=Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))
bar.add_xaxis(list(all_date_dict.keys()))
bar.add_yaxis("销售额",list(all_date_dict.values()),label_opts=LabelOpts(is_show=False))
bar.set_global_opts(

    title_opts=TitleOpts(title="某公司的每日销售额",pos_left="center",pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True,min_=30000,max_=120000)
)

bar.render("每日销售额.html")

all_date_dict['2011-02-02']=44722
all_date_dict['2011-02-03']=47443
Date_List=[]
for i in all_date_dict:
    Date_List.append([i,int(all_date_dict[i])])
"""

#生成日历图
# c = (
#     Calendar()
#     .add(
#         "",
#         Date_List,
#         calendar_opts=opts.CalendarOpts(
#             range_="2011",
#             daylabel_opts=opts.CalendarDayLabelOpts(name_map="cn"),
#             monthlabel_opts=opts.CalendarMonthLabelOpts(name_map="cn"),
#         ),
#     )
#     .set_global_opts(
#         title_opts=opts.TitleOpts(title="某公司的每日销售额",pos_left="center"),
#
#         visualmap_opts=opts.VisualMapOpts(
#             max_=65000,
#             min_=31000,
#             orient="horizontal",
#             is_piecewise=True,
#             pos_top="230px",
#             pos_left="100px",
#         ),
#
#
#     )
#
#     .render("每日销售额.html")
# )
#

"""
#保存到数据库
from pymysql import Connection

conn=Connection(
    host='localhost',
    port=3306,
    user='root',
    password='********',
    autocommit=True
)
cursor=conn.cursor()
conn.select_db('py_sql')
for i in all_date:
    sql=f"insert into py_sql.orders values('{i.date}','{i.order_id}',{i.money},'{i.province}')"
    #执行sql
    cursor.execute(sql)


conn.close()
"""