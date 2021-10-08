from collections import Counter
def equalizeArray(arr):
    contador = Counter(arr)
    return len(arr)-contador.most_common(1)[0][1]
