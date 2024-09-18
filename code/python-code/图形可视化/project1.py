import pyecharts
line=pyecharts.charts.Line()
# x=["中国",'美国','英国']
# y=[30,20,10,]
line.add_xaxis(["中国",'美国','法国'])
line.add_yaxis("金牌",[20,19,12])

line.set_global_opts(
    #图标标题
    title_opts=pyecharts.options.TitleOpts(title="金牌排行榜",pos_left="center",pos_bottom="1%"),
    #图例
    legend_opts=pyecharts.options.LegendOpts(is_show=True),
    #工具箱
    toolbox_opts=pyecharts.options.ToolboxOpts(is_show=True),
    #视觉映射
    visualmap_opts=pyecharts.options.VisualMapOpts(is_show=True)
)
line.render()
