class board:
    
    def __init__(self,n):
        self.num_queens = n
        self.number = n #rows = column = number of queens
        self.positions = []
    
    def add_positions(self,indexies:list):
    
        for i in indexies:
            self.positions.append(i)
        
        return None    
    
    def state_score(self):
        pass

