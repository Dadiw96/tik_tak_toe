import os
import random
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
class Menu:
    def __init__(self):
        self.twoplayer = True
        self.dificulty = None
        
    def mainMenu(self):
        self.tryb()
        self.board = Board(self.board_size())
        if not self.twoplayer: 
            self.set_dificulty()      
        
    def board_size(self):
        return  self.check("Podaj rozmiar planszy od 3 do 10\n",10,3)
        
    def tryb(self):
        i = self.check(" 1 single \n 2 multi",2,1)
        if i == 2:
            self.twoplayer = True
        elif i == 1: self.twoplayer = False 
             
    def set_dificulty(self):
        i = self.check(f"Poziom Trudnosci maks {self.board.r*self.board.r}\n",self.board.r*self.board.r,0)
        self.dificulty = i 
    def check(self,message,max,min=0):
        while True:
            print(f"{message}")
            w = input()
            if  not w.isdigit():
                print(f"Podaj wartosc w zakresie od {min} do {max}")
            elif(int(w) not in range (min,max)):
                print(f"Podaj wartosc w zakresie od {min} do {max}")
            else:    
                return int(w)
class Game(Menu):
    def __init__(self):
        super().__init__()
        self.board = None
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
            
            
            
    def start(self):
        
        self.mainMenu()
        if self.twoplayer:
            self.start_multi()
        else:
            self.start_single()
            d = self.dificulty
            if d == 0:bot = Bot_beg(self.playertwo.get_sign(),self.board)
            else: bot = Bot_mm(self.playertwo.get_sign(),self.board,d)
                    
        self.playertwo.bot = bot
        self.end(self.middle())   
                   
                   
                   
    def middle(self):
        move = 0
        while True:
            if  move == 9 or self.playerone.move():
                return self.playerone.get_sign()
            move+=1    
            if move == 9 or self.playertwo.move():
                return self.playertwo.get_sign()
            move+=1
            if move == 9:
                self.end(None)
    def end(self,winner):
        if winner == None:
            print("Remis")
        else:
            print("Wygral: ",winner)
class Player:
    def __init__(self,board,sign = None, human = True, bot = None):
        self.sign = sign 
        self.is_human = human
        self.board = board
        self.bot = bot
        
    def set_sign(self):
         self.sign = input("o lub x ")
    def get_sign(self):
        return self.sign
    def get_is_human(self):
        return self.is_human
        
    def inp(self):
        
        while True:
            w = input(f"Podaj pozycje dla {self.sign} ")
            if  not w.isdigit():
                print(f"Wrong input pls type (0-{(self.board.r*self.board.r)-1})")
            elif(int(w) not in range (self.board.r-1)):
                print(f"Wrong input pls type (0-{(self.board.r*self.board.r)-1})")
            else:    
                return int(w)
    def move(self):
        s = self.sign
        if self.is_human: 
            i = self.inp()  
        else: 
            i = self.bot.move()
        if self.board.allowed(i):
            self.board.set_arr(i,s)
            self.board.b(i,s)
            if self.board.update(i,s):
                  return True             
        else:
            print("Pole zajete\n")
            self.move()
        return False
class Board:
    def __init__(self,r=3):
        self.r = r#rozmiar tablicy
        self.h = "_" * (self.r * 4 - 1) 
        self.v = "|"
        
        self.arr=[" " for _ in range(self.r * self.r )] 
        self.scores = { "row":[0]*self.r , "col":[0]*self.r , "diag":[0,0]}
        self.diag=[[(self.r +1) * (n) for n in range(self.r )],
                   [(self.r -1) * (n + 1) for n in range(self.r)]]
        
    def b(self, i=None, s=None):
        v=self.v
        arr=self.arr
        b = []
        for row in range(self.r):
            line_content = f" {arr[row * self.r]} "
            for col in range(1, self.r):
                line_content += f"{v} {arr[row * self.r + col]} "
            b.append(line_content)
            if row < self.r - 1:  # Dodaj liniê poziom¹ pomiêdzy wierszami
                b.append(self.h)
        self.draw(b)
        
    def draw(self,b):
        self.clear()
        for line in b:
            print(line)
        print(" ")
 
    def set_arr(self,i,s):
        self.arr[i] = s
        
    def allowed(self,i):
           return self.arr[i] == " "
    
    def update(self,i,s):
        r = self.r
        val = 1 if s=="o" else -1
        row = i //r#wiersze
        col = i % r #kolumny 
        self.scores ["row"][row] +=  val
        self.scores ["col"][col] +=  val
       
        if i in self.diag[0]:
            self.scores["diag"][0] += val
        if i in self.diag[1]:
            self.scores["diag"][1] += val
    
    # Sprawdzenie, czy którakolwiek z wartoœci osi¹gnê³a r lub -r
        if r in self.scores["row"] or r in self.scores["col"] or r in self.scores["diag"]:
            return True
        if -r in self.scores["row"] or -r in self.scores["col"] or -r in self.scores["diag"]:
            return True
        return False
    
    def downgrade(self,i,s):
       r = self.r
       val = -1 if s=="o" else 1
       row = i // r#wiersze
       col = i % r #kolumny 
       self.scores ["row"][row] +=  val
       self.scores ["col"][col] +=  val
       
       if i in self.diag[0]:
           self.scores["diag"][0] += val
       if i in self.diag[1]:
           self.scores["diag"][1] += val              
   
    def clear(self):       
        if os.name == 'nt':  
            os.system('cls')#win
        else: 
            os.system('clear')
