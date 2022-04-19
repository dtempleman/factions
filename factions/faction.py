from pathlib import Path
from dataclasses import dataclass
import json

DATA_DIR = Path('data')
SAVE_FILE = DATA_DIR / 'factions.json'


@dataclass
class Faction():
    name: str
    force: int
    wealth: int
    cunning: int
    treasure: int = 0
    

    def __str__(self):
        return f"{self.name}: {self.get_stats()} treasure:  {self.get_treasure()}"

    def get_force_stat(self):
        return self.force

    def get_wealth_stat(self):
        return self.wealth
    
    def get_cunning_stat(self):
        return self.cunning

    def get_stats(self):
        return dict(
            force=self.get_force_stat(),
            wealth=self.get_wealth_stat(),
            cunning=self.get_cunning_stat(),
        )

    def get_treasure(self):
        return self.treasure

    def add_treasure(self, x):
        self.treasure += x
    
    def remove_treasure(self, x):
        self.treasure -= x


def save_factions_to_json(factions, save_file=SAVE_FILE):
    data = []
    for faction in factions:
        fac = faction.get_stats()
        fac["name"] = faction.name
        data.append(fac)
    with open(save_file, 'w') as f:
        for fac in factions:
            json.dump(data, f)


def load_factions_from_json(save_file=SAVE_FILE):
    factions = []
    with open(save_file) as f:
        for data in f:
            fac = json.loads(data)
            print(fac)
            factions.append(
                Faction(
                    name=fac["name"],
                    force=fac["force"],
                    wealth=fac["wealth"],
                    cunning=fac["cunning"],
                )
            )


def caclulate_faction_income(faction):
    return 0


