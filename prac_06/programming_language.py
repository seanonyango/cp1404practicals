class ProgrammingLanguage:
    def __init__(self, language="", typing="", reflection="", year=0):
        self.language = language
        self.typing = typing.title()
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.typing == "Dynamic":
            return True
        else:
            return False

    def __str__(self):
        return f"{self.language}, {self.typing} Typing, Reflection = {self.reflection}, First appeared in {self.year}"
