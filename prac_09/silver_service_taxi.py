from taxi import Taxi


class SilverServiceTaxi(Taxi):
    def __init__(self, name, fuel, fanciness):
        flagfall = 4.50
        super().__init__(name, fuel)
        self.price_per_km *= fanciness
        self.flagfall = flagfall

    def __str__(self):
        return f"{super().__str__()} plus flagfall of {self.flagfall}"

    def get_fare(self):
        """Calculates fare"""
        return super().get_fare() + self.flagfall
