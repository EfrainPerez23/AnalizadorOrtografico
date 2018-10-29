import language_check
from DataLayer.Models.Grammar import Grammar

class CheckGrammar:

    def checkGrammar(self, message):
        
        tool = language_check.LanguageTool('es-ES')
        matches = tool.check(message)
        return None if len(matches) == 0 else  [
            Grammar(match.category, match.contextoffset, match.msg, match.replacements, match.errorlength).json()
            for match  in matches
        ]
