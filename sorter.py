
# It's a basic class that has named Sorter

class Sorter(list, object):
  
  #My function that i wrote it
    def sorter(item):
        if type(item) != list:
            pass
        
        elif type(item) == list:
            for i in range(0,len(item)):
                if type(item[i]) == int:
                    continue
                    
                elif type(item[i]) == float:
                    continue
                    
                elif type(item[i]) == str:
                    item[i] = int()
                    
                elif type(item[i]) == complex:
                    item[i] = int()
                        
     # First appear before sorting   
        print(item)
        item.sort()
        print(item)
    # First appear after sorting 
    
    def __init__(self, item):
        self.sorter(item)
