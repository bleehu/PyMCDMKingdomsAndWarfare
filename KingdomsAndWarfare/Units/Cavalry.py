from .Unit import Unit

class Cavalry(Unit):
    
    def __init__(self, name: str, description: str):
        self.type = Unit.Type.CAVALRY
        super().__init__(name, description)