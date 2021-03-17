import kivy
from kivy.app import App 

kivy.require('2.0.0') 

from kivy.uix.gridlayout import GridLayout 

from kivy.config import Config 

Config.set('graphics', 'resizable', 0) 
Config.set('graphics', 'width', '400') 
Config.set('graphics', 'height', '400') 


class CalcGridLayout(GridLayout): 

	def calculate(self, calculation): 
		if calculation: 
			try: 
				self.display.text = str(eval(calculation)) 
			except Exception: 
				self.display.text = "Error"

class CalculatorApp(App): 

	def build(self): 
		return CalcGridLayout() 

calcApp = CalculatorApp() 
calcApp.run() 

