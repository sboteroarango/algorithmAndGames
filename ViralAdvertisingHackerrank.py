def viralAdvertising(n):
    totalLikes = 2
    numeroGuardado = 2
    for i in range(n-1):
        totalLikes += math.floor((numeroGuardado*3)/2)
        numeroGuardado = math.floor((numeroGuardado*3)/2)
    return totalLikes
