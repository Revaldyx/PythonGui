from kivy.config import Config
from kivy.uix.gridlayout import GridLayout
import kivy
from kivy.app import App

kivy.require('2.0.0')

# config ukuran window
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '400')


class CalcGridLayout(GridLayout):
    def calculate(self, calculation):
        if calculation:
            try:
                # fungsi eval() berfungsi untuk memparsing (menguraikan) string ekspresi yang dilewatkan ke dalamnya,
                # dan menjalankannya sebagai ekspresi Python murni.
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = "Error"


class CalculatorApp(App):

    def build(self):
        return CalcGridLayout()


if __name__ == "__main__":
	calcApp = CalculatorApp()
	calcApp.run()
