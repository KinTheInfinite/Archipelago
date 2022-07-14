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
    ItemName.LIFE_CRYSTAL: ItemData(22001, True, 15, True),
    ItemName.MANA_CRYSTAL: ItemData(22002, True, 9, True),
}

# Traps
trap_items_table = {
    ItemName.MOB_TRAP: ItemData(22100, ItemClassification.trap),
    ItemName.BOULDER_TRAP: ItemData(22101, ItemClassification.trap),
    ItemName.LAVA_TRAP: ItemData(22102, ItemClassification.trap),
    ItemName.ICE_TRAP: ItemData(22103, ItemClassification.trap),
    ItemName.GRAVITY_FLIP_TRAP: ItemData(22104, ItemClassification.trap),
    ItemName.BLOOD_MOON_TRAP: ItemData(22105, ItemClassification.trap),
}

# Crates / Rewards
misc_items_table = {
    ItemName.MONEY_BAG: ItemData(22200, ItemClassification.filler),
    ItemName.POTION_BAG: ItemData(22201, ItemClassification.filler),
    ItemName.SOUL_BAG: ItemData(22202, ItemClassification.filler),
    ItemName.CRATE_BAG: ItemData(22203, ItemClassification.filler),
    ItemName.BAR_BAG: ItemData(22204, ItemClassification.filler),
    ItemName.SPAWNER_BAG: ItemData(22205, ItemClassification.filler),
}

# Complete item table.
item_table = {
    **stat_upgrade_table,
    **trap_items_table,
    **misc_items_table,
}

lookup_id_to_name: typing.Dict[int, str] = {data.code: item_name for item_name, data in item_table.items() if data.code}
