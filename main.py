from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import math

class Root(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=20, spacing=16, **kwargs)
        self.add_widget(Label(text="⚡ Conductor Area Calculator", font_size="22sp", bold=True))
        self.d_input = TextInput(hint_text="Enter diameter in mm (e.g., 2.89)", multiline=False, input_filter="float")
        self.add_widget(self.d_input)
        btn = Button(text="Calculate Area"); btn.bind(on_release=self.calculate_area)
        self.add_widget(btn)
        self.result = Label(text="Area: — mm²", font_size="18sp")
        self.add_widget(self.result)
        self.add_widget(Label(text="[i]A = π × (d/2)^2[/i]", markup=True))

    def calculate_area(self, *_):
        try:
            d = float((self.d_input.text or "").strip())
            if d <= 0: raise ValueError
            area = math.pi * (d/2)**2
            self.result.text = f"Area: {area:.4f} mm²"
        except Exception:
            self.result.text = "Please enter a valid positive number."

class ConductorAreaApp(App):
    def build(self): 
        self.title = "Conductor Area"
        return Root()

if __name__ == "__main__":
    ConductorAreaApp().run()
