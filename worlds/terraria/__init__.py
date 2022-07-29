import typing
import random

from BaseClasses import Item, MultiWorld, ItemClassification, Tutorial
from .Items import TerrariaItem, ItemData, item_table, stat_upgrade_table, trap_items_table, misc_items_table
from .Locations import TerrariaLocation, location_table, base_location_table, \
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
    16-bit sprites found on the Super NES. Defeat the Moon Lord or Wall of Flesh to win!
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
            "progressive_life": self.world.progressive_life[self.player],
            "progressive_mana": self.world.progressive_mana[self.player],
            "trap_amount": self.world.trap_amount[self.player],
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
        total_required_locations = 0
        for region in self.world.regions:
            total_required_locations += len(region.locations)
        # Subtract Event Locations
        total_required_locations -= 3

        # Progressive Crafting Option
        # Wood unlocked at start, 12 tiers of upgrades
        if self.world.progressive_crafting[self.player]:
            itempool += [self.create_item(ItemName.PROGRESSIVE_CRAFTING)] * 12
            
        # Progressive Life Option
        if self.world.progressive_life[self.player]:
            itempool += [self.create_item(ItemName.LIFE_CRYSTAL)] * 15
            
        # Progressive Mana Option
        if self.world.progressive_mana[self.player]:
            itempool += [self.create_item(ItemName.MANA_CRYSTAL)] * 9
            
        # Random trap amount (if any)
        trap_amount = int(self.world.trap_amount[self.player])
        if trap_amount > 0:
            for i in range(trap_amount):
                itempool += [self.create_item(random.choice(list(trap_items_table.keys())))]
            
        # Fill item pool with the remaining misc items
        for _ in range(len(itempool), total_required_locations):
            item = self.world.random.choice(list(misc_items_table.keys()))
            #check_quantity = list(misc_items_table[item])
            #while check_quantity[2] <= 0:
                #item = self.world.random.choice(list(misc_items_table.keys()))
                #check_quantity = list(misc_items_table[item])
            itempool += [self.create_item(item)]
            #check_quantity[2] = check_quantity[2] - 1;
            #misc_items_table[item] = tuple(check_quantity)

        self.world.itempool += itempool

    def get_filler_item_name(self) -> str:
        return self.world.random.choice(list(misc_items_table.keys()))

    def create_regions(self):
        create_regions(self.world, self.player)

    def create_item(self, name: str) -> Item:
        data = item_table[name]
        return TerrariaItem(name, ItemClassification.progression if data.progression else ItemClassification.filler, data.code, self.player)

    def set_rules(self):
        set_rules(self.world, self.player)
