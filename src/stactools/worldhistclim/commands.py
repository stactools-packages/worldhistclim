import logging

import click

from stactools.worldhistclim import stac

logger = logging.getLogger(__name__)


def create_worldhistclim_command(cli):
    """Creates the stactools-worldhistclim command line utility."""
    @cli.group(
        "worldhistclim",
        short_help=("Commands for working with stactools-worldhistclim"),
    )
    def worldhistclim():
        pass

    @worldhistclim.command(
        "create-collection",
        short_help="Creates a STAC collection",
    )
    @click.argument("destination")
    def create_collection_command(destination: str):
        """Creates a STAC Collection

        Args:
            destination (str): An HREF for the Collection JSON
        """
        collection = stac.create_collection()

        collection.set_self_href(destination)

        collection.save_object()

        return None

    @worldhistclim.command("create-item", short_help="Create a STAC item")
    @click.argument("source")
    @click.argument("destination")
    def create_item_command(source: str, destination: str):
        """Creates a STAC Item

        Args:
            source (str): HREF of the Asset associated with the Item
            destination (str): An HREF for the STAC Collection
        """
        item = stac.create_item(source)

        item.save_object(dest_href=destination)

        return None

    return worldhistclim
