
def climbingLeaderboard(ranked, player):
    
    rankedSinDuplicados = list(dict.fromkeys(ranked))
    clasificaciones = []
    for play in player:
        
        if play in rankedSinDuplicados:
            clasificaciones.append(rankedSinDuplicados.index(play)+1)
        if play not in rankedSinDuplicados:
            if play< ranked[-1]:
                clasificaciones.append(len(rankedSinDuplicados)+1)
            elif play> ranked[0]:
                clasificaciones.append(1)
            else:
                
                for i in range(len(rankedSinDuplicados)):
                    if (rankedSinDuplicados[i]>play) and (rankedSinDuplicados[i+1]<play):
                        clasificaciones.append(i+2) 
    
    return clasificaciones


