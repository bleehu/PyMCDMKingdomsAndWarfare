from .Unit import Unit

class Artillery(Unit):
    def __init__(self, name: str, description: str):
        self.type = Unit.Type.ARTILLERY
        super().__init__(name, description)