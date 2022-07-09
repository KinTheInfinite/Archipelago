from BaseClasses import MultiWorld
from .Names import LocationName, ItemName
from ..AutoWorld import LogicMixin
from ..generic.Rules import set_rule


class TerraraLogic(LogicMixin):
    def _terraria_has_crafting_tier(self, player: int, amount:int) -> bool:
        return self.has(ItemName.PROGRESSIVE_CRAFTING, player, amount)

    def _terraria_has_health_upgrades(self, player: int, amount: int) -> bool:
        return self.has(ItemName.LIFE_CRYSTAL, player, 0)#amount)
        
    def _terraria_has_mana_upgrades(self, player: int, amount: int) -> bool:
        return self.has(ItemName.MANA_CRYSTAL, player, 0)#amount)
        
    def _terraria_health_and_mana_maxed(self, player:int) -> bool:
        return self._terraria_has_health_upgrades(player, 15) and self._terraria_has_mana_upgrades(player, 9)
        
    def _terraria_can_defeat_king_slime(self, player: int) -> bool:
        return self._terraria_has_crafting_tier(player, 3)
        
    def _terraria_can_defeat_eye(self, player: int) -> bool:
        return self._terraria_has_crafting_tier(player, 3) and self._terraria_has_health_upgrades(player, 5) and self._terraria_has_mana_upgrades(player, 5)
        
    def _terraria_can_break_orb_or_heart(self, player: int) -> bool:
        return self._terraria_has_crafting_tier(player, 3) and self._terraria_has_health_upgrades(player, 5) and self._terraria_has_mana_upgrades(player, 5)
        
    def _terraria_can_defeat_brain_or_eater(self, player: int) -> bool:
        return self._terraria_has_crafting_tier(player, 3) and self._terraria_has_health_upgrades(player, 10) and self._terraria_has_mana_upgrades(player, 9)
        
    def _terraria_can_defeat_queen_bee(self, player: int) -> bool:
        return self._terraria_has_crafting_tier(player, 3) and self._terraria_health_and_mana_maxed(player)
        
    def _terraria_can_defeat_skeletron(self, player: int) -> bool:
        return self._terraria_has_crafting_tier(player, 5) and self._terraria_health_and_mana_maxed(player)
        
    def _terraria_can_defeat_wall_of_flesh(self, player: int) -> bool:
        return self._terraria_has_crafting_tier(player, 6) and self._terraria_health_and_mana_maxed(player)
        
    def _terraria_can_defeat_queen_slime(self, player: int) -> bool:
        return self._terraria_has_crafting_tier(player, 7) and self._terraria_health_and_mana_maxed(player)
        
    def _terraria_can_defeat_mechanical_bosses(self, player: int) -> bool:
        return self._terraria_has_crafting_tier(player, 9) and self._terraria_health_and_mana_maxed(player)
        
    def _terraria_can_defeat_plantera(self, player: int) -> bool:
        return self._terraria_has_crafting_tier(player, 10) and self._terraria_health_and_mana_maxed(player)
        
    def _terraria_can_defeat_golem(self, player: int) -> bool:
        return self._terraria_has_crafting_tier(player, 11) and self._terraria_health_and_mana_maxed(player)
        
    def _terraria_can_defeat_duke_fishron(self, player: int) -> bool:
        return self._terraria_has_crafting_tier(player, 11) and self._terraria_health_and_mana_maxed(player)
        
    def _terraria_upgrades_maxed_out(self, player: int) -> bool:
        return self._terraria_has_crafting_tier(player, 12) and self._terraria_health_and_mana_maxed(player)

