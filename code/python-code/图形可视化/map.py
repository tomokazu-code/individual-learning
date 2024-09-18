import pyecharts
map=pyecharts.charts.Map()
date=[
    ("郑州市",99),
    ("新乡市",123),
    ("开封市",14),
]
map.add("地图",date,"河南")
map.set_global_opts(
    visualmap_opts=pyecharts.options.VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min":1,"max":49,"label":"1-49","color":"#CCFFFF"},
            {"min":50,"max":99,"label":"50-99","color":"#FF1111"},
            {"min":100,"max":149,"label":"100-149","color":"#00FF00"}

        ]


    )
)


map.render()

