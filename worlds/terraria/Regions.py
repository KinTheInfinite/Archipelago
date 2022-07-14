import typing

from BaseClasses import MultiWorld, Region, Entrance, ItemClassification
from .Items import TerrariaItem
from .Locations import TerrariaLocation, location_table, base_location_table, \
            life_crystal_location_table, mana_crystal_location_table
from .Names import LocationName, ItemName

def create_regions(world, player: int):

    locations: typing.List[str] = []

    # Add required locations.
    locations += [location for location in base_location_table]

    # Add life crystal locations
    if world.progressive_life[player]:
        locations += [location for location in life_crystal_location_table]
            
    # Add mana crystal locations
    if world.progressive_mana[player]:
        locations += [location for location in mana_crystal_location_table]

    # Set up the regions correctly.
    world.regions += [
        create_region(world, player, "Menu", None, [LocationName.TERRARIA_MENU]),
        create_region(world, player, "Terraria World", locations),
    ]
    
    world.get_entrance(LocationName.TERRARIA_MENU, player).connect(world.get_region("Terraria World", player))
    world.get_location(LocationName.TERRARIA_MENU, player).place_locked_item(TerrariaItem("No Item", ItemClassification.progression, None, player))
    world.get_location(LocationName.WOF_DEFEATED, player).place_locked_item(TerrariaItem(ItemName.BOSS_WALL_OF_FLESH, ItemClassification.progression, None, player))
    world.get_location(LocationName.MOON_LORD_DEFEATED, player).place_locked_item(TerrariaItem(ItemName.BOSS_MOON_LORD, ItemClassification.progression, None, player))


def create_region(world: MultiWorld, player: int, name: str, locations=None, exits=None):
    # Shamelessly stolen from the ROR2 definition, lol
    # Thats okay I stole all your code too rogue legacy
    ret = Region(name, None, name, player)
    ret.world = world
    if locations:
        for location in locations:
            loc_id = location_table.get(location, 0)
            location = TerrariaLocation(player, location, loc_id, ret)
            ret.locations.append(location)
    if exits:
        for exit in exits:
            ret.exits.append(Entrance(player, exit, ret))

    return ret
