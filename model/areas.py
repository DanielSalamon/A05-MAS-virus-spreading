
class Area():
    def __init__(self):
        self.capacity = 1
        self.members = list()
        self.memNum = 0
        self.full = False
        self.numberOfInfected = 0
    
    def addMember(agent):
        if not self.full:
            self.members.append(agent)
            self.menNum += 1
            if self.capacity == self.menNum:
                self.full = True
        return not self.full
    
    def isFull(self):
        return self.full
    
class Home(Area):
    def __init__(self):
        self.capacity = 2 
    
class Other(Area):
    def __init__(self):
        self.capacity = 50
    
class School(Area):
    def __init__(self):
        self.capacity = 250
    
class Work(Area):
    def __init__(self):
        self.capacity = 6