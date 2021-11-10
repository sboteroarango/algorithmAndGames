def jumpingOnClouds(c):
    saltos = 0
    i = 0
    while i <= len(c)-1:
        try:
            print(i)
            if c[i+1] == 1:
                i += 2
                saltos += 1
            elif c[i+1] == 0:
                if c[i+2] == 0:
                    i += 2
                    saltos += 1
                else:
                    i += 1
                    saltos += 1
        except:
            if i == len(c)-1:
                return saltos
            else:
                return saltos + 1
