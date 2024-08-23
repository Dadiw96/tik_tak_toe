#tik tak toe 
#bot;napisany chciwym argorytmem

import os
#from boty_tik_tak_toe import *
class Board:
    def __init__(self):
        self.h = "_"
        self.v = "|"
        self.arr=[" " for _ in range(9)] 
        self.scores = { "row":[0,0,0], "col":[0,0,0], "diag":[0,0]} 
        
    def b(self, i=None, s=None):
        v=self.v
        arr=self.arr
        top= [f"{arr[0]} {v} {arr[1]} {v} {arr[2]}"]
        mid= [f"{arr[3]} {v} {arr[4]} {v} {arr[5]}"]
        bot= [f"{arr[6]} {v} {arr[7]} {v} {arr[8]}"]
        line=(self.h*13)
        b=(top,line,mid,line,bot)
        self.draw(b)
        #return top,line,mid,bot
        
    def draw(self,b):
        self.clear()
        for line in b:
            print(line)
        
    #def inp(self,s="o"):
#        while True:
#            w=input(f"Podaj pozycje dla {s} ")
#            if  not w.isdigit():
#                print("Wrong input pls type (0-8)")
#            elif(int(w) not in range (9)):
#                print("Wrong input pls type (0-8)")
#            else:    
#                return int(w)
#    def player(self,s):
#         i = self.inp(s)   
#         if self.allowed(i,s):
#             self.arr[i]=s
#             self.b(i,s)
#             if self.update(i,s):
#                   print(s,"is Winner")
#                   return True
#             
#         else:
#             print("Pole zajete\n")
#         return False 
#          
#            
#    def o(self,player = True):
#        s="o"
#        if player:
#           return self.player(s)
#           
#        
#           
#           
#    def x(self,player = True):
#        s="x"
#        if player:
#            return self.player(s)
#        else:
            
 #trzeba to przepisac tak by if byl uzyty tylko raz moze stworzyc funkcje menu ktora spr to raz i potem obsluguje sie to zmieniajac poprostu przypisanie do zmiennej w liscie  sa mozliwosci a przypisuje konkretna wartosc do zmiennej i to dziala wywolujac funkcje game z:parametrami
    def set_arr(i,s):
        self.arr[i] = s
        
    def allowed(self,i,s):
           return self.arr[i] ==" "
    def update(self,i,s):
        val = 1 if s=="o" else -1
        row = i //  3#wiersze
        col = i %  3 #kolumny 
        self.scores ["row"][row] +=  val
        self.scores ["col"][col] +=  val
       
        if i in [0, 4, 8]:
            self.scores["diag"][0] += val
        if i in [2, 4, 6]:
            self.scores["diag"][1] += val
    
    # Sprawdzenie, czy którakolwiek z wartości osiągnęła 3 lub -3
        if 3 in self.scores["row"] or 3 in self.scores["col"] or 3 in self.scores["diag"]:
            return True
        if -3 in self.scores["row"] or -3 in self.scores["col"] or -3 in self.scores["diag"]:
            return True
        return False
                  
    def clear(self):
                  os.system('clear')              
                  
    
        
                  
                  
                  
                   
                   
                       
                     
           
           
def main():               
    board = Board()
    board.game()
    
if __name__ == "__main__":
    main()