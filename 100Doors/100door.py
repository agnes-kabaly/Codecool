door_list = [0 * i for i in range(101)]

for student in range(1, 101) :
    for door in range (1, 101) :
        if Sdoor_list[door] == 0:
            doorLsit[door] = 1
            print("Open it!")

        else:
            print("Close it")
            door_list[door] == 0

print("the following doors are open: ")
