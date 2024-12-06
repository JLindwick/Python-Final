
class Moves():
    def __init__(self,name,moveType,attack):
        self.name = name
        self.moveType = moveType
        self.attack = attack
    
    def getName(self):
        return self.name
    
    def setName(self,value):
        self.name = value

    def getMoveType(self):
        return self.moveType
    
    def setMoveType(self,value):
        self.moveType = value

    def getAttack(self):
        return self.attack
    
    def setAttack(self,value):
        self.attack = value    


    