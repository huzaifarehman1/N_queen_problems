import heapq
import random

class board:
    
    def __init__(self,n):
        self.num_queens = n
        self.number = n #rows = column = number of queens
        self.board = [ ["" for i in range(n)] for j in range(n) ]
        self.positions = []
    
    def place_Queens(self,indexies:list,Randomized = False):
        """place Queen on the specified tile
        Randomized: if True, the placement is random
        indexies: list of tuples (row, column) where the queens should be placed   
        if Randomized is False, the queens are placed on the specified indexies
        if Randomized is True, the queens are placed randomly on the board
        """
        if not(Randomized):
            for i in indexies:
                r,c = i
                self.board[r][c] = "Q"
                self.positions.append((r,c))
        
        else:
            choiceR = set()
            choiceC = set()
            for i in range(self.number):
                choiceC.add(i)
                choiceR.add(i)
            for i in range(self.number):    
                r = random.choice(choiceR)
                choiceR.remove(r)
                c = random.choice(choiceC)
                choiceC.remove(c)
                self.board[r][c] = "Q"
                self.positions.append((r,c))
        return None    
    
    def calculator(self,num):
        temp = num - 1
        return int((1+temp)*(temp/2))
    
    def state_score(self):
        """The admirability of a state(lower the better)"""
        # 0 for the solution
        # work by counting check of all pieces to all pieces 
        total_score = 0
        R_counter = {}
        C_counter = {}
        MD_counter = {}
        AD_counter = {}
        for i in range(self.number):
            r,c = self.positions[i]
            if r not in R_counter:
                R_counter[r] = 1
            else:
                R_counter[r] += 1 
                
            if c not in C_counter:
                C_counter[c] = 1
            else:
                C_counter[c] += 1       
                
            Main_diagonal_entry = r - c
            if Main_diagonal_entry not in MD_counter:
                MD_counter[Main_diagonal_entry] = 1     
            else:
                MD_counter[Main_diagonal_entry] += 1
            
            AD_entry = r + c
            if AD_entry not in AD_counter:
                AD_counter[AD_entry] = 1     
            else:
                AD_counter[AD_entry] += 1
        
        for k,v in R_counter.items():
            R_score = self.calculator(v)  
            total_score +=  R_score
        
        for k,v in C_counter.items():
            C_score = self.calculator(v)   
            total_score +=  C_score 
        
        for k,v in MD_counter.items():
            MD_score = self.calculator(v)  
            total_score +=  MD_score
        
        for k,v in AD_counter.items():
            AD_score = self.calculator(v)   
            total_score +=  AD_score 
        
        return total_score

class storage:
    def __init__(self,size):
        """
            store best k nodes (lowest value)
        Args:
            size (int): k / size of the storage
        """
        self.size = size
        self.count = 0
        self.arr = []
    
    def is_full(self):
        return self.count>=self.size
    
    def is_empty(self):
        return self.count<=0  
    
    def push(self,container):
        if self.is_full():
            pass
            
    
    def pop(self):
        if self.is_empty():
            raise Exception("EMPTY!!")
        
        

def Solver(n):
    pass    

if __name__ == "__main__":
    pass