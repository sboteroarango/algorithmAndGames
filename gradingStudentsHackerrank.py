def gradingStudents(grades):
    yaCalificadas = []
    for grade in grades:
        if grade<38:
            yaCalificadas.append(grade)
        else:
            multiplosDeCinco = list(range(5,101,5))
            for multiplo in multiplosDeCinco:
                if grade/multiplo <=1:
                    multiploDeCincoSiguiente=multiplo
                    break
            if multiploDeCincoSiguiente-grade <3:
                yaCalificadas.append(multiploDeCincoSiguiente)
            else:
                yaCalificadas.append(grade)
    return yaCalificadas
