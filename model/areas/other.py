from .area import Area


class Other(Area):
    def __init__(self, idNum):
        super().__init__(idNum)
        self.capacity = 50
        self.areaType = 'other'