class Node:
    def __init__(self, value=None, myparent = None):
        self.value = value
        self.children = []
        self.myparent = myparent
class Bot_beg:
    #bot na beg robi losowy ruch ale spr czy moze wygrac lub przegrac nastepnym ruchem  
    
    def __init__(self, s, board):
        self.s = s#twój znak
        self.e = "x" if self.s == "o" else "o"#znak przeciwnika
        self.board = board#plansza
        self.arr=[i for i in range(board.r * board.r)] #tablica przechowuje wartosci pol ktore zostaja usuniete jesli ruch zostanie wykonany
   
    
    
    def arr_update(self):#zmienia wewnêtrzn¹ tablicê/planszê bota poprzez urzycie self.board.allowed i usuniêcie wartoœci z tablicy
        for i in self.arr:
            if not self.board.allowed(i):
                self.arr.remove(i)
                
    def sim_update(self, i, s):#==> BOOL True jeœli mo¿esz wygraæ/przegraæ w nastêpnym ruchu u¿ywa funkcji spr czy ktoœ jest zwyciêzc¹ by spr który ruch wykonaæ
        anwser = self.board.update(i,s)
        self.board.downgrade(i,s)#cofa zmiany w self.board.scores
        return anwser
 
   
    def move(self):#++>INT zwraca index na który nale¿y postawiæ symbol i spr czy patrz sim_upload
       self.arr_update()
       for i in self.arr:
           if self.sim_update(i, self.s):
               return i
           elif self.sim_update(i,self.e):
               return i
       return random.choice(self.arr )
class Bot_mm:
    def __init__(self, s, board, depth=4):
        self.s = s
        self.e = "x" if self.s == "o" else "o"
        self.board = board
        self.max_depth = depth
    
    def minimax(self, node, depth, alpha, beta, is_maximizing):
        if self.board.update(node.move, self.s if is_maximizing else self.e):
            return 1 if is_maximizing else -1
        if depth == 0 or not any(self.board.allowed(i) for i in range(len(self.board.arr))):
            return 0
    
        if is_maximizing:
            max_eval = float('-inf')
            for i in range(self.board.r*self.board.r):
                if self.board.allowed(i):
                    child = Node(i, parent=node)
                    node.children.append(child)
                    eval = self.minimax(child, depth - 1, alpha, beta, False)
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
            return max_eval
    
        else:
            min_eval = float('inf')
            for i in range(self.board.r*self.board.r):
                if self.board.allowed(i):
                    child = Node(i, parent=node)
                    node.children.append(child)
                    eval = self.minimax(child, depth - 1, alpha, beta, True)
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
            return min_eval
    
    def move(self):
        root = Node(None)
        best_value = float('-inf')
        best_move = None
        for i in range(self.board.r*self.board.r):
            if self.board.allowed(i):
                node = Node(i, parent=root)
                value = self.minimax(node, self.max_depth, float('-inf'), float('inf'), True)
                if value > best_value:
                    best_value = value
                    best_move = i
        return best_move
class Game_gui_back:
    def __init__(self,r,twoplayer,dif):
        self.board = Board(r)
        self.playerone = None
        self.playertwo = None
        self.twoplayer = twoplayer
        self.dif = dif

def testowa():
    board=Board(5)
    print(board.arr)
    print(board.scores)
    print(board.diag)
    board.b()  
#def testowagui():
    
    
def main():
    gra = Game()
    board=Board()
    #gra.start()
    Gui(gra).run()
    #testowagui()
    
if __name__ == "__main__":
    main()