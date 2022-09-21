from rio_tiler.io import COGReader
import matplotlib.pyplot as plt
import json
import httpx
from folium import Map, TileLayer
from rasterio import crs

hrrr_url = "s3://hrrrzarr/sfc/20210101/20210101_00z_anl.zarr/surface/TMP/surface/"
with COGReader(hrrr_url) as image:
    print(image.dataset)  # rasterio opened dataset
    img = image.read()

# plt.imshow(img.data[0,:,:])

#titiler_endpoint = "https://titiler.xyz"  # Developmentseed Demo endpoint. Please be kind.
titiler_endpoint = "http://127.0.0.1:8000"
oil_url = "https://opendata.digitalglobe.com/events/mauritius-oil-spill/post-event/2020-08-12/105001001F1B5B00/105001001F1B5B00.tif"
hrrr_url = "s3://hrrrzarr/sfc/20210101/20210101_00z_anl.zarr/surface/TMP/surface/TMP"

# Fetch File Metadata to get min/max rescaling values (because the file is stored as float32)
oil_r = httpx.get(
    f"{titiler_endpoint}/cog/info",
    params = {
        "url": oil_url,
    }
).json()

oil_bounds = oil_r["bounds"]
print(oil_r)

# Fetch File Metadata to get min/max rescaling values (because the file is stored as float32)
hrrr_r = httpx.get(
    f"{titiler_endpoint}/cog/info",
    params = {
        "url": hrrr_url,
    }
).json()


print(hrrr_r)
hrrr_bounds = hrrr_r["bounds"]