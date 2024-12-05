from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

NAMES = {"James", "Jonathan", "Tiffany", "Sandra"}


class DynamicWidgetsApp(App):
    """Kivy app to dynamically create labels."""

    def __init__(self, **kwargs):
        """Initialize the app."""
        super().__init__(**kwargs)
        self.names = NAMES

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_widgets.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create labels from data and add them to the GUI."""
        for name in self.names:
            label = Label(text=name)
            self.root.ids.entries_box.add_widget(label)

    def clear_all(self):
        """Clear all widgets from the entries box."""
        self.root.ids.entries_box.clear_widgets()


if __name__ == "__main__":
    DynamicWidgetsApp().run()
