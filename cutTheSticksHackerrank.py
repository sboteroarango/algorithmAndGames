
def cutTheSticks(arr):
    cantidadDeSticks = [len(arr)]
    while len(arr)>1:
        arr = list(map(lambda stick:stick-min(arr),arr))
        arr = [stick for stick in arr if stick>0]
        if len(arr)>0:
            cantidadDeSticks.append(len(arr))
    return cantidadDeSticks
        
