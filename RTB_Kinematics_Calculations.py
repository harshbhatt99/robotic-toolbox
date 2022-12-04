# -*- coding: utf-8 -*-
"""Copy of RTB_Kinematics_Calculations_Panda.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tWg3igZ3kh83xIPgoTxETdf3q9R_wamz
"""

!pip3 install roboticstoolbox-python

import math
from spatialmath.base import *
from spatialmath import SE3
import spatialmath.base.symbolic as sym
import numpy as np

import roboticstoolbox as rtb

panda = rtb.models.URDF.Panda()
print(panda)
T = panda.fkine(panda.qz, end='panda_hand')
print(T)

point = SE3(0.6, -0.5, 0.0)
point_sol = panda.ikine_LM(point)
print("\nInverse Kinematics Solution :\n" ,point_sol)

## Creating Robotic arm through defining links and Serial Linkage
Link_1=rtb.DHLink(0.5, math.pi/2, 0, 0)
Link_2=rtb.DHLink(0,    0,   0, 0.4)
Link_3=rtb.DHLink(0,    0,   0, 0.4)
h2_panda_robot= rtb.DHRobot([Link_1 ,Link_2,Link_3])
h2_panda_robot

##Forward Kinematics

q1=50
q2=30
q3=0

T=h2_panda_robot.fkine([math.radians(q1),math.radians(q2),math.radians(q3)])

print("Transformation Matrix :\n",T)

# Selection a point to get inverse kinematics solution as angles
print("point-> x: %2.2f ,y: %2.2f ,z: %2.2f" %(1.5,2.5,2.3) )
point = SE3( 0.4453 , 0.5307 , 0.9  )
point_sol = h2_panda_robot.ikine_LM(point)
print(point_sol)

L = sym.symbol('l_1:4') # Symbolics for links
print("symblic Links : ",L)
Link_1=rtb.DHLink(L[0], math.pi/2, 0, 0)
Link_2=rtb.DHLink(0,    0,   0, L[1])
Link_3=rtb.DHLink(0,    0,   0, L[2])
Kaka_robot_symbolic= rtb.DHRobot([Link_1 ,Link_2,Link_3])

Q= sym.symbol('q1:4')   # Symbolics for rotations angles
print("symblic Angles : ",Q)

point = SE3(0.6, -0.5, 0.0)
# point_sol = puma.ikine_LM(point)
T_symbolic=Kaka_robot_symbolic.fkine(Q)
T_symbolic

Ts_symbolic = T_symbolic.simplify()
M = np.matrix(Ts_symbolic.A)
M

M[:3,3] # extracting translation part