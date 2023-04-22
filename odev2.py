
#input: [[1, 2], [3, 4], [5, 6, 7]] / output: [[[7, 6, 5], [4, 3], [2, 1]]
  
verilen = [[1, 2], [3, 4], [5, 6, 7]]  
def tersle(l):
    l.reverse()
    reverse = [tersle(sublist) for sublist in l if type(sublist) == list]
    
tersle(verilen)
print(verilen)