def set_rules(world: MultiWorld, player: int):
    #Progression
    #set_rule(world.get_location(LocationName.KING_SLIME_DEFEATED, player), lambda state: state._terraria_can_defeat_king_slime(player))
    #set_rule(world.get_location(LocationName.EYE_DEFEATED, player), lambda state: state._terraria_can_defeat_eye(player))
    #set_rule(world.get_location(LocationName.SHADOW_OR_HEART_BROKEN, player), lambda state: state._terraria_can_break_orb_or_heart(player))
    #set_rule(world.get_location(LocationName.BRAIN_OR_EATER_DEFEATED, player), lambda state: state._terraria_can_defeat_brain_or_eater(player))
    #set_rule(world.get_location(LocationName.QUEEN_BEE_DEFEATED, player), lambda state: state._terraria_can_defeat_queen_bee(player))
    #set_rule(world.get_location(LocationName.SKELETRON_DEFEATED, player), lambda state: state._terraria_can_defeat_skeletron(player))
    set_rule(world.get_location(LocationName.WOF_DEFEATED, player), lambda state: state._terraria_can_defeat_wall_of_flesh(player))
    #set_rule(world.get_location(LocationName.QUEEN_SLIME_DEFEATED, player), lambda state: state._terraria_can_defeat_queen_slime(player))
    #set_rule(world.get_location(LocationName.TWINS_DEFEATED, player), lambda state: state._terraria_can_defeat_mechanical_bosses(player))
    #set_rule(world.get_location(LocationName.DESTROYER_DEFEATED, player), lambda state: state._terraria_can_defeat_mechanical_bosses(player))
    #set_rule(world.get_location(LocationName.SKELETRON_PRIME_DEFEATED, player), lambda state: state._terraria_can_defeat_mechanical_bosses(player))
    #set_rule(world.get_location(LocationName.PLANTERA_DEFEATED, player), lambda state: state._terraria_can_defeat_plantera(player))
    #set_rule(world.get_location(LocationName.GOLEM_DEFEATED, player), lambda state: state._terraria_can_defeat_golem(player))
    #set_rule(world.get_location(LocationName.DUKE_FISHRON_DEFEATED, player), lambda state: state._terraria_can_defeat_duke_fishron(player))
    #set_rule(world.get_location(LocationName.EMPRESS_DEFEATED, player), lambda state: state._terraria_upgrades_maxed_out(player))
    #set_rule(world.get_location(LocationName.LUNATIC_CULTIST_DEFEATED, player), lambda state: state._terraria_upgrades_maxed_out(player))
    set_rule(world.get_location(LocationName.MOON_LORD_DEFEATED, player), lambda state: state._terraria_upgrades_maxed_out(player))
    
    #Achievements
    #set_rule(world.get_location(LocationName.MATCHING_ATTIRE, player), lambda state: state._terraria_can_defeat_king_slime(player))
    #set_rule(world.get_location(LocationName.THE_CAVALRY, player), lambda state: state._terraria_can_defeat_king_slime(player))
    #set_rule(world.get_location(LocationName.FASHION_STATEMENT, player), lambda state: state._terraria_can_defeat_king_slime(player))
    set_rule(world.get_location(LocationName.SLIPPERY_SHINOBI, player), lambda state: state._terraria_can_defeat_king_slime(player))
    set_rule(world.get_location(LocationName.LIKE_A_BOSS, player), lambda state: state._terraria_can_defeat_king_slime(player))
    #set_rule(world.get_location(LocationName.HOLD_ON_TIGHT, player), lambda state: state._terraria_can_defeat_king_slime(player))
    
    set_rule(world.get_location(LocationName.EYE_ON_YOU, player), lambda state: state._terraria_can_defeat_eye(player))
    
    set_rule(world.get_location(LocationName.SMASHING_POPPET, player), lambda state: state._terraria_can_break_orb_or_heart(player))
    
    set_rule(world.get_location(LocationName.WORM_FODDER_MASTERMIND, player), lambda state: state._terraria_can_defeat_brain_or_eater(player))
    set_rule(world.get_location(LocationName.COMPLETELY_AWESOME, player), lambda state: state._terraria_can_defeat_brain_or_eater(player))
    #set_rule(world.get_location(LocationName.VEHICULAR_MANSLAUGHTER, player), lambda state: state._terraria_can_defeat_brain_or_eater(player))
    #set_rule(world.get_location(LocationName.INTO_ORBIT, player), lambda state: state._terraria_can_defeat_brain_or_eater(player))
    
    #set_rule(world.get_location(LocationName.WHERES_MY_HONEY, player), lambda state: state._terraria_can_defeat_queen_bee(player))
    set_rule(world.get_location(LocationName.STING_OPERATION, player), lambda state: state._terraria_can_defeat_queen_bee(player))
    #set_rule(world.get_location(LocationName.NOT_THE_BEES, player), lambda state: state._terraria_can_defeat_queen_bee(player))
    
    set_rule(world.get_location(LocationName.BONED, player), lambda state: state._terraria_can_defeat_skeletron(player))
    set_rule(world.get_location(LocationName.DUNGEON_HEIST, player), lambda state: state._terraria_can_defeat_skeletron(player))
    #set_rule(world.get_location(LocationName.ITS_GETTING_HOT_IN_HERE, player), lambda state: state._terraria_can_defeat_skeletron(player))
    #set_rule(world.get_location(LocationName.ROCK_BOTTOM, player), lambda state: state._terraria_can_defeat_skeletron(player))
    set_rule(world.get_location(LocationName.GOBLIN_PUNTER, player), lambda state: state._terraria_can_defeat_skeletron(player))
    
    set_rule(world.get_location(LocationName.MINER_FOR_FIRE, player), lambda state: state._terraria_can_defeat_wall_of_flesh(player))
    set_rule(world.get_location(LocationName.STILL_HUNGRY, player), lambda state: state._terraria_can_defeat_wall_of_flesh(player))
    set_rule(world.get_location(LocationName.ITS_HARD, player), lambda state: state._terraria_can_defeat_wall_of_flesh(player))
    set_rule(world.get_location(LocationName.BEGONE_EVIL, player), lambda state: state._terraria_can_defeat_wall_of_flesh(player))
    set_rule(world.get_location(LocationName.EXTRA_SHINY, player), lambda state: state._terraria_can_defeat_wall_of_flesh(player))
    #set_rule(world.get_location(LocationName.HEAD_IN_THE_CLOUDS, player), lambda state: state._terraria_can_defeat_wall_of_flesh(player))
    #set_rule(world.get_location(LocationName.BULLDOZER, player), lambda state: state._terraria_can_defeat_wall_of_flesh(player))
    set_rule(world.get_location(LocationName.BLOODBATH, player), lambda state: state._terraria_can_defeat_wall_of_flesh(player))
    #set_rule(world.get_location(LocationName.JEEPERS_CREEPERS, player), lambda state: state._terraria_can_defeat_wall_of_flesh(player))
    
    set_rule(world.get_location(LocationName.BUCKETS_OF_BOLTS, player), lambda state: state._terraria_can_defeat_mechanical_bosses(player))
    #set_rule(world.get_location(LocationName.GET_A_LIFE, player), lambda state: state._terraria_can_defeat_mechanical_bosses(player))
    
    set_rule(world.get_location(LocationName.PHOTOSYNTHESIS, player), lambda state: state._terraria_can_defeat_plantera(player))
    set_rule(world.get_location(LocationName.DRAX_ATTAX, player), lambda state: state._terraria_can_defeat_plantera(player))
    set_rule(world.get_location(LocationName.THE_GREAT_SOUTHERN_PLANTKILL, player), lambda state: state._terraria_can_defeat_plantera(player))
    set_rule(world.get_location(LocationName.TEMPLE_RAIDER, player), lambda state: state._terraria_can_defeat_plantera(player))
    set_rule(world.get_location(LocationName.ROBBING_THE_GRAVE, player), lambda state: state._terraria_can_defeat_plantera(player))
    set_rule(world.get_location(LocationName.THERE_ARE_SOME_WHO_CALL_HIM, player), lambda state: state._terraria_can_defeat_plantera(player))
    set_rule(world.get_location(LocationName.DECEIVER_OF_FOOLS, player), lambda state: state._terraria_can_defeat_plantera(player))
    #set_rule(world.get_location(LocationName.FUNKYTOWN, player), lambda state: state._terraria_can_defeat_plantera(player))
    set_rule(world.get_location(LocationName.BIG_BOOTY, player), lambda state: state._terraria_can_defeat_plantera(player))
    set_rule(world.get_location(LocationName.PRETTY_IN_PINK, player), lambda state: state._terraria_can_defeat_plantera(player))
    #set_rule(world.get_location(LocationName.DYE_HARD, player), lambda state: state._terraria_can_defeat_plantera(player))
    #set_rule(world.get_location(LocationName.THE_FREQUENT_FLYER, player), lambda state: state._terraria_can_defeat_plantera(player))
    #set_rule(world.get_location(LocationName.YOU_AND_WHAT_ARMY, player), lambda state: state._terraria_can_defeat_plantera(player))
    set_rule(world.get_location(LocationName.PRISMANCER, player), lambda state: state._terraria_can_defeat_plantera(player))
    #set_rule(world.get_location(LocationName.MARATHON_MEDALIST, player), lambda state: state._terraria_can_defeat_plantera(player))
    
    set_rule(world.get_location(LocationName.LIHZAHRDIAN_IDOL, player), lambda state: state._terraria_can_defeat_golem(player))
    set_rule(world.get_location(LocationName.FISH_OUT_OF_WATER, player), lambda state: state._terraria_can_defeat_golem(player))
    set_rule(world.get_location(LocationName.SWORD_OF_THE_HERO, player), lambda state: state._terraria_can_defeat_golem(player))
    set_rule(world.get_location(LocationName.TIL_DEATH, player), lambda state: state._terraria_can_defeat_golem(player))
    set_rule(world.get_location(LocationName.ARCHAEOLOGIST, player), lambda state: state._terraria_can_defeat_golem(player))
    set_rule(world.get_location(LocationName.IT_CAN_TALK, player), lambda state: state._terraria_can_defeat_golem(player))
    #set_rule(world.get_location(LocationName.TOPPED_OFF, player), lambda state: state._terraria_can_defeat_golem(player))
    
    set_rule(world.get_location(LocationName.OBSESSIVE_DEVOTION, player), lambda state: state._terraria_can_defeat_duke_fishron(player))
    
    #Completion Condition
    world.completion_condition[player] = lambda state: state.has(ItemName.BOSS_MOON_LORD, player)
    