#ASTU GPA Calculator
#Customize your subjects here
subjects = ["Applied mathematics II", "Statistics", "Emerging", "Logic", "Biology", "Biology Lab", "Physics Lab", "Chemistry Lab"]
Points = []
chrs = []

for x in subjects:
   Grade_Pt = float(input(f"\nEnter point of {x}: "))
   chr = int(input(f"Enter credit hour of {x}: "))
   Point = Grade_Pt * chr
   print(f"Point of {x} is {Point}")
   Points.append(Point)
   chrs.append(chr)


print(f"\nThe points you got are: {Points}")
print("\n Sum of the points is: " + str(sum(Points)))
print("\n################################\n")

print("Your GPA is: " + str(sum(Points)/sum(chrs)))
print("\n################################")














