# tuple = collection which is ordered and unchangeable
# 			used to group together related data


student = ("Tuguldur",20,"male")

print(student.count("Tuguldur"))
print(student.index("male"))

for x in student:
	print(x)

if "Tuguldur" in student:
	print("Tuguldur is here!")