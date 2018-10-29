from DataLayer.DataAccessObject.Dependencies.DTO import DTO

class User(DTO):
    
    def __init__(self, _id, firstName, lastName, email, wrongWords):
        self.id = _id
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.wrongWords = wrongWords
    
    def json(self):
        return {
            'firstName': self.firstName,
            'lastName': self.lastName,
            'email': self.email,
            'wrongWords': self.wrongWords
        }

    def isValid(self):
        if self.id and self.firstName and self.lastName and self.email:
            return True
        return False