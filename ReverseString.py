class ReverseString(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        current_str = [char for char in s]
        i = 0
        j = len(s)-1
        while i < j:
            temp = current_str[i]
            current_str[i] = current_str[j]
            current_str[j] = temp
            i += 1
            j -= 1
        return ''.join(current_str)
    