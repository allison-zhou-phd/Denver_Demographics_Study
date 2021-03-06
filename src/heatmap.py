import branca
import pandas as pd
import json
import math
import folium

block_group_geo = '../data/denver.json'

df = pd.read_pickle('../data/pickled_df_2014_2018')

colorscale = branca.colormap.linear.YlOrRd_09.scale(0, 240000)
colorscale = colorscale.to_step(index=[0, 60000, 120000, 180000, 240000])
colorscale.caption = 'Median Income (2014_2018)'
data_inc = df.set_index('STFID')['MED_HH_INCOME']

def style_function(feature):
    blk_grp = data_inc.get(int(feature['id']), None)
    #print(blk_grp)
    #print(type(blk_grp))
    return {
        'fillColor': '#gray' if blk_grp is None or math.isnan(blk_grp) else colorscale(blk_grp),
        'fillOpacity': 0.5,
        'weight': 0        
    }

m = folium.Map(
    location=[39.7392, -104.9903],
    zoom_start=11,
    tiles='openstreetmap'
)

folium.GeoJson(
    data = block_group_geo,
    style_function = style_function    
).add_to(m)

colorscale.add_to(m)
m