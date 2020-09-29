from .area import Area


class School(Area):
    def __init__(self, idNum):
        super().__init__(idNum)
        self.capacity = 250
        self.areaType = 'school'
