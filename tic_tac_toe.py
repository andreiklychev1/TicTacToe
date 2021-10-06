from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from kivy.uix.button import Button
from kivy.config import Config

Config.set("graphics","resizable","0")
Config.set("graphics","width","600")
Config.set("graphics","height","600")

choice = ['X', 'O']; switch = 0

class MainApp(App):

    def tic_tac_toe(self, arg):
        global switch

        arg.disabled = True
        arg.text = choice[switch]

        if not switch: switch = 1
        else: switch = 0

        coordinate = (
            (0,1,2,3),(4,5,6,7),(8,9,10,11),(12,13,14,15), # X
            (0,4,8,12),(1,5,9,13),(2,6,10,14),(3,6,11,15), # Y
            (0,5,10,15),(3,6,9,12),(4,9,14),(1,6,11),(2,5,8),(7,10,13)       # D
        )

        vector = (
            [self.button[x].text for x in (0,1,2,3)],
            [self.button[x].text for x in (4,5,6,7)],
            [self.button[x].text for x in (8,9,10,11)],
            [self.button[x].text for x in (12,13,14,15)],

            [self.button[y].text for y in (0,4,8,12)],
            [self.button[y].text for y in (1,5,9,13)],
            [self.button[y].text for y in (2,6,10,14)],
            [self.button[y].text for y in (3,6,11,15)],
                                           
            [self.button[d].text for d in (0,5,10,15)],
            [self.button[d].text for d in (3,6,9,12)],
            [self.button[d].text for d in (4,9,14)],
            [self.button[d].text for d in (1,6,11)],
            [self.button[d].text for d in (2,5,8)],
            [self.button[d].text for d in (7,10,13)]
        )

        win = False
        color = [0,1,0,1] # Green

        for index in range(14):
            if vector[index].count('X') == 3\
            or vector[index].count('O') == 3:
                win = True
                for i in coordinate[index]:
                    self.button[i].color = color
                break

        if win:
            for index in range(16):
                self.button[index].disabled = True
        
    def restart(self, arg):
        global switch; switch = 0
        for index in range(16):
            self.button[index].color = [1,0,0,1]
            self.button[index].text = ""
            self.button[index].disabled = False

    def build(self):
        self.title = "Крестики-нолики"
        
        root = BoxLayout(orientation = "vertical", padding = 5)

        grid = GridLayout(cols = 4)
        self.button = [0 for _ in range(16)]
        for index in range(16):
            self.button[index] = Button(
                    color = [1,0,1,1],
                    font_size = 64,
                    disabled = False,
                    on_press = self.tic_tac_toe
                )
            grid.add_widget(self.button[index])
        root.add_widget(grid)

        root.add_widget(
            Button(
                text = "Restart",
                size_hint = [1,.1],
                on_press = self.restart
            )
        )
        return root

if __name__ == "__main__":
    MainApp().run()