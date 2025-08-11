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
            choiceR = list(range(self.number))
            
            for i in range(self.number):
                r = random.choice(choiceR)
                choiceR.remove(r)
                
                c = i
                
                self.board[r][c] = "Q"
                self.positions.append((r, c))
        
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


    def create_ALL_neighbours(self):
        """
        Create all neighbours of the current state as a list

        Returns:
            [board objects] (list): a list containing all neighbours as board object 
        """
        lis = []
        
        for r,c in self.positions:
            possible = [
                # Vertical (up, down)
                (r-1, c),  # up
                (r+1, c),  # down

                # Horizontal (left, right)
                (r, c-1),  # left
                (r, c+1),  # right

                # Diagonals
                (r-1, c-1),  # up-left
                (r-1, c+1),  # up-right
                (r+1, c-1),  # down-left
                (r+1, c+1)   # down-right
            ]
            for Nr,Nc in possible:
                
                if Nr<0:
                    continue
                if Nc<0:
                    continue
                
                if Nr>=self.number:
                    continue
                if Nc >= self.number:
                    continue
                
                if self.board[Nr][Nc]=="Q":
                    continue
                
                temp = board(self.number)
                newPositions = []
                for i in self.positions:
                    if (r,c)==(i[0],i[1]):
                        temp.place_Queens([(Nr,Nc)])
                    else:
                        temp.place_Queens([i])
                lis.append(temp)            
                    
        
        return lis

    def __hash__(self):
        return hash(tuple(self.positions))
    
    def print(self):
        for i in self.board:
            print(i)
        return
    
    def __lt__(self,other):
        return True
    
    def __eq__(self, other):
        if isinstance(other, board):
            return  set(self.positions) == set(other.positions)
        return False
    
        
    
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
        self.max = 0

    def is_full(self):
        return self.count>=self.size
    
    def is_empty(self):
        return self.count<=0  
    
    def push(self,Board:board,score):
        flag = False
        if self.is_full(): 
            if score>self.max:
                return False
            m = max(self.arr,key = lambda x : x[0])
            self.arr.remove(m)
            flag = True
            
        tup = (score,Board)
        if score>self.max and not(flag):
            self.max = score    
        # we dont want any bad neighbours
        heapq.heappush(self.arr,tup)
        if not flag:
            self.count += 1
        if flag:
            self.max = max(self.arr, key = lambda x: x)[0]
            
    
    def pop(self):
        if self.is_empty():
            raise Exception("EMPTY!!")
        self.count -= 1
        tup = heapq.heappop(self.arr)
        return tup
        
        
        

def Solver(n):
        if n<=3:
            print("No solution found")
            return 
        state_seen = 0
        seen = set()
        frontier = storage(n)
        while True:
           
           Board_ = board(n)
           Board_.place_Queens([],True)
           
           
           if Board_ in seen:
                continue
           seen.add(Board_)
           frontier.push(Board_,Board_.state_score())
           if not(frontier.is_full()):
                continue # add till frontier is full    
            
           while not(frontier.is_empty()):
                state_seen += 1
                ele: board
                score: int
                score,ele = frontier.pop()
                
                # start hill climbing 
                flag = True
                best = score
                curr = ele
                while flag:
                    flag = False
                    if best <= 0: # found solution
                        print(f"Found solution in {state_seen} states")
                        curr.print()
                        return state_seen
                    
                    neighbours = ele.create_ALL_neighbours()
                    i:board
                    for i in neighbours:
                        if i not in seen:
                            seen.add(i)
                            score = i.state_score()
                            if score<best:
                                frontier.push(i,score)
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