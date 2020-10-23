from .area import Area
class All(Area):
    def __init__(self, model):
        super().__init__(model)
        self.capacity = 99999
        self.areaType = 'all'