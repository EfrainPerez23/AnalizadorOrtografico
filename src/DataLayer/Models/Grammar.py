class Grammar(object):

    def __init__(self, category, errorPosition, message, replacements, errorLength):
        self.category = category
        self.errorPosition = errorPosition
        self.message = message
        self.replacements = replacements
        self.errorLength = errorLength
    
    def json(self):
        return {
            'category': self.category,
            'errorPosition': self.errorPosition,
            'message': self.message,
            'replacements': self.replacements,
            'errorLength': self.errorLength
        }