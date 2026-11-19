from pulp import *
from parser import Model
from calculator import *
import random
from view import project_contours

prob = LpProblem(name="Minesweeper", sense=LpMaximize)
peaks = []

n, m = (16, 30)
num_mines = 99

steep_rate = 3

peak_num = 9

for i in range(peak_num):
    x = random.randint(0, m-1)
    y = random.randint(0, n-1)
    peaks.append((y, x))

X = [[prob.add_variable(name=f"X_{i}_{j}", cat=LpBinary) for j in range(m)] for i in range(n)]

C = [[prob.add_variable(name=f"C_{i}_{j}", lowBound=0, cat=LpContinuous) for j in range(m)] for i in range(n)]
score = [[0 for j in range(m)] for i in range(n)]

f = prob.add_variable(name="max", lowBound=0, cat=LpContinuous)
for i in range(n):
    for j in range(m):
        exp = 0
        score[i][j] = calculate_score(node=(i, j), peaks=peaks, rate=steep_rate)
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                ny = i + dy
                nx = j + dx
                if ny < 0 or ny >= n or nx < 0 or nx >= m: continue
                exp += X[ny][nx]
        prob.addConstraint(constraint=C[i][j] == exp)
        prob.addConstraint(constraint=f >= C[i][j])
prob.addConstraint(f <= 4)
prob.addConstraint(lpSum(lpSum(X)) == num_mines)

for row in range(n):
    prob.addConstraint(constraint=lpSum(X[row]) <= n/2)

for col in range(m):
    exp = 0
    for i in range(n):
        exp += X[i][col]
    prob.addConstraint(constraint=exp <= m/2)
obj = 0
for i in range(n):
    for j in range(m):
        obj += score[i][j] * X[i][j]
prob.setObjective(obj=obj)
prob.solve()
print(prob)
model = Model(n, m)
model.parse(X, C)
print(X)

for y, x in peaks:
    model.board[y][x] = 'P'
print(model)

# project_contours(costs=score, board=model.board)

print(LpStatus[prob.status])

# print(prob.constraints())