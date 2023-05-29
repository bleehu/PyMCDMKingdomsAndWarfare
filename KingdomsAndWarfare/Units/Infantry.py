from .Unit import Unit

class Infantry(Unit):
    def level_up(self) -> None:
        self.Attack = self.Attack + 1
        self.Defense = self.Defense + 2
        self.Morale = self.Morale + 2
        self.Command = self.Command + 2
    
    def level_down(self) -> None:
        self.Attack = self.Attack - 1
        self.Defense = self.Defense - 2
        self.Morale = self.Morale - 2
        self.Command = self.Command - 2
    
    def upgrade(self) -> None:
        self.Power = self.Power + 2
        self.Toughness = self.Toughness + 2
    
    def downgrade(self) -> None:
        self.Power = self.Attack - 2
        self.Toughness = self.Toughness - 2