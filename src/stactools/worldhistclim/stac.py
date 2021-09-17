from datetime import datetime
import os
from dateutil.relativedelta import relativedelta
from pystac.extensions.base import PropertiesExtension
import pytz
import json
import logging
import rasterio
from stactools.worldclim import constants
from stactools.worldhistclim.constants import (WORLDHISTCLIM_CRS, WORLDHISTCLIM_ID,
                                           WORLDHISTCLIM_EPSG, WORLDHISTCLIM_TITLE,
                                           DESCRIPTION, WORLDHISTCLIM_PROVIDER,
                                           LICENSE, LICENSE_LINK, INSTRUMENT)

import pystac
from pystac import (Collection, Asset, Extent, SpatialExtent, TemporalExtent,
                    CatalogType, MediaType)

from pystac.extensions.projection import (SummariesProjectionExtension,
                                          ProjectionExtension)
from pystac.extensions.scientific import ScientificExtension
from pystac.extensions.raster import RasterExtension, RasterBand
from pystac.extensions.file import FileExtension
from pystac.extensions.item_assets import AssetDefinition, ItemAssetsExtension
from pystac.extensions.label import (
    LabelClasses,
    LabelExtension,
    LabelTask,
    LabelType,
)
from pystac.item import Item
from pystac.summaries import Summaries
from shapely.geometry import Polygon

logger = logging.getLogger(__name__)

def create_collection() -> Collection:
    """Create a STAC Collection

    This function includes logic to extract all relevant metadata from
    an asset describing the STAC collection and/or metadata coded into an
    accompanying constants.py file.

    See `Collection<https://pystac.readthedocs.io/en/latest/api.html#collection>`_.

    Returns:
        Collection: STAC Collection object
    """
    providers = [
        Provider(
            name="The OS Community",
            roles=[
                ProviderRole.PRODUCER, ProviderRole.PROCESSOR,
                ProviderRole.HOST
            ],
            url="https://github.com/stac-utils/stactools",
        )
    ]

    # Time must be in UTC
    demo_time = datetime.now(tz=timezone.utc)

    extent = Extent(
        SpatialExtent([[-180., 90., 180., -90.]]),
        TemporalExtent([demo_time, None]),
    )

    collection = Collection(
        id="my-collection-id",
        title="A dummy STAC Collection",
        description="Used for demonstration purposes",
        license="CC-0",
        providers=providers,
        extent=extent,
        catalog_type=CatalogType.RELATIVE_PUBLISHED,
    )

    return collection


def create_item(asset_href: str) -> Item:
    """Create a STAC Item

    This function should include logic to extract all relevant metadata from an
    asset, metadata asset, and/or a constants.py file.

    See `Item<https://pystac.readthedocs.io/en/latest/api.html#item>`_.

    Args:
        asset_href (str): The HREF pointing to an asset associated with the item

    Returns:
        Item: STAC Item object
    """

    properties = {
        "title": "A dummy STAC Item",
        "description": "Used for demonstration purposes",
    }

    demo_geom = {
        "type":
        "Polygon",
        "coordinates": [[[-180, -90], [180, -90], [180, 90], [-180, 90],
                         [-180, -90]]],
    }

    # Time must be in UTC
    demo_time = datetime.now(tz=timezone.utc)

    item = Item(
        id="my-item-id",
        properties=properties,
        geometry=demo_geom,
        bbox=[-180, 90, 180, -90],
        datetime=demo_time,
        stac_extensions=[],
    )

    # It is a good idea to include proj attributes to optimize for libs like stac-vrt
    proj_attrs = ProjectionExtension.ext(item, add_if_missing=True)
    proj_attrs.epsg = 4326
    proj_attrs.bbox = [-180, 90, 180, -90]
    proj_attrs.shape = [1, 1]  # Raster shape
    proj_attrs.transform = [-180, 360, 0, 90, 0, 180]  # Raster GeoTransform

    # Add an asset to the item (COG for example)
    item.add_asset(
        "image",
        Asset(
            href=asset_href,
            media_type=MediaType.COG,
            roles=["data"],
            title="A dummy STAC Item COG",
        ),
    )

    return item
