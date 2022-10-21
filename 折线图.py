import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LabelOpts



fus=open("D:/美国.txt","r",encoding="UTF-8")
us_data=fus.read()

fja=open("D:/日本.txt","r",encoding="UTF-8")
ja_data=fja.read()

fin=open("D:/印度.txt","r",encoding="UTF-8")
in_data=fin.read()

us_data=us_data.replace("jsonp_1629344292311_69436(","")
us_data=us_data[:-2]

ja_data=ja_data.replace("jsonp_1629350871167_29498(","")
ja_data=ja_data[:-2]

in_data=in_data.replace("jsonp_1629350745930_63180(","")
in_data=in_data[:-2]

us_dict=json.loads(us_data)
ja_dict=json.loads(ja_data)
in_dict=json.loads(in_data)

us_trend_data=us_dict["data"][0]["trend"]
ja_trend_data=ja_dict["data"][0]["trend"]
in_trend_data=in_dict["data"][0]["trend"]

us_xdata=us_trend_data["updateDate"][:314]
ja_xdata=ja_trend_data["updateDate"][:314]
in_xdata=in_trend_data["updateDate"][:314]

us_ydata=us_trend_data["list"][0]["data"][:314]
ja_ydata=ja_trend_data["list"][0]["data"][:314]
in_ydata=in_trend_data["list"][0]["data"][:314]

line=Line()
line.set_global_opts(title_opts=TitleOpts(title="2020年三国确诊人数对比",pos_left="center",pos_bottom="1%"))


line.add_xaxis(us_xdata)
line.add_yaxis("美国确诊人数",us_ydata,label_opts=LabelOpts(is_show=False))
line.add_yaxis("日本确诊人数",ja_ydata,label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度确诊人数",in_ydata,label_opts=LabelOpts(is_show=False))

line.render()

fus.close()
fin.close()
fja.close()