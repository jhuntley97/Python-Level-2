#Jwaun Huntley
#4/11/2019

x = int(input("What day did you leave on? 0 for Sunday and 6 for Saturday..."))
y = int(input("How many nights was you gone?"))
c = x +(y % 7)

print("The day you got back is",c)
