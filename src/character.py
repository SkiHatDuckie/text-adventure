class Character:
    def __init__(self, name: str, health: int, level: int, moveset: tuple) -> None:
        self.name = name
        self.health = health
        self.level = level
        self.moveset = moveset
        self.exp = 0

    def check_for_level(self, exp_cap):
        pass


# TODO: Add bleed effect
def on_move_claws(user: Character, opp: Character) -> str:
    damage = 4 * user.level * 1.2
    opp.health -= damage
    return "{user.name} lunged at {opp.name} with sharp claws dealing {damage} dmg"

def on_move_bite(user: Character, opp: Character) -> str:
    damage = 6 * user.level * 1.2
    opp.health -= damage
    return "{user.name} unhinged their jaw at {opp.name} forcibly crushing down at them dealing \
{damage} dmg"

# TODO: Add weakness effect
def on_move_tail_whip(user: Character, opp: Character) -> str:
    damage = 2 * user.level * 1.2
    opp.health -= damage
    return "{user.name} wildly fling their tail at {opp.name} knocking them back dealing \
{damage} dmg"

# TODO: Add charges(?)
def on_move_savor(user: Character) -> str:
    health = 4 * user.level * 1.3
    user.health += health
    return "{user.name} begins to inhale the aroma of ramen then delightfully devour a chunk \
of the noodle in the sack healing {health} HP"

# TODO: Add fire damage effect
def on_move_spicy_breath(user: Character, opp: Character) -> str:
    damage = 3 * user.level * 1.2
    opp.health -= damage
    return "{user.name} begins to stuff their mouth with peppers then chokes them out launching \
them towards {opp.name} dealing {damage} dmg"

def on_move_headbutt(user: Character, opp: Character) -> str:
    opp_damage = 6 * user.level * 1.2
    user_damage = 5
    opp.health -= opp_damage
    user.health -= user_damage
    return "{user.name} violently thrashes againsts {opp.name}'s forehead dealing {opp_damage} \
to the {opp.name} and 5 dmg to themself"

def on_move_slam(user: Character, opp: Character) -> str:
    damage = 4 * user.level * 1.2
    opp.health -= damage
    return "{user.name} jumps into the air slamming down the air creating a shockwave dealing \
{damage} dmg to {opp.name} before climbing back to their wagon"

# TODO: Add taunt effect
def on_move_mock(user: Character, opp: Character) -> str:
    return "{user.name} mocks {opp.name}"

# TODO: Add sleepy effect
def on_move_yawn(user: Character) -> str:
    return "{user.name} yawns during the battle decreasing his next atk by 75%"

# TODO: Add weakness effect
def on_move_flour_throw(user: Character, opp: Character) -> str:
    damage = 2 * user.level * 1.4
    opp.health -= damage
    return "{user.name} pulls out a sack of flour throwing it at {opp.name} dealing {damage} dmg"
