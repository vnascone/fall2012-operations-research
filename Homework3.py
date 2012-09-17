from networkClass import *

net = networkClass()
net.addNodes([1,2,3,4,5,6,7])
net.addArcs([
             [(1,2), 5],
             [(1,3), 14],
             [(1,4), 6],
             [(2,3), 6],
             [(2,5), 12],
             [(2,6), 12],
             [(3,5), 2],
             [(3,6), 3],
             [(4,3) ,7],
             [(4,6), 9],
             [(5,7), 4],
             [(6,7), 4]])
net.minCost()
net.maxCost()
net.getCutSets()
