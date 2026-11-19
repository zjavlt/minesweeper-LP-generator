import pulp as plp
from typing import List

class Model(object):
    def __init__(self, n, m):
        self.board = [['.' for _ in range(m)] for _ in range(n)]
        print(self)
    
    def parse(self, values: List[List[plp.LpVariable]], neighbors: List[List[plp.LpVariable]]):
        for row_index, row in enumerate(values):
            for col_index, col in enumerate(row):
                if col.varValue:
                    self.board[row_index][col_index] = '*'
        for row_index, row in enumerate(neighbors):
            for col_index, col in enumerate(row):
                if self.board[row_index][col_index] == '.' and col.varValue:
                    print(col.varValue)
                    self.board[row_index][col_index] = str(int(col.varValue))
                
        
    def __str__(self):
        total = ""
        for i in self.board:
            total += " ".join(i)
            total += "\n"
        return total

if __name__ == "__main__":
    model = Model(3, 4)
    print(model)