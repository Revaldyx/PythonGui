from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


from kivy.core.window import Window

Window.size = (400,400)

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2
                
        self.inside.add_widget(Label(text="Nama: ", font_size=24,))
        self.nama = TextInput(multiline="false")
        self.inside.add_widget(self.nama)
        
        self.inside.add_widget(Label(text="NPM: ", font_size=24))
        self.npm = TextInput(multiline="false")
        self.inside.add_widget(self.npm)
        
        self.inside.add_widget(Label(text="Kelas: ", font_size=24))
        self.kelas = TextInput(multiline="false")
        self.inside.add_widget(self.kelas)

        self.add_widget(self.inside)

        self.simpan = Button(text="Simpan", font_size=32)
        self.simpan.bind(on_press=self.pressed)
        self.add_widget(self.simpan)

    def pressed(self, instance):
        nama = self.nama.text
        npm = self.npm.text
        kelas = self.kelas.text

        print("Nama:", nama, "NPM: ", npm, "Kelas: ", kelas)
        
        # popup = Popup(title='Data Mahasiswa', content=Label(text='Nama, nama, '),
        #       auto_dismiss=True)
        # popup.open()

class MyApp (App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    MyApp().run()