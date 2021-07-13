def utopianTree(n):
    altura = 1
    for i in range(1,n+1):
        if i%2 != 0:
            altura = altura * 2
        else:
            altura = altura + 1

    return altura
