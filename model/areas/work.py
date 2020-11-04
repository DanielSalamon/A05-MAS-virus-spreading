from .area import Area


class Work(Area):
    def __init__(self, model):
        super().__init__(model)
        self.capacity = 6
        self.areaType = 'work'
