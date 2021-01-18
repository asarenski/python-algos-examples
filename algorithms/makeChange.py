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

print(f'totalWays: {makeChangeRecursive([25, 10, 5, 1], 100)}')

