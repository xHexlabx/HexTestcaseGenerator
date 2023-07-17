import numpy as np

class linear :
    
    def __init__(self) :
        
        pass
    
    def generate(n , sorting , range , lin) :
        
        ls = []
        
        if lin == True :
            
            first = range[0]
            last = range[-1]
            
            start = np.random.randint(first , last - n)
            
            ls = [num for num in range(start , start + n)]
            
        if sorting == 'asc' :
            
            ls.sort()
        
        if sorting == 'desc' :
            
            ls.sort( reverse = True )
        
        return ls
        
        
        

class graph :
    
    pass
