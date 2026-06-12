class ReverseVowelsOfAString(object):
    def __init__(self):
        self.vowels = set('aeiouAEIOU')
    def reverseVowels(self, s):        
        """
        :type s: str
        :rtype: str
        """    
        if s == None or s == '':
            return s
        else:
            i = 0
            j = len(s) - 1  
            s = list(s)
            while i < j:
                if s[i] not in self.vowels:
                    i += 1
                    continue
                if s[j] not in self.vowels:
                    j -= 1
                    continue
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            return ''.join(s)
        