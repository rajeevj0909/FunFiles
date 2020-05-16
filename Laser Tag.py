player = [[1,45],[2,32],[1,51],[1,18],[2,78],[2,92],[1,12],[2,84]]
green=0
red=0
for score in player:
    if score[0]==1:
        green=green+score[1]
    elif score[0]==2:
        red=red+score[1]
print("Green got", green)
print("Red got", red)
