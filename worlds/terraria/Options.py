import typing

from Options import Choice, Range, Option, Toggle, DeathLink, DefaultOnToggle, OptionList, OptionSet

class RequiredBosses(Choice):
    """
    Determines the win condition for the randomizer.
    """
    display_name = "Required Bosses"
    option_none = 0
    option_wall_of_flesh = 1
    option_moon_lord = 2
    default = 2
    
class TrapAmount(Range):
    """
    Determines the amount of traps randomized into the pool
    """
    display_name = "Trap Amount"
    range_start = 0
    range_end = 30
    default = 6

class ProgressiveCrafting(Toggle):
    """
    If enabled, crafting certain tiers of items: copper, iron, adamantite, etc
    is locked behind progressive item upgrades.
    """
    display_name = "Progressive Crafting"
    
class ProgressiveLife(Toggle):
    """
    If enabled, life crystals are randomized.
    """
    display_name = "Progressive Life Crystals"
    
class ProgressiveMana(Toggle):
    """
    If enabled, mana crystals are randomized.
    """
    display_name = "Progressive Mana Crystals"

terraria_options: typing.Dict[str, type(Option)] = {
    "required_bosses": RequiredBosses,
    "trap_amount": TrapAmount,
    "progressive_crafting": ProgressiveCrafting,
    "progressive_life": ProgressiveLife,
    "progressive_mana": ProgressiveMana,
    "death_link": DeathLink,
}
