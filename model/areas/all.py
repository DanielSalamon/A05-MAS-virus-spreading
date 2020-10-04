from .area import Area
class All(Area):
    def __init__(self):
        super().__init__()
        self.capacity = 99999
        self.areaType = 'all'