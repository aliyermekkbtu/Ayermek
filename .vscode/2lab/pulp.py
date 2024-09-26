from pulp import LpMaximize, LpProblem, LpVariable, value

problem = LpProblem("Maximize", LpMaximize)

x1 = LpVariable('x1', lowBound=0) 
x2 = LpVariable('x2', lowBound=0) 
x3 = LpVariable('x3', lowBound=0)

problem += 30 * x1 + 20 * x2 + 10 * x3 

problem += 2 * x1 +  x2  <= 100
problem += x1 + 2 * x2   <= 80


problem.solve()


print("x1 =", value(x1))
print("x2 =", value(x2))
print("Max =", value(problem.objective))