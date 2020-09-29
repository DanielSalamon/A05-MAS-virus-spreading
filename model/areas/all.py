from .area import Area
class All(Area):
    def __init__(self,idNum):
        super().__init__(idNum)
        self.capacity = 99999
        self.areaType = 'all'