import datetime


class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percent):
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percent = completion_percent

    def __str__(self):
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority: {self.priority}, estimate: ${self.cost_estimate:.2f}, "
                f"completion: {self.completion_percent}%")

    def is_complete(self):
        """Determine if project is complete"""
        return self.completion_percent == 100

    def project_to_string(self):
        """Return a string representation of the project"""
        return (f"{self.name}\t{self.start_date.strftime('%d/%m/%Y')}\t"
                f"{self.priority}\t{self.cost_estimate}\t{self.completion_percent}")



