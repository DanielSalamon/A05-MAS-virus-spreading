from .area import Area


class Home(Area):
    def __init__(self, model):
        super().__init__(model)
        self.capacity = 2
        self.areaType = 'home'
