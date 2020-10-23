from .area import Area


class Other(Area):
    def __init__(self):
        super().__init__()
        self.capacity = 50
        self.areaType = 'other'
