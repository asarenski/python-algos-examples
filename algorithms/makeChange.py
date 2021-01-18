def makeChangeRecursive(denoms = [], total = 0):
    if total == 0:
        return 1
    elif not denoms:
        return 0

    maxDenom = max(denoms)
    count = 0
    while total - (count * maxDenom) > 0:
        count += 1
    
    denoms.remove(maxDenom)

    totalWays = 0
    for i in range(count+1):
        totalWays += makeChangeRecursive(denoms.copy(), total - i*maxDenom)

    return totalWays

"""
The goal of this method is to reduce the duplicate times we calculate change
for a specific denom and total pair.
"""
def makeChangeTopDownDP(denoms = [], total = 0):
    if not denoms or total <= 0:
        return 0

    # allocate a 2D array where:
    # first key is total
    # second key is denom index
    map = [[0 for i in denoms] for j in range(total+1)]
        
    ways = makeChangeTopDownDPHelper(denoms, total, 0, map)

    return ways
    

def makeChangeTopDownDPHelper(denoms = [], total = 0, denomIdx = 0, map = []):
    if total == 0:
        return 1
    elif denomIdx >= len(denoms):
        return 0

    if map[total][denomIdx] > 0:
        return map[total][denomIdx]

    denomCount = 0
    while total - denoms[denomIdx] * denomCount >= 0:
        denomCount += 1

    ways = 0
    for i in range(denomCount+1):
        nextTotal = total - i*denoms[denomIdx]
        ways += makeChangeTopDownDPHelper(denoms, nextTotal, denomIdx+1, map)
    
    map[total][denomIdx] = ways

    return ways



print(f'totalWays: {makeChangeRecursive([25, 10, 5, 1], 100)}')
print(f'totalWays DP: {makeChangeTopDownDP([25, 10, 5, 1], 100)}')
