#----------------------------------------------------
# 1. Convert pandas dataframe into geopandas dataframe
#----------------------------------------------------
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

pd_df = pd.read_csv('./points.csv')
pd_df['geometry'] = pd_df.apply(lambda row: Point(row.lng, row.lat), axis=1)
gp_df = gpd.GeoDataFrame(pd_df)

#OR even better
pd_df = pd.read_csv('./points.csv')
gp_df = gpd.GeoDataFrame(pd_df, geometry=gpd.points_from_xy(pd_df.Longitude, pd_df.Latitude))
#----------------------------------------------------

#----------------------------------------------------
#2. Creates a geopandas dataframe
#----------------------------------------------------
gp_df = gp.read_file('./file_name.shp')
gp_df2 = gp.read_file('./file_name2.geojson')
#----------------------------------------------------

#----------------------------------------------------
#3. Saves as a file from a geopandas dataframe
# The try and catch is there to avoid the overwrite
# missing functionality in geopandas
#----------------------------------------------------
try: 
    os.remove('./file_name.geojson')
except OSError:
    pass
gp_df.to_file('./file_name.geojson', driver="GeoJSON")

try: 
    os.remove('./file_name.shp')
except OSError:
    pass
gp_df.to_file('./file_name.shp', driver="ESRI Shapefile")
#----------------------------------------------------

#----------------------------------------------------
#4. Creates a boundinng box dataframe of 4 columns:
#minx, miny, maxx, maxy
#----------------------------------------------------
bounds_df = gp_df['geometry'].bounds
#----------------------------------------------------

#----------------------------------------------------
#5. Creates a centroid longitude series
#----------------------------------------------------
centroid_ser_lng = gp_df['geometry'].centroid.x
#----------------------------------------------------

#----------------------------------------------------
#6. Creates a centroid latitude series
#----------------------------------------------------
centroid_ser_lat = gp_df['geometry'].centroid.y
#----------------------------------------------------

#----------------------------------------------------
#7. Concats the original dataframe with the bounding
#box and centroid columns
#----------------------------------------------------
new_df = pd.concat([gp_df, bounds_df,centroid_ser_lng,centroid_ser_lat], axis=1)
new_df.rename(columns={0: 'centroid_lng'}, inplace=True)
new_df.rename(columns={1: 'centroid_lat'}, inplace=True)
#----------------------------------------------------

#----------------------------------------------------
#8. Creates a boolean series where points and polyons
#intersect. Then concatenate result series with the points df
#----------------------------------------------------
polys_df = gpd.read_postgis(sql,con,geom_col='geometry')
points_df = gp.read_file('./points.geojson')

intersection_ser = points_df.intersects(polys_df.unary_union)
intersection_df = pd.concat([points_df,intersection_ser],axis=1)
#----------------------------------------------------



