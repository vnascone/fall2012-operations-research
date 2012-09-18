from pulp import *

def getNetForCost(cost):
  # List the nodes
  nodes = [1, 2, 3, 4, 5, 6, 7]
  
  # List the arcs
  arcs = [(1,2),
          (1,4),
          (1,3),
          (2,5),
          (2,4),
          (3,4),
          (3,6),
          (4,5),
          (4,7),
          (4,6),
          (5,7),
          (6,7)]
  
  # List the arc weights (SAME ORDER)
  weights = [16,
             35,
             9,
             25,
             12,
             15,
             22,
             14,
             19,
             17,
             8,
             14]
  
  # Create structure for easy searching in case we need it
  data = dict(zip(arcs, weights))
  
  # Generate the basic model variables, since it is binary we can use min=0 max=1 and the integer solver
  vars = LpVariable.dicts("arc", arcs, 0, 1, LpInteger)
  
  # Create the model variable to contain the data
  model = LpProblem("Network Flow Minimization", LpMinimize)
      
  # Create the objective function
  model += lpSum([vars[a] * data[a] for a in arcs]), "Total Distance"
  
  # Constraints for Node 1
  model += (vars[(1,2)] + vars[(1,3)] + vars[(1,4)] == 1), "Conservation for Node 1"
  
  # Constraints for Node 7
  model += (vars[(5,7)] + vars[(4,7)] + vars[(6,7)] == 1), "Conservation for Node 7"
  
  # Constraints for remaining nodes
  for n in nodes:
    if n != 1 and n!=7:
      model += (lpSum([vars[(i,j)] for (i,j) in arcs if j == n]) == lpSum([vars[(i,j)] for (i,j) in arcs if i == n])), "Conservation for Node %s"%n
  
  # Constraints accounting for unit cost at each arc
  model += (lpSum([vars[(i,j)] for (i,j) in arcs]) == cost), "Constraint for Arc Unit Cost"
  
  # Write the problem to an lp file
  model.writeLP("HW2.lp")
  
  # Solve the problem
  model.solve()
  
  # Print the model status
  print "Status:", LpStatus[model.status]
  
  # Print each variable with its optimum value
  for v in model.variables():
    print v.name, "=", v.varValue
  
  # Finally print the minimal distance as found by the model
  print "Total Distance = ", value(model.objective)
  print model.constraints['Constraint_for_Arc_Unit_Cost'].pi
