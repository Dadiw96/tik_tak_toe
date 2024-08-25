from TreeN import Tree
from tik_tak_toe import Board
import random

   
#stworzyc klase vot z ktorej pozostale;klasy bot beda dziedziczyc methody a z kolei te metody beda uzywane w innych plikach np w grze         (stala bula;nazw;metod)    
                  
            
class Bot_beg:
    #bot na beg robi losowy ruch ale spr czy moze wygrac lub przegrac nastepnym ruchem  
    
    def __init__(self, s, board):
        self.s = s
        self.e = "x" if self.s == "o" else "o"
        self.board = board
        self.arr=[0,1,2,3,4,5,6,7,8]#tablica przechowuje wartosci pol ktore zostaja usuniete jesli ruch zostanie wykonany
   
    
    
    def arr_update(self):
        for i in self.arr:
            if not self.board.allowed(i):
                self.arr.remove(i)
                
    def sim_update(self, i, s):
        anwser = board.update(i,s)
        board.downgrade(i,s)
        return anwser
 
    def downgrade(self,i,s):
        val = -1 if s=="o" else 1
        row = i //  3#wiersze
        col = i %  3 #kolumny 
        self.scores ["row"][row] +=  val
        self.scores ["col"][col] +=  val
       
        if i in [0, 4, 8]:
            self.scores["diag"][0] += val
        if i in [2, 4, 6]:
            self.scores["diag"][1] += val
    def move(self):
       self.arr_update()
       for i in self.arr:
           if self.board.sim_update(i, self.s):
               return i
           elif self.board.sim_update(i,self.e):
               return i
           else: return random.choice(self.arr )
                  
       
     
     

class bot_minmax:
    pass
    '''
    #budowanie drzewa stanoa gry z uzyciem allowe
    
    #rozwiniecie poziomow trudnosci;za sprawa wybrania ilosci ruxhow do przodu ktore przewiduje bot dla np
    easy to 2
    medium 4 
    hard 6
    god cala gra 
    
    
    '''
    def minimax(self, node, depth, alpha, beta, is_maximizing):
    # Warunek końcowy (liść lub maksymalna głębokość)
        if not node.children or depth == 0:
            return node.value
    
        if is_maximizing:
            max_eval = float('-inf')
            for child in node.children:
                eval = self.minimax(child, depth - 1, alpha, beta, False)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break  # Beta cut-off
            return max_eval
    
        else:
            min_eval = float('inf')
            for child in node.children:
                eval = self.minimax(child, depth - 1, alpha, beta, True)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break  # Alpha cut-off
            return min_eval        
def main ():
         board = Board()
         board.b()
if __name__ == "__main__":
            main()
            