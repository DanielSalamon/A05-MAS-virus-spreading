from .area import Area


class Work(Area):
    def __init__(self):
        super().__init__()
        self.capacity = 6
        self.areaType = 'work'
