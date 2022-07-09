import typing

from Options import Choice, Range, Option, Toggle, DeathLink, DefaultOnToggle, OptionList, OptionSet


class ProgressiveCrafting(Toggle):
    """
    If enabled, crafting certain tiers of items: copper, iron, adamantite, etc
    is locked behind progressive item upgrades.
    """
    display_name = "Progressive Crafting"

terraria_options: typing.Dict[str, type(Option)] = {
    "progressive_crafting": ProgressiveCrafting,
    "death_link": DeathLink,
}
