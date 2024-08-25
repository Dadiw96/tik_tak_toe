from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.switch import Switch
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.slider import Slider
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from allinone import*
class MainMenu(App):
    def __init__(self,g=None,**kwargs):
        super(MainMenu, self).__init__(**kwargs) 
        self.r = 3
        self.twoplayer = False
        self.dif = None
    def build(self):

        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Dodajemy napis "MainMenu" na górze
        title = Label(text="MainMenu", font_size=32, size_hint_y=None, height=50)
        main_layout.add_widget(title)
        
        # Uk³ad poziomy dla checkboxów
        checkbox_layout = BoxLayout(orientation='horizontal', spacing=10)
        
        # Checkbox dla jednego gracza
        self.checkbox1 = CheckBox(active=True)
        checkbox1_label = Label(text="Jeden gracz", size_hint_x=None, width=150)
        self.checkbox1.bind(active=self.on_checkbox_active)
        checkbox_layout.add_widget(checkbox1_label)
        checkbox_layout.add_widget(self.checkbox1)
        
        # Checkbox dla dwóch graczy
        self.checkbox2 = CheckBox()
        checkbox2_label = Label(text="Dwoch graczy", size_hint_x=None, width=150)
        self.checkbox2.bind(active=self.on_checkbox_active)
        checkbox_layout.add_widget(checkbox2_label)
        checkbox_layout.add_widget(self.checkbox2)
        
       

        # Etykieta, która bêdzie wyœwietla³a wartoœæ suwaka roz
        self.tekst_slider_roz = Label(text='Rozmiar planszy: 3', font_size=24, size_hint_y=None, height=50)
        main_layout.add_widget(self.tekst_slider_roz)
        
        # Tworzenie suwaka rozmiaru
        self.slider_roz = Slider(min=3, max=10, value=3, step=1)
        self.slider_roz.bind(value=self.on_value_change_roz)
        main_layout.add_widget(self.slider_roz)
        # Dodajemy uk³ad checkboxów do g³ównego layoutu
        main_layout.add_widget(checkbox_layout)

        # Etykieta, która bêdzie wyœwietla³a wartoœæ suwaka dif
        self.tekst_slider_dif = Label(text='Poziom Trudnosci: 0', font_size=24, size_hint_y=None, height=50)
        main_layout.add_widget(self.tekst_slider_dif)
        # Tworzenie suwaka poziomu trudnoœci
        self.slider_dif = Slider(min=0, max=self.r*self.r, value=0, step=1)
        self.slider_dif.bind(value=self.on_value_change_dif)
        main_layout.add_widget(self.slider_dif)
        # Tworzenie przycisku rozpoczêcia gry
        self.button = Button(text="Rozpocznij gre!",size_hint=(None, None), size=(100, 50))
        self.button.bind(on_press=self.on_button_press) # Przypisanie funkcji do przycisku
        main_layout.add_widget(self.button)
        return main_layout
    def on_checkbox_active(self, checkbox, value):#check box
        if checkbox == self.checkbox1:
            if value:
                self.twoplayer = False
                self.checkbox2.active = False
                self.slider_dif.opacity = 1 # Suwak widoczny
                self.slider_dif.disabled = False
        elif checkbox == self.checkbox2:
            if value:
                self.twoplayer = True
                self.checkbox1.active = False
                self.slider_dif.opacity = 0 # Suwak widoczny
                self.slider_dif.disabled = True
        print(self.twoplayer)
    def on_value_change_roz(self, instance, value):#suwak
        # Aktualizacja tekstu etykiety w zale¿noœci od wartoœci suwaka
        self.r = int(value)
        self.tekst_slider_roz.text = f'Rozmiar planszy: {self.r}'
        new_max_value = self.r * self.r
        
        # Ustawianie maksymalnej wartoœci slidera2 oraz wartoœci slidera2
        self.slider_dif.max = new_max_value
        if self.slider_dif.value > new_max_value:
            self.slider_dif.value = new_max_value
    def on_value_change_dif(self, instance, value):#suwak
        # Aktualizacja tekstu etykiety w zale¿noœci od wartoœci suwaka
        self.dif = int(value)
        self.tekst_slider_dif.text = f'Poziom trudnosci: {int(self.dif)}'
    def on_button_press(self, instance):
        pass
        #gg = Game_gui_front(self.r,self.twoplayer.self.dif)

        
