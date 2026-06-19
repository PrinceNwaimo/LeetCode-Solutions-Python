class IsomorphicStrings(object):
    def isIsomorphic(self, s, t):
        """         
        :type s: str
        :type t: str
        :rtype: bool         
        """
        if s == None or t == None:            
            return False
        elif s == "" and t == "":
            return True         
        else:
            if len(s) != len(t):
                return False
            lookup = {}   
            for i in range(0, len(s)):
                c1 = s[i]
                c2 = t[i]
                if c1 in lookup:
                    if lookup[c1] != c2:
                        return False
                else:
                    if c2 in lookup.values():
                        return False
                    lookup[c1] = c2
            return True