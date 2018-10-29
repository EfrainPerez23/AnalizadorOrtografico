import language_check
tool = language_check.LanguageTool('es-ES')
msg = 'Hola como komo q'
matches = tool.check(msg)
for match in matches:
    print(match)
print(language_check.correct(msg, matches))