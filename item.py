class Item:
    def __init__(self,name,quantity):
        self.name = name
        self.quantity = quantity

    def checkQuantity(self):
        if self.quantity <= 0:
            return False
        else:
            print(f"you have {self.quantity}")
            return True
        
    def setName(self,value):
        self.name = value

    def getName(self):
        return self.name
    
    def setQuantity(self,value):
        self.quantity = value
        
    def getQuantity(self):
        return self.quantity