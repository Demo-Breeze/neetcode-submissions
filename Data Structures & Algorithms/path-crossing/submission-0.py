class Solution:     
    def isPathCrossing(self, path: str) -> bool:         
        coordinate = [0,0]         
        final  = [[0,0]]         
        for i in path:             
            match i:                 
                case "N":                     
                    coordinate[0]+=1                 
                case "E":                     
                    coordinate[1]+=1                 
                case "W":                     
                    coordinate[1]-=1                 
                case "S":                     
                    coordinate[0]-=1 
                case _:
                   print("I did something wrong")

            final.append(coordinate[:])                   
        b = [list(x) for x in set(tuple(x) for x in final)]         
        if len(final)!= len(b):             
            return True        
        else:             
            return False