from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.609


class MilesConverter(App):
    """Kivy App for converting miles to kilometres."""
    km_value = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, text):
        """Handle convert button"""
        miles = self.string_to_float(text)
        self.update_result(miles)

    def handle_change(self, text, change):
        """Handle up and down button"""
        miles = self.string_to_float(text) + change
        self.root.ids.miles_input.text = str(miles)

    def update_result(self, miles):
        self.km_value = str(miles * MILES_TO_KM)

    @staticmethod
    def string_to_float(text):
        """Convert text value to float """
        try:
            return float(text)
        except ValueError:
            return 0.0


MilesConverter().run()
