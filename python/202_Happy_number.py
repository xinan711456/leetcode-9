class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        val = set()  
        while n not in val:  
            val.add(n)  
            newn = 0  
            while n != 0:  
                newn +=  (n % 10) * (n % 10)  
                n /=  10  
            n = newn  
            if n == 1:  
                return True  
        return False 
        
