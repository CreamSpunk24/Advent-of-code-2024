left = []
right = []
sim_score = 0
with open("input.txt", "r") as file:
    for line in file:
        data = list(map(int, line.strip().split()))
        if len(data) != 2:
            continue
        left.append(data[0])
        right.append(data[1])
    left.sort()
    print(left)
    right.sort()
    total = 0
    for i in range(len(left)):
        diff = abs(left[i]- right[i])
        total = total + diff
    print(total)
    for i in range(len(left)):
      c =  right.count(left[i])
      sim_score = sim_score + c * left[i]
    print(sim_score)
      


    
        
        

