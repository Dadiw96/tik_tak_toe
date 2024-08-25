from boty_tik_tak_toe import *
from TreeN import Tree
from tik_tak_toe import Board

#funkcja menu ktora spina program i nim;zarzadza 

class Menu:
    def __init__(self):
        self.twoplayer = True
        self.bot = None
        self.t =None
        self.dificulty = None
        
    def mainMenu(self):
        #r=board_size()
        self.tryb()
        if not self.twoplayer: 
            self.set_dificulty()
           
           
           
    
    def board_size(self):
        pass
        
    def tryb(self):
        i = int(input(" 1 single \n 2 multi"))
        if i == 2:
            self.twoplayer = True
        elif i == 1: self.twoplayer = False 
             
    
    def set_dificulty(self):
        #i = int(input("Poziom Trudnosci "))
        i=0
        self.dificulty = i
        
class Game(Menu):
        def __init__(self):
                    super().__init__()
                    self.board = Board()
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
            elif not self.twoplayer:
                   self.start_single()
                   d = self.dificulty
                   if d == 0:bot = Bot_beg(self.playertwo.get_sign,self.board)
                   #elif:
                    
                   self.playertwo.bot = bot
            self.middle()   
                   
                   
                   
        def middle(self):
                   move = 0
                   while True:
                       if  move == 9 or self.playerone.move():
                           break
                       move+=1    
                       if move == 9 or self.playertwo.move():
                           break
                       move+=1
                   if move == 9:
                      print("Remis")                
                    
                    
                   
                   
    
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
    
    def move_human(self):
        s = self.sign
        i = self.inp()  
        if self.board.allowed(i,s):
            self.board.set_arr(i,s)
            self.board.b(i,s)
            if self.board.update(i,s):
                  print(s,"is Winner")
                  return True             
        else:
            print("Pole zajete\n")
        return False
        
    def inp(self):
        
        while True:
            w=input(f"Podaj pozycje dla {self.sign} ")
            if  not w.isdigit():
                print("Wrong input pls type (0-8)")
            elif(int(w) not in range (9)):
                print("Wrong input pls type (0-8)")
            else:    
                return int(w)
    def move_bot(self):
        s = self.sign
        i = self.bot.move()
        if self.board.allowed(i,s):
            self.board.set_arr(i,s)
            self.board.b(i,s)
            if self.board.update(i,s):
                  print(s,"is Winner")
                  return True                  
        else:
            print("Pole zajete\n")
        return False
                  
    def move(self):
        if self.is_human: 
            return self.move_human()
        elif not self.is_human:
            return self.move_bot()
      
 
        
    
                         
                    
                    
                    
                    
        
        
def main():
    gra= Game()
    gra.start()
    
if __name__ == "__main__":
    main()