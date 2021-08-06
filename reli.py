import webbrowser

import folium
import pandas as pd
from folium import plugins

df = pd.read_excel("新.xlsx")
df.dropna(inplace=True)

full = df.dropna()

m = folium.Map(location=[31.1623, 121.4154], zoom_start=10, zoom_control='False', control_scale=True)

folium.TileLayer("http://rt1.map.gtimg.com/realtimerender?z={z}&x={x}&y={y}&type=vector&style=0", tms=True,
                 attr="Tencent").add_to(m)

marker_cluster = folium.plugins.MarkerCluster().add_to(m)

# mark points
for name, row in full.iterrows():
    folium.Marker([row["纬度"], row["经度"]], popup="{0}:{1}".format(row["停车场名称"], 1)).add_to(marker_cluster)

# headMap
# lnglats = df.dropna()[["纬度", "经度"]].values.tolist()
# headMap = folium.plugins.HeatMap(lnglats).add_to(m)

# 为地图对象添加点击显示经纬度的子功能
m.add_child(folium.LatLngPopup())

m.save("上海停车场.html")
webbrowser.open('上海停车场.html')
