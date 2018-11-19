from DataLayer.DataAccessObject.Dependencies.DTO import DTO

class WrongWord(DTO):
    
    def __init__(self, _id, label, quantity, users):
        self.id = _id
        self.label = label
        self.quantity = quantity
        self.users = users
    
    def json(self):
        return {
            'id': self.id,
            'label': self.label,
            'quantity': self.quantity,
            'users': self.users
        }
    

    def isValid(self):
        if self.label and self.quantity:
            return True
        return False