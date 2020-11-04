from .area import Area


class School(Area):
    def __init__(self, model):
        super().__init__(model)
        self.capacity = 250
        self.areaType = 'school'
