from model.agents import baseAgent

class Meetings():

    def __init__(self, model):

        self.model = model
        self.overall = list()
        self.home = list()
        self.school = list()
        self.other = list()

    
    def addAgent(agent):
        contact = agent.getToMeet()
        if contact.sum is not 0:
            for setting in contact:
                for meets in setting:
                    if meets > 0:
                        pass
