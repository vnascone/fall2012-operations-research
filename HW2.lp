\* Network Flow Minimization *\
Minimize
Total_Distance: 16 arc_(1,_2) + 9 arc_(1,_3) + 35 arc_(1,_4) + 12 arc_(2,_4)
 + 25 arc_(2,_5) + 15 arc_(3,_4) + 22 arc_(3,_6) + 14 arc_(4,_5)
 + 17 arc_(4,_6) + 19 arc_(4,_7) + 8 arc_(5,_7) + 14 arc_(6,_7)
Subject To
Conservation_for_Node_1: arc_(1,_2) + arc_(1,_3) + arc_(1,_4) = 1
Conservation_for_Node_2: arc_(1,_2) - arc_(2,_4) - arc_(2,_5) = 0
Conservation_for_Node_3: arc_(1,_3) - arc_(3,_4) - arc_(3,_6) = 0
Conservation_for_Node_4: arc_(1,_4) + arc_(2,_4) + arc_(3,_4) - arc_(4,_5)
 - arc_(4,_6) - arc_(4,_7) = 0
Conservation_for_Node_5: arc_(2,_5) + arc_(4,_5) - arc_(5,_7) = 0
Conservation_for_Node_6: arc_(3,_6) + arc_(4,_6) - arc_(6,_7) = 0
Conservation_for_Node_7: arc_(4,_7) + arc_(5,_7) + arc_(6,_7) = 1
Constraint_for_Arc_Unit_Cost: arc_(1,_2) + arc_(1,_3) + arc_(1,_4)
 + arc_(2,_4) + arc_(2,_5) + arc_(3,_4) + arc_(3,_6) + arc_(4,_5) + arc_(4,_6)
 + arc_(4,_7) + arc_(5,_7) + arc_(6,_7) = 2
Binaries
arc_(1,_2)
arc_(1,_3)
arc_(1,_4)
arc_(2,_4)
arc_(2,_5)
arc_(3,_4)
arc_(3,_6)
arc_(4,_5)
arc_(4,_6)
arc_(4,_7)
arc_(5,_7)
arc_(6,_7)
End
