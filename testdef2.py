def tavan(n, t=2):
    '''
    this function answer you a tavan
    
    '''
    
    
    javab = 1
    for i in range (t):
        javab *= n

    return javab
print(tavan(5))