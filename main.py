import random

class board:
    
    def __init__(self,n):
        self.num_queens = n
        self.number = n #rows = column = number of queens
        
        self.positions = [-1]*n # no queen at any column and row | self.positions[i] = j means i column and j row
    
    def place_Queens(self,indexies:set,Randomized = False):
        """place Queen on the specified tile
        Randomized: if True, the placement is random
        indexies: list[int] — list where index = column, value = row  
        if Randomized is False, the queens are placed on the specified indexies
        if Randomized is True, the queens are placed randomly on the board
        """
        if not(Randomized):
            for c,r in enumerate(indexies):
                self.positions[c] = r
        
        else:
            rows = list(range(self.number))
            random.shuffle(rows)
            for c in range(self.number):
                r = rows[c]
                self.positions[c] = r
                    
        return None    
    
    def calculator(self,num):
        temp = num - 1
        return int((1+temp)*(temp/2))
    
    def state_score(self):
        """The admirability of a state(lower the better)"""
        # 0 for the solution
        # work by counting check of all pieces to all pieces 
        total_score = 0
        MD_counter = {}
        AD_counter = {}
        for c,r in enumerate(self.positions):   
                
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
        
        
        for k,v in MD_counter.items():
            MD_score = self.calculator(v)  
            total_score +=  MD_score
        
        for k,v in AD_counter.items():
            AD_score = self.calculator(v)   
            total_score +=  AD_score 
        
        return total_score


    def create_ALL_neighbours(self):
        """
        Create all neighbours of the current state as a list

        Returns:
            [board objects] (list): a list containing all neighbours as board object 
        """
        lis = []
        
        for c,r in enumerate(self.positions):
            for j in range(c + 1,self.number):
                Nc = j
                Nr = self.positions[j]
                
                temp = board(self.number)
                newPositions = self.positions[::]
                newPositions[c],newPositions[Nc] = newPositions[Nc],newPositions[c]
                temp.place_Queens(newPositions)        
                lis.append(temp)
                    
                    
        
        return lis

    def __hash__(self):
        return hash(tuple(self.positions))
    
    def print(self):
        self.board = [ ["" for i in range(self.number)] for j in range(self.number) ]
        for c,r in enumerate(self.positions):
             if r!=-1:
                 self.board[r][c] = "Q"
        for i in self.board:
            print(i)
        with open("answer.txt","w") as f:
            f.write(str(self.board[0])+ "\n")
            
        with open("answer.txt","a") as f:    
            for i in range(1,self.number):
                f.write(str(self.board[i]) + "\n")    
        return
    
    def __lt__(self,other):
        return True
    
    def __eq__(self, other):
        if isinstance(other, board):
            return  set(self.positions) == set(other.positions)
        return False
    

        
        
        

def Solver(n):
        res = 0
        if n<=3:
            print("No solution found")
            return 
        state_seen = 0
        max_ = float("inf")
        
        while True:
                res += 1
           
                Board_ = board(n)
                Board_.place_Queens([],True)
                
                score = Board_.state_score()
                if score<max_:
                    max_ = score
                    print(f"Best start till now have {max_} score")
                else:
                    continue    
           
              
            
           
                state_seen += 1
                ele: board
                score: int
                ele = Board_
                
                # start hill climbing 
                flag = True
                best = score
                curr = ele
                while flag:
                    flag = False
                    if best <= 0: # found solution
                        curr.print()
                        print(f"Found solution in {state_seen} states and {res} restarts (first included)" )
                        return state_seen
                    
                    neighbours = curr.create_ALL_neighbours()
                    i:board
                    for i in neighbours:
                            state_seen += 1
                            score = i.state_score()
                            if score<best:
                                flag = True
                                best = score
                                curr = i
                            
                
            

def take_input():
    while True:
        try:
            x = int(input("Enter the number (n) of Queens: "))
        except ValueError :
            print("only integers allowed")
            continue
        except Exception as e:
            print(e)
            print("something went wrong")
            continue
            
        else:    
            if x<=0:
                print("x must be >= 1")
                continue
            return x

if __name__ == "__main__":
    n = take_input()
    Solver(n)   