class Game_gui_front(App):
    def __init__(self,r=5,twoplayer = True,dif=0,**kwargs):
        super(Game_gui_front, self).__init__(**kwargs) 
        self.board = Board(r)
        self.playerone = Player
        self.playertwo = None
        self.twoplayer = twoplayer
        self.dif = dif
        self.r = r
        self.arr = self.board.arr
        self.s="o"
        #self.back = Game_gui_back(self.s,self.board,self.twoplayer,self.dif)

        
        #gg = Game_gui_back(board,bot,playerone,playertwo)
    def build(self):
        self.main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        grid_layout = GridLayout(cols=self.r,  size=(100, 100))
        for i in range(self.r*self.r):
            btn = Button(text=f'{self.arr[i]}',font_size=48,)
            btn.bind(on_press=lambda instance, i=i: self.on_button_press(instance, i))
            grid_layout.add_widget(btn)
        self.l_gracz= Label(text=f'Kolej {self.s}', font_size=24, size_hint_y=None, height=50)
        self.main_layout.add_widget(self.l_gracz)
        # Tworzenie FloatLayout
        float_layout = FloatLayout(size_hint_y=None, height=200)
        for i in range(3):
            btn = Button(text=f'Float {i+1}', size_hint=(.2, .2), pos_hint={'x': i*0.3, 'y': 0.5})
            float_layout.add_widget(btn)

        # Dodawanie layoutów do g³ównego layoutu
        self.main_layout.add_widget(grid_layout)
        self.main_layout.add_widget(float_layout)
        return self.main_layout
    def on_button_press(self,instance,i):
        if self.board.allowed(i):
            self.board.set_arr(i,self.s)
            instance.text = self.s
            instance.disabled = True
            self.s = "x" if self.s == "o" else "o"
            self.l_gracz.text=f'Kolej {self.s}'
class Game_gui_back:
    def __init__(self,s,board,twoplayer,dif):
        self.board = board
        
        self.twoplayer = twoplayer
        self.dif = dif 
        self.playerone = None
        self.playertwo = None

    def start_multi(self):
        self.playerone = Player(self.board)
        self.playerone.set_sign()
        s = "x" if self.playerone.get_sign() == "o" else "o"
        self.playertwo = Player(self.board,s)
            
    def start_single(self):
        self.playerone = Player(self.board)
        self.playerone.set_sign()
        s = "x" if self.playerone.get_sign() == "o" else "o"
        self.playertwo = Player(self.board,s,human=False)


class Test1(App):
    def build(self):
        layout = RelativeLayout()

        # Tworzenie przycisku
        num=1
        button = Button(text="Kliknij mnie!",size_hint=(None, None), size=(100, 50))
        button1 = Button(text="Kliknij mnie!",size_hint=(None, None), size=(100, 50))
        button.bind(on_press=self.on_button_press) # Przypisanie funkcji do przycisku


        layout.add_widget(button)
        layout.add_widget(button1)
        return layout

    def on_button_press(self, instance):
        # Tutaj mo¿esz odczytaæ dane z przycisku
        print("Przycisk zostal!")
        print("Tekst przycisku to:", instance.text)

class Test2(App):
    def build(self):
        layout = BoxLayout()
        img = Image()
        button = Button(text="Kliknij mnie!",size_hint=(None, None), size=(100, 50))
        button1 = Button(text="Kliknij mnie!",size_hint=(None, None), size=(100, 50))
        button2 = Button(text="Kliknij mnie!")
        button.bind(on_press=self.on_button_press) # Przypisanie funkcji do przycisku


        layout.add_widget(button)
        layout.add_widget(button1)
        
        # Tworzenie prostego obrazu z pikseli
        texture = Texture.create(size=(1024, 1024))
        texture.blit_buffer(b'\xFF\xFF\xFF' * 1024 * 1024, colorfmt='rgb')
        img.texture = texture
        
        layout.add_widget(img)
        return layout
    def on_button_press(self, instance):
        # Tutaj mo¿esz odczytaæ dane z przycisku
        print("Przycisk zostal!")
        print("Tekst przycisku to:", instance.text)

class Test3(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Tworzenie CheckBox
        self.checkbox = CheckBox()
        self.checkbox.bind(active=self.on_checkbox_active)
        layout.add_widget(self.checkbox)

        # Etykieta do wyœwietlania stanu CheckBox
        self.label = Label(text="CheckBox is off")
        layout.add_widget(self.label)

        return layout

    def on_checkbox_active(self, checkbox, value):
        if value:
            self.twoplayer = False
        else:
            self.twoplayer = True
class RelativeLayoutExample(App):
    def build(self):
        layout = RelativeLayout()

        layout.add_widget(Button(text='Przycisk 1', size_hint=(.3, .3), pos_hint={'x': .1, 'y': .7}))
        layout.add_widget(Button(text='Przycisk 2', size_hint=(.3, .3), pos_hint={'x': .5, 'y': .7}))
        layout.add_widget(Button(text='Przycisk 3', size_hint=(.3, .3), pos_hint={'x': .1, 'y': .3}))

        return layout

class SliderApp(App):
    def build(self):
        # G³ówny uk³ad pionowy
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Etykieta, która bêdzie wyœwietla³a wartoœæ suwaka
        self.label = Label(text='Wartosc: 0', font_size=24, size_hint_y=None, height=50)
        layout.add_widget(self.label)
        
        # Tworzenie suwaka
        self.slider = Slider(min=0, max=100, value=0, step=1)
        self.slider.bind(value=self.on_value_change)
        layout.add_widget(self.slider)
        
        return layout

    def on_value_change(self, instance, value):
        # Aktualizacja tekstu etykiety w zale¿noœci od wartoœci suwaka
        self.label.text = f'Wartosc: {int(value)}'


    
if __name__ == '__main__':
    MainMenu().run()
    Game_gui_front().run()
    #Test1().run()#przyciski
    #Test2().run()#tekstura
    #Test3().run()#check box
    #RelativeLayoutExample().run()
    #SliderApp().run()


    