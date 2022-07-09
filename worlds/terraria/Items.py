import typing

from BaseClasses import Item, ItemClassification
from .Names import ItemName


class ItemData(typing.NamedTuple):
    code: typing.Optional[int]
    progression: bool
    quantity: int = 1
    event: bool = False


class TerrariaItem(Item):
    game: str = "Terraria"

    def __init__(self, name, advancement: bool = False, code: int = None, player: int = None):
        super(TerrariaItem, self).__init__(name, advancement, code, player)


# Separate tables for each type of item.
stat_upgrade_table = {
    #Wood unlocked at start
    #Copper + Tin, Iron + Lead, Silver + Tungsten, Gold + Platinum + Fossil + Bee, Obsidian + Meteor + Jungle + Necro + Shadow + Crimson, Molten (6 tiers, Pre-Hardmode)
    #Spider + Cobalt + Palladium, Mythril + Orichalcum, Adamantite + Titanium + Frost + Forbidden, Hallowed, Chlorophyte + Turtle + Shroomite + Spectre + Spooky, Lunar (6 tiers, Hardmode)
    ItemName.PROGRESSIVE_CRAFTING: ItemData(22000, ItemClassification.progression, 12, True),
    #ItemName.LIFE_CRYSTAL: ItemData(22001, True, 15, True),
    #ItemName.MANA_CRYSTAL: ItemData(22002, True, 9, True),
}

misc_items_table = {
    #Crates / Rewards
    ItemName.WOODEN_CRATE: ItemData(22101, ItemClassification.filler, 10),
    ItemName.IRON_CRATE: ItemData(22102, ItemClassification.filler, 10),
    ItemName.GOLDEN_CRATE: ItemData(22103, ItemClassification.filler, 10),
    ItemName.JUNGLE_CRATE: ItemData(22104, ItemClassification.filler, 10),
    ItemName.SKY_CRATE: ItemData(22105, ItemClassification.filler, 10),
    ItemName.CORRUPT_CRATE: ItemData(22106, ItemClassification.filler, 10),
    ItemName.CRIMSON_CRATE: ItemData(22107, ItemClassification.filler, 10),
    ItemName.HALLOWED_CRATE: ItemData(22108, ItemClassification.filler, 10),
    ItemName.DUNGEON_CRATE: ItemData(22109, ItemClassification.filler, 10),
    ItemName.FROZEN_CRATE: ItemData(22110, ItemClassification.filler, 10),
    ItemName.OASIS_CRATE: ItemData(22111, ItemClassification.filler, 10),
    ItemName.OBSIDIAN_CRATE: ItemData(22112, ItemClassification.filler, 10),
    ItemName.OCEAN_CRATE: ItemData(22113, ItemClassification.filler, 10),
    #Traps
    ItemName.MOB_TRAP: ItemData(22200, ItemClassification.trap, 1),
    ItemName.BOULDER_TRAP: ItemData(22201, ItemClassification.trap, 1),
    ItemName.LAVA_TRAP: ItemData(22202, ItemClassification.trap, 1),
    ItemName.ICE_TRAP: ItemData(22203, ItemClassification.trap, 1),
    ItemName.GRAVITY_FLIP_TRAP: ItemData(22204, ItemClassification.trap, 1),
    ItemName.BLOOD_MOON_TRAP: ItemData(22205, ItemClassification.trap, 1),
}

# Complete item table.
item_table = {
    **stat_upgrade_table,
    **misc_items_table,
}

lookup_id_to_name: typing.Dict[int, str] = {data.code: item_name for item_name, data in item_table.items() if data.code}
