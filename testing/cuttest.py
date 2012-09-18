from networkClass import *

net = networkClass()
net.addNodes([1,2,3,4])
net.addArcs([[(1,2), 16], [(1,3), 9], [(3,2), 5], [(2,4), 11], [(3,4), 15]])
net.getCutSets()
