import typing

from BaseClasses import Item, MultiWorld, Tutorial
from .Items import TerrariaItem, ItemData, item_table, stat_upgrade_table, misc_items_table
from .Locations import TerrariaLocation, location_table, progression_location_table, achievement_location_table, \
            life_crystal_location_table, mana_crystal_location_table
from .Options import terraria_options
from .Regions import create_regions
from .Rules import set_rules
from .Names import ItemName
from ..AutoWorld import World, WebWorld


class TerrariaWeb(WebWorld):
    theme = "stone";
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Terraria Randomizer software on your computer. This guide covers single-player, multiworld, and related software.",
        "English",
        "terraria_en.md",
        "terraria/en",
        ["Whoneedspacee"]
    )]


class TerrariaWorld(World):
    """
    Terraria is a 2D sandbox game with gameplay that revolves around exploration, building, crafting, combat, survival, and mining, 
    playable in both single-player and multiplayer modes. The game has a 2D sprite tile-based graphical style reminiscent of the 
    16-bit sprites found on the Super NES. Defeat the Moon Lord or Wall of Flesh to win.
    """
    game: str = "Terraria"
    options = terraria_options
    topology_present = True
    data_version = 3
    required_client_version = (0, 2, 3)
    web = TerrariaWeb()

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = location_table

    def _get_slot_data(self):
        return {
            "progressive_crafting": self.world.progressive_crafting[self.player],
            "death_link": self.world.death_link[self.player],
        }

    def _create_items(self, name: str):
        data = item_table[name]
        return [self.create_item(name)] * data.quantity

    def fill_slot_data(self) -> dict:
        slot_data = self._get_slot_data()
        for option_name in terraria_options:
            option = getattr(self.world, option_name)[self.player]
            slot_data[option_name] = option.value

        return slot_data

    def generate_basic(self):
        itempool: typing.List[TerrariaItem] = []
        total_required_locations = len(location_table)

        # Fill item pool with all required items
        for item in {**stat_upgrade_table}:
            itempool += self._create_items(item)
            
        # Fill item pool with the remaining
        for _ in range(len(itempool), total_required_locations):
            item = self.world.random.choice(list(misc_items_table.keys()))
            check_quantity = list(misc_items_table[item])
            while check_quantity[2] <= 0:
                item = self.world.random.choice(list(misc_items_table.keys()))
                check_quantity = list(misc_items_table[item])
            itempool += [self.create_item(item)]
            check_quantity[2] = check_quantity[2] - 1;
            misc_items_table[item] = tuple(check_quantity)

        self.world.itempool += itempool

    def get_filler_item_name(self) -> str:
        return self.world.random.choice(list(misc_items_table.keys()))

    def create_regions(self):
        create_regions(self.world, self.player)

    def create_item(self, name: str) -> Item:
        data = item_table[name]
        return TerrariaItem(name, data.progression, data.code, self.player)

    def set_rules(self):
        set_rules(self.world, self.player)
