import json
from pyecharts.charts import Map
from pyecharts.options import TitleOpts,VisualMapOpts
f=open("D:/疫情.txt","r",encoding="UTF-8")
data=f.read()
f.close()
data_dict=json.loads(data)
city_data=data_dict["areaTree"][0]["children"][1]["children"]
total_city_data=[]
for city in city_data:
    city_name=city["name"]+"市"
    city_num=city["total"]["confirm"]
    total_city_data.append((city_name,city_num))

map=Map()
map.add("江苏省疫情图",total_city_data,"江苏")
map.set_global_opts(title_opts=TitleOpts(title="江苏省疫情图"),
         visualmap_opts=VisualMapOpts(
             is_show=True,
             is_piecewise=True,
             pieces=[{"min":0,"max":9,"label":"1-9人","colour":"#FFEFD5"},
                    {"min":10,"max":19,"label":"10-19人","colour":"#7FFFD4"},
                    {"min":20,"max":39,"label":"20-39人","colour":"#EEE8AA"},
                    {"min":40,"max":59,"label":"40-59人","colour":"#BA55D3"},
                    {"min":60,"max":79,"label":"60-79人","colour":"#EE7942"},
                    {"min":80,"max":99,"label":"80-99人","colour":"#CD5555"},
                    {"min":100,"label":">100人","colour":"#8B3A3A"},
                    ]
         )
                    )





map.render()
