def repeatedString(s, n):
    cantidadA = s.count('a')
    cantidadA = cantidadA*(n//len(s))
    cantidadA += s[0:n%len(s)].count('a')
    return cantidadA
