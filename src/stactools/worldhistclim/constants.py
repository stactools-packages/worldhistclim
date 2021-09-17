# input information from the abstract here

from pyproj import CRS
from pystac import Provider
from pystac import Link

WORLDHISTCLIM_ID = "world-hist-clim"
WORLDHISTCLIM_EPSG = 4326  # to find  from a tiff file: gdalinfo file_path
WORLDHISTCLIM_CRS = CRS.from_epsg(WORLDHISTCLIM_EPSG)
WORLDHISTCLIM_TITLE = "Historical climate data"
LICENSE = "CC-BY-SA-4.0"
LICENSE_LINK = Link(
    rel="license",
    target="https://creativecommons.org/licenses/by-sa/4.0/",
    title=
    "Creative Commons - Attribution-ShareAlike 4.0 International - CC BY-SA 4.0"
)

DESCRIPTION = "This is WorldClim version 2.1 climate data for 1970-2000. This version was released in January 2020. There are monthly climate data for minimum, mean, and maximum temperature, precipitation, solar radiation, wind speed, water vapor pressure, and for total precipitation. There are also 19 “bioclimatic” variables. The data is available at the four spatial resolutions, between 30 seconds (~1 km2) to 10 minutes (~340 km2). Each download is a “zip” file containing 12 GeoTiff (.tif) files, one for each month of the year (January is 1; December is 12)."
# more metadata
INSTRUMENT = " Weather station data from between 9000 and 60 000 weather stations were interpolated using thin-plate splines with covariates including elevation, distance to the coast and three satellite-derived covariates: maximum and minimum land surface temperature as well as cloud cover, obtained with the MODIS satellite platform"

WORLDHISTCLIM_PROVIDER = Provider(
    name="WorldClim",
    roles=["processor", "host"],
    url="https://worldclim.org/data/worldclim21.html")

WORLDCLIM_FTP_tmin = [
    "https://biogeo.ucdavis.edu/data/worldclim/v2.1/base/wc2.1_10m_tmin.zip",
    "https://biogeo.ucdavis.edu/data/worldclim/v2.1/base/wc2.1_5m_tmin.zip",
    "https://biogeo.ucdavis.edu/data/worldclim/v2.1/base/wc2.1_2.5m_tmin.zip",
    "https://biogeo.ucdavis.edu/data/worldclim/v2.1/base/wc2.1_30s_tmin.zip"
]  # list of all links

COORDINATE_SYSTEM = {
    "wkt":
    ('GEOGCRS[\"WGS 84\",DATUM[\"World Geodetic System 1984\",ELLIPSOID[\"WGS 84\",6378137,298.257223563,LENGTHUNIT["metre",1]]],PRIMEM[\"Greenwich\",0,ANGLEUNIT[\"degree\",0.0174532925199433]],CS[\"ellipsoidal\",2],AXIS[\"geodetic latitude (Lat)\",north,ORDER[1],ANGLEUNIT[\"degree\",0.0174532925199433]],AXIS[\"geodetic longitude (Lon)\",east,ORDER[2],ANGLEUNIT[\"degree\",0.0174532925199433]],ID[\"EPSG\",4326]]'
     )
}
