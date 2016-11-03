list = [0 * x for x in range(101)]	#Create a list of 100 '0s'

doors = "The following doors are open: "

for j in range(1, 101) :
    for i in range(1, 101) :
        if i % j == 0:
            if list[i] == 0:
                list[i] = 1
            else:
                list[i] = 0

for k in range(100):
	if list[k] == 1:
		doors = doors + str(k) + ", "

doors = doors.replace(", , ", "")
print (doors)
