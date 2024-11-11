class Guitar:
    def __init__(self, name="", year=0, cost=0, current_year=0):
        self.name = name
        self.year = year
        self.cost = cost
        self.current_year = current_year

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def __repr__(self):
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def get_age(self):
        age = self.current_year - self.year
        return age

    def is_vintage(self):
        if Guitar.get_age(self) > 50:
            return True
        else:
            return False
