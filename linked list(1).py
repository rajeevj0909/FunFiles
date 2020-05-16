link_list = [[1,"b"],[2,"c"],[None,"d"],[0,"a"]]
next_free = 4
start = 3


def output_list():
    print(link_list[start][1])
    next_node = link_list[start][0]
    for item in link_list:
        if next_node != None: #None is Python equivalent to null
            print(link_list[next_node][1])
            next_node = link_list[next_node][0]
        else:
            print("\n")
            break

def add_item(data):
    global next_free #required for variables above to be accessed within function
    global link_list
    link_list[next_free-2][0] = next_free
    link_list.append([None,data])
    next_free = next_free + 1

output_list()
add_item("e")
output_list()
