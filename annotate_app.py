"""Annotate image
"""
from os import listdir
from os.path import isfile, join

import geopandas as gpd
from fiona.crs import from_epsg


def load_farm_geom(farm_geom_path):
    toyohashi_df = gpd.read_file(farm_geom_path)
    toyohashi_df["geometry"] = toyohashi_df["geometry"].to_crs(epsg=4326)
    toyohashi_df.crs = from_epsg(4236)
    return toyohashi_df


shapefile_path = "23201豊橋市2016/23201豊橋市2016_5.shp"

geom_df = load_farm_geom(shapefile_path)
small_geom_df = geom_df.cx[137.325:137.35, 34.7:34.75]
print("Loaded shape file....")

images_dir = "../automate_web/scrape"

scraped = [f for f in listdir(images_dir) if isfile(join(images_dir, f))]

print("dataset points size: ", small_geom_df.shape[0])
precision = 12

scraped_rename = []
for image_name in scraped:
    long, lat = image_name.split("_")
    scraped_rename.append(f"{long[:precision]}_{lat[:precision]}.png")


for farm_geom in small_geom_df.geometry:
    coord = list(farm_geom.centroid.coords[0])
    image_name = f"{str(coord[1])[:precision]}_{str(coord[0])[:precision]}.png"
    if image_name in scraped_rename:
        index = scraped_rename.index(image_name)
        image_filename = join(images_dir, scraped[index])
        print("found: ", image_filename)

