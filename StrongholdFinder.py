#Made by sirBadDoggo
import math
from sympy import symbols, Eq, solve #This library helps solve equations

x,z = symbols('x,z') #Initializes the variables

#Input 1 for coordinates
x1 = float(input("x1: "))
z1 = float(input("z1: "))
ang1 = float(input("ang1: ")) #Facing Angle X
ang1 = ang1 * -1
if ang1 < 0 :
    ang1 = 180 + (180 + ang1) 
#Calculates slope from the angle
m1 = math.tan( math.radians(ang1) )
#Equation of the line 1
eqn1 = Eq( ( ( (x1-x)/(z1-z) ) - m1 ),0 )

#Input 2 for coordinates
x2 = float(input("x2: "))
z2 = float(input("z2: "))
ang2 = float(input("ang2: ")) #Facing Angle X
ang2 = ang2 * -1
if ang2 < 0 :
    ang2 = 180 + (180 + ang2) 
#Calculates slope from the angle    
m2 = math.tan( math.radians(ang2) )
#Equation of the line 2
eqn2 = Eq( ( ( (x2-x)/(z2-z) ) -m2 ),0 )

#Below solves the lines to get the intersecting point
print("Solving:")
Coordinates = solve((eqn1,eqn2),(x,z) ) #The final coordinates

#Rounds the values to 2 decimal places
X = round(Coordinates[x],2)
Z = round(Coordinates[z],2)

print("Coordinates are {0} ~ {1}".format(X,Z))