from .area import Area


class School(Area):
    def __init__(self):
        super().__init__()
        self.capacity = 250
        self.areaType = 'school'
