from programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
languages = [python, ruby, visual_basic]
dynamic_languages = [language.language for language in languages if language.is_dynamic()]
print(f"The dynamic languages are:\n{"\n".join(dynamic_languages)}")
