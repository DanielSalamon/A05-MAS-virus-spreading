from .area import Area


class Home(Area):
    def __init__(self, idNum):
        super().__init__(idNum)
        self.capacity = 2
        self.areaType = 'home'
