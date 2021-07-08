def countingValleys(steps, path):
    
    valleys = 0
    posicionActual = 0
    posicionAnterior = 0
    for step in path:
        if step == 'U':
            posicionActual +=1
        else:
            posicionActual -=1
        if posicionActual == 0 and posicionAnterior <0:
            valleys += 1
        posicionAnterior = posicionActual
    return valleys
