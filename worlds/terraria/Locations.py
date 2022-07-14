import typing

from BaseClasses import Location
from .Names import LocationName


class TerrariaLocation(Location):
    game: str = "Terraria"


# Base Locations
base_location_table = {
    LocationName.TERRARIA_MENU:None,
    #LocationName.KING_SLIME_DEFEATED:None,
    #LocationName.EYE_DEFEATED:None,
    #LocationName.SHADOW_OR_HEART_BROKEN:None,
    #LocationName.BRAIN_OR_EATER_DEFEATED:None,
    #LocationName.QUEEN_BEE_DEFEATED:None,
    #LocationName.SKELETRON_DEFEATED:None,
    LocationName.WOF_DEFEATED:None,
    #LocationName.QUEEN_SLIME_DEFEATED:None,
    #LocationName.TWINS_DEFEATED:None,
    #LocationName.DESTROYER_DEFEATED:None,
    #LocationName.SKELETRON_PRIME_DEFEATED:None,
    #LocationName.PLANTERA_DEFEATED:None,
    #LocationName.GOLEM_DEFEATED:None,
    #LocationName.DUKE_FISHRON_DEFEATED:None,
    #LocationName.EMPRESS_DEFEATED:None,
    #LocationName.LUNATIC_CULTIST_DEFEATED:None,
    LocationName.MOON_LORD_DEFEATED:None,
    
    LocationName.TIMBER:22500,
    LocationName.NO_HOBO:22501,
    LocationName.HAMMER_TIME:22502,
    LocationName.OOO_SHINY:22503,
    LocationName.HEART_BREAKER:22504,
    #LocationName.THROWING_LINES:22505,
    LocationName.YOU_CAN_DO_IT:22506,
    LocationName.BENCHED:22507,
    #LocationName.I_AM_LOOT:22508,
    #LocationName.STAR_POWER:22509,
    LocationName.HEAVY_METAL:22510,
    #LocationName.MATCHING_ATTIRE:22511,
    #LocationName.THE_CAVALRY:22512,
    #LocationName.FASHION_STATEMENT:22513,
    LocationName.SLIPPERY_SHINOBI:22514,
    LocationName.LIKE_A_BOSS:22515,
    #LocationName.HOLD_ON_TIGHT:22516,
    LocationName.EYE_ON_YOU:22517,
    LocationName.SMASHING_POPPET:22518,
    LocationName.WORM_FODDER_MASTERMIND:22519,
    LocationName.COMPLETELY_AWESOME:22520,
    #LocationName.VEHICULAR_MANSLAUGHTER:22521,
    #LocationName.INTO_ORBIT:22522,
    #LocationName.WHERES_MY_HONEY:22523,
    LocationName.STING_OPERATION:22524,
    #LocationName.NOT_THE_BEES:22525,
    LocationName.BONED:22526,
    LocationName.DUNGEON_HEIST:22527,
    #LocationName.ITS_GETTING_HOT_IN_HERE:22528,
    #LocationName.ROCK_BOTTOM:22529,
    LocationName.GOBLIN_PUNTER:22530,
    LocationName.MINER_FOR_FIRE:22531,
    LocationName.STILL_HUNGRY:22532,
    LocationName.ITS_HARD:22533,
    LocationName.BEGONE_EVIL:22534,
    LocationName.EXTRA_SHINY:22535,
    #LocationName.HEAD_IN_THE_CLOUDS:22536,
    #LocationName.BULLDOZER:22537,
    LocationName.BLOODBATH:22538,
    #LocationName.JEEPERS_CREEPERS:22539,
    LocationName.BUCKETS_OF_BOLTS:22540,
    LocationName.DRAX_ATTAX:22541,
    LocationName.PHOTOSYNTHESIS:22542,
    #LocationName.GET_A_LIFE:22543,
    LocationName.THE_GREAT_SOUTHERN_PLANTKILL:22544,
    LocationName.TEMPLE_RAIDER:22545,
    LocationName.ROBBING_THE_GRAVE:22546,
    LocationName.THERE_ARE_SOME_WHO_CALL_HIM:22547,
    LocationName.DECEIVER_OF_FOOLS:22548,
    #LocationName.FUNKYTOWN:22549,
    LocationName.BIG_BOOTY:22550,
    LocationName.PRETTY_IN_PINK:22551,
    #LocationName.DYE_HARD:22552,
    #LocationName.THE_FREQUENT_FLYER:22553,
    #LocationName.YOU_AND_WHAT_ARMY:22554,
    LocationName.PRISMANCER:22555,
    #LocationName.MARATHON_MEDALIST:22556,
    LocationName.LIHZAHRDIAN_IDOL:22557,
    LocationName.FISH_OUT_OF_WATER:22558,
    LocationName.SWORD_OF_THE_HERO:22559,
    LocationName.TIL_DEATH:22560,
    LocationName.ARCHAEOLOGIST:22561,
    LocationName.IT_CAN_TALK:22562,
    #LocationName.TOPPED_OFF:22563,
    LocationName.OBSESSIVE_DEVOTION:22564,
}

life_crystal_location_table = {f"{LocationName.LIFE_CRYSTAL} {i + 1}": i + 22700 for i in range(15)}

mana_crystal_location_table = {f"{LocationName.MANA_CRYSTAL} {i + 1}": i + 22800 for i in range(9)}

location_table = {
    **base_location_table,
    **life_crystal_location_table,
    **mana_crystal_location_table,
}

lookup_id_to_name: typing.Dict[int, str] = {id: name for name, _ in location_table.items()}
