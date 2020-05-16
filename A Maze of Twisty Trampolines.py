pointer_list = []
input_file = open("day5input.txt", "r")
input_file = input_file.readlines()
for line in input_file:
        line = int(line)
        pointer_list.append(line)


steps = 0
index = 0


while index < len(pointer_list) and index > -1:
        if pointer_list[index]>2:
            new_index = pointer_list[index]-1
            current_val = pointer_list[index]
            pointer_list[index] = new_index
            index = index+current_val
            steps = steps+1
        else:
            new_index = pointer_list[index]+1
            current_val = pointer_list[index]
            pointer_list[index] = new_index
            index = index+current_val
            steps = steps+1
print(pointer_list)
print(steps)
