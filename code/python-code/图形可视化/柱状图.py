import pyecharts
bar=pyecharts.charts.Bar()

bar.add_xaxis(["中国",'美国','法国'])
bar.add_yaxis("GDP",[20,19,12],label_opts=pyecharts.options.LabelOpts(position="right"))


#翻转xy
bar.reversal_axis()


bar.render("GDP.html")