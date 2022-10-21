from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts
map=Map()
data=[
    ("北京",99),
    ("江苏",199),
    ("广东",299),
    ("台湾",399),
    ("重庆",499),
    ("西藏",256),
    ("新疆",2),
    ("吉林",325)
]
map.add("测试地图",data,"china")

map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min":1,"max":9,"label":"1-9","colour":"#CCFFFF"},
            {"min":10,"max":99,"label":"10-99","colour":"#FFFF99"},
            {"min":100,"max":199,"label":"100-199","colour":"#FF9966"},
            {"min":200,"max":299,"label":"200-299","colour":"#FF6666"},
            {"min":300,"max":399,"label":"300-399","colour":"#CC3333"},
            {"min":400,"max":1000,"label":"400-1000","colour":"#990033"},
        ]
    )

)












map.render()