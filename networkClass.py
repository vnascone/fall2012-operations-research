#!/usr/bin/python
# A project by Vincent Nascone for the Fall 2012 EM 457 Class
# This will serve as a class to help solve network problems during the semester
# If used in homework problems I'll include the source code as part of the work for the problem

from pulp import *

class networkClass(object):
  def __init__(self, nodes = [], arcs = [], weights = [], cutsets=[]):
    self.nodes = nodes
    self.arcs = arcs
    self.weights = weights
    self.cutsets = cutsets

# Function to add the nodes in the graph problem
  def addNode(self, node):
    self.nodes.append(node)

# Function to add the arcs or edges in the graph problem
# Should be used in the format addArc((source, destination), weight)
  def addArc(self, arc, weight):
    self.arcs.append(arc)
    self.weights.append(weight)

# Function to add multiple nodes at once
  def addNodes(self, unodes):
    for node in unodes:
      self.addNode(node)

# Function to add multiple arcs at once
# To be added in the format of addArcs([[(source1, destination1), weight1], [(source2, destination2), weight2], [(sourceN, destinationN), weightN]]
  def addArcs(self, uarcs):
    for arc in uarcs:
      self.addArc(arc[0], arc[1])

# Function to solve the created graph for the minimal cost, i.e. getting from source (first node in the array) to destination (last node in the array) minimizing the total cost (sum of the weight of each arc)
  def optimizeNet(self, maxormin):
  
    # Create a variable to store our method to search for weight given the arc
    data = dict(zip(self.arcs, self.weights))
    
    # Generate the basic model variables, since it is binary we can use min=0 and max=1
    vars = LpVariable.dicts("arc", self.arcs, 0, 1, LpInteger)

    # Create the model variable to contain our linear programming problem
    if maxormin == 'max':
      model = LpProblem("Network Cost Maximization", LpMaximize)
    elif maxormin == 'min':
      model = LpProblem("Network Cost Minimization", LpMinimize)

    # Create the objective function
    model += lpSum([vars[a] * data[a] for a in self.arcs]), "Total Cost"

    # Constraints for the first node
    model += (lpSum([vars[(i,j)] for (i,j) in self.arcs if i == self.nodes[0] ]) == 1), "Conservation for Node 1"

    # Constraints for the final node
    model += (lpSum([vars[(i,j)] for (i,j) in self.arcs if j == self.nodes[-1] ]) == 1), "Conservation for Node %s"%self.nodes[-1]

    # Constraints for the remaining nodes
    for n in self.nodes:
      if n != self.nodes[0] and n!= self.nodes[-1]:
        model += (lpSum([vars[(i,j)] for (i,j) in self.arcs if j == n]) == lpSum([vars[(i,j)] for (i,j) in self.arcs if i == n])), "Conservation for Node %s"%n

    # Solve the problem
    model.solve()

    # Print the model status
    print "Status:" , LpStatus[model.status]

    # Print the arcs that we chose
    for v in model.variables():
      if v.varValue == 1.0:
        print v.name

    # Finally print the optimum distance as found by the model:
    print "Total Cost = ", value(model.objective)

  def minCost(self):
    self.optimizeNet('min')

  def maxCost(self):
    self.optimizeNet('max')

  def getDirectPredecessor(self, arc):
    ret = [(i,j) for (i,j) in self.arcs if j == arc[0]]
    return ret

  # Function to
  def cutSetHelper(self, cut):
    pre = {}
    ret = []
    temp = []
    cut2=[]
    
    # Iterate over each member of a cutset to find its direct predecessors
    for set in cut:
      for a in set:
        q = self.getDirectPredecessor(a)
        if len(q) > 0:
          pre[a] = q

    # Create a Set of possible cutsets
    for set in cut:
      for a in set:
        if a in pre:
          temp = []
          for b in set:
            if a != b:
              temp.append(b)
              for q in pre[a]:
                if q not in temp:
                  temp.append(q)
          cut2.append(temp)

    # Ensure only 
    for c in cut2:
      if c not in self.cutsets:
        checki=[]
        checkj=[]
        doit = True
        for i,j in c:
          checki.append(i)
          checkj.append(j)
        for i in checki:
          if i in checkj:
            doit = False
        if doit:
          ret.append(c)
          self.cutsets.append(c)
    return ret

  def getCutSets(self):
    cut = []
    cut.append([(i,j) for (i,j) in self.arcs if j == self.nodes[-1]])
    self.cutsets = cut

    while(cut != []):
      cut = self.cutSetHelper(cut)

    return self.cutsets
