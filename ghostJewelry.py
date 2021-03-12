import random
class ghost:
    def __init__(self, weight, jewelry):
        self.jewelry = jewelry
        self.weight = weight
        
def max_ghost(ghosts,usedGhosts): #finds the ghost with the most jewels
    jewelVals = []
    for i in ghosts:
        if i in usedGhosts:
            jewelVals.append(0)
        else:
            jewelVals.append(i.jewelry)
    
    max_index = jewelVals.index(max(jewelVals))
    return ghosts[max_index]

def weight_calc(ghosts, maxGhost, subWeight, usedGhosts): #recursively finds number of jewels on sub
    maxGhost = max_ghost(ghosts, usedGhosts)
    usedGhosts.append(maxGhost)

    if len(usedGhosts) > len(ghosts): #returns 0 if no more     ghosts fit on the sub
        return 0
    elif maxGhost.weight>subWeight: #returns the value of the next ghost that has not been used if the ghost with the most jewels doesnt fit
        return weight_calc(ghosts, maxGhost, subWeight, list(usedGhosts))
    else: #returns the max of the ghost with the most jewels + the rest of the possible values with the weight of the sub minus the ghost or the largest possible value without the ghost with the most jewels
        return max((maxGhost.jewelry + weight_calc(ghosts, maxGhost, subWeight -maxGhost.weight, list(usedGhosts)), weight_calc(ghosts, maxGhost, subWeight, list(usedGhosts))))

ghosts = []
ghosts.append(ghost(20, 35))
ghosts.append(ghost(40, 76))
ghosts.append(ghost(60, 128))
ghosts.append(ghost(12, 24))
ghosts.append(ghost(17,52))
ghosts.append(ghost(1,1))
ghosts.append(ghost(33,70))
print(str(weight_calc(ghosts, 0, 60, [])) + ' jewels fit on the sub')