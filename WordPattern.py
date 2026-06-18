class WordPattern(object):
    def wordPattern(self, pattern, str):
        """         
        :type pattern
        : str
        :type str
        : str        
        :rtype: bool
        """
        if pattern == None or str == None:
            return False         
        else:
            len_str = len(str.split(" "))
            len_pattern = len(pattern)
            if len_str != len_pattern:
                return False
            str = str.split(" ")
            lookup = {}
            for i in range(0, len(pattern)):
                s = str[i]
                p = pattern[i]
                if p in lookup:
                    if lookup[p] != s:
                        return False
                else:
                    if s in lookup.values():
                        return False
                    lookup[p] = s
            return True