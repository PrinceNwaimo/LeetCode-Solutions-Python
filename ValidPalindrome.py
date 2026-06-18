import re 
class ValidPalindrome(object):
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
        if len(s) == 0:             
            return True
        else:             
            start = 0
            s = s.lower()
            newS = re.sub(r"[^a-zA-Z09]","",s)             
            end = len(newS)-1
            while start < end:
                if newS[start] == newS[end]:
                    start = start + 1
                    end = end - 1
                else:                    
                    return False
            return True
