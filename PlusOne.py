class PlusOne(object):
    def plusOne(self, digits):         
        """
        :type digits: List[int]
        :rtype: List[int]         """
        if len(digits) <= 0:             
            return [0]
        else:             
            carry = 1
            i = len(digits)-1
            running_sum = 0
            new_digits = []             
            while i >= 0:
                running_sum = digits[i] + carry
                if running_sum >= 10:
                    carry = 1                 
                else:
                    carry = 0
                new_digits.append(running_sum %10)                
                i -= 1
            if carry == 1:
                new_digits.append(1)
            return new_digits[::-1]
            
