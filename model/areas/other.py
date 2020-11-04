from .area import Area


class Other(Area):
    def __init__(self, model):
        super().__init__(model)
        self.capacity = 50
        self.areaType = 'other'
