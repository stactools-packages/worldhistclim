import stactools.core

from stactools.worldhistclim.stac import create_collection, create_item

__all__ = ['create_collection', 'create_item']

stactools.core.use_fsspec()


def register_plugin(registry):
    from stactools.worldhistclim import commands
    registry.register_subcommand(commands.create_worldhistclim_command)


__version__ = "0.1.0"
