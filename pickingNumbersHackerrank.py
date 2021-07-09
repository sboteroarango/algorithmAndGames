def pickingNumbers(a):
    listaDeLongitudes = []
    for i in a :
        listaDeLongitudes.append(a.count(i)+a.count(i-1))
        listaDeLongitudes.append(a.count(i)+a.count(i+1))
        a.pop(a.index(i))
    return max(listaDeLongitudes)
        
