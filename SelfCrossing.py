class SelfCrossing(object):     
    def isSelfCrossing(self, x):
        """         
        :type x: List[int]         
        :rtype: bool         
        """
        if x == None or len(x) <= 3:             
            return False
        else:             
            for i in range(3, len(x)):
                if (x[i-3] >= x[i-1]) and (x[i-2] <= x[i]):
                    return True                 
                if (i >= 4) and (x[i - 4] + x[i] >= x[i-2]) and (x [i-3] == x[i-1]):
                    return True  
                if (i>=5) and (x[i-5] <= x[i-3])and (x[i-4] <=  x[i-2]) and (x[i-1] <= x[i - 3]) and (x[i-1] >= x[i-3] - x[i-5]) and (x[i] >= x[i-2] - x[i-4]) and (x[i] <= x[i-2]):                     
                    return True
                return False
            