import typing

from Options import Choice, Range, Option, Toggle, DeathLink, DefaultOnToggle, OptionList, OptionSet


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
    display_name = "Progressive Crafting"
    
class ProgressiveMana(Toggle):
    """
    If enabled, mana crystals are randomized.
    """
    display_name = "Progressive Crafting"

class TrapAmount(Range):
    """
    Determines the amount of traps randomized into the pool
    """
    display_name = "Trap Amount"
    range_start = 0
    range_end = 30
    default = 6

terraria_options: typing.Dict[str, type(Option)] = {
    "progressive_crafting": ProgressiveCrafting,
    "progressive_life": ProgressiveLife,
    "progressive_mana": ProgressiveMana,
    "trap_amount": TrapAmount,
    "death_link": DeathLink,
}
