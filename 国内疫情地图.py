import json
from pyecharts.charts import Map
from pyecharts.options import TitleOpts
from pyecharts.options import VisualMapOpts
f=open("D:/疫情.txt","r",encoding="UTF-8")
data=f.read()
f.close()
data_dict=json.loads(data)
data_list=data_dict["areaTree"][0]["children"]

total_data=[]
for province in data_list:
    province_name=province['name']
    province_confirm=province['total']['confirm']
    total_data.append((province_name,province_confirm))

map=Map()
map.add("各省份确诊人数",total_data,"china")
map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
pieces=[
            {"min":1,"max":9,"label":"1-9","colour":"#CCFFFF"},
            {"min":10,"max":199,"label":"10-199","colour":"#FFFF99"},
            {"min":200,"max":399,"label":"200-399","colour":"#FF9966"},
            {"min":400,"max":599,"label":"400-599","colour":"#FF6666"},
            {"min":600,"max":799,"label":"600-799","colour":"#CC3333"},
            {"min":800,"max":1199,"label":"800-1199","colour":"#990033"},
            {"min":1200,"label":">1200","colour":"#990033"},
        ]
    )
)


map.render()
