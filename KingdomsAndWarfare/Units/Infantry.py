from .Unit import Unit

class Infantry(Unit):
    def __init__(self, name: str, description: str):
        self.type = Unit.Type.INFANTRY
        super().__init__(name, description)

    def level_up(self) -> None:
        self.attack = self.attack + 1
        self.defense = self.defense + 2
        self.morale = self.morale + 2
        self.command = self.command + 2
    
    def level_down(self) -> None:
        self.attack = self.attack - 1
        self.defense = self.defense - 2
        self.morale = self.morale - 2
        self.command = self.command - 2
    
    def upgrade(self) -> None:
        self.power = self.power + 2
        self.toughness = self.toughness + 2
    
    def downgrade(self) -> None:
        self.power = self.power - 2
        self.toughness = self.toughness - 2