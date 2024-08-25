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
        #os.system('clear')  
        os.system('cls')             
                  
    
        
                  
                  
                  
                   
                   
                       
                     
           
           
def main():               
    board = Board()
    board.b()
    
if __name__ == "__main__":
    main()