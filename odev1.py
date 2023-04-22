#input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5] / output: [1,'a','cat',2,3,'dog',4,5]


def duzle(liste):
    duzlenmis = []
    for item in liste:
        if type(item) == list:
            duzlenmis += duzle(item)
        else:
            duzlenmis.append(item)
    
    return duzlenmis

verilen = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print(duzle(verilen))