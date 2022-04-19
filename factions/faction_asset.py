from dataclasses import dataclass
from faction import Faction
from enum import Enum, auto


class AssetType(Enum):
    NONE = auto()
    CUNNING = auto()
    WEALTH = auto()
    FORCE = auto()
    SPECIAL = auto()


class Dice(Enum):
    D4 = auto()
    D6 = auto()
    D8 = auto()
    D10 = auto()


class MagicTier(Enum):
    NONE = auto()
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()   


@dataclass
class FactionAsset():
    name: str
    owner: Faction
    cost: int

    asset_type: AssetType
    asset_tier: int
    magic: MagicTier

    max_hits: int
    hits: int

    qualities: list = []

    attack_type: AssetType = AssetType.NONE
    defend_type: AssetType = AssetType.NONE

    damage_dice: Dice = Dice.D6
    damage_n_dice: int = 0

    counter_dice: Dice = Dice.D6
    counter_n_dice: int = 0


def create_asset(faction, asset, location):
    # add an asset to the location and set the owner to faction.
    return asset


def move_asset(asset, to_location):
    # move the asset to the new location and apply any event.
    pass


def attack(attacker, defender):
    # the attacker 'attacks' the defender.
    pass


def repair_asset(asset, x):
    # replending the hp of the asset by x.
    pass


def scout(asset):
    # the asset scouts all tiles within its rage.
    pass