class ValidParentheses(object):
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        if s == []:
            return False
        else:
            stack = []
            balanced = True
            index = 0
            while index < len(s) and balanced:
                symbol = s[index]
                if symbol in "({[":
                    stack.append(symbol)
                else:
                    if stack == []:
                        balanced = False
                    else:
                        top = stack.pop()
                        if not self.matches(top, symbol):
                            balanced = False
                index = index + 1
            return balanced and stack == []

    def matches(self, left, right):
        pairs = {"(": ")", "[": "]", "{": "}"}
        return left in pairs and pairs[left] == right