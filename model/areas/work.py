from .area import Area


class Work(Area):
    def __init__(self, idNum):
        super().__init__(idNum)
        self.capacity = 6
        self.areaType = 'work'
