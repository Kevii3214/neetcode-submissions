class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for char in s:
            if (char == '(' or char == '{' or char == '['):
                stack.append(char)
            elif len(stack) != 0:
                x = stack.pop()
                if x == '(' and char == ')':
                    continue
                elif x == '{' and char == '}':
                    continue
                elif x == '[' and char == ']':
                    continue
                else:
                    return False
            else:
                return False
        if (len(stack) == 0):
            return True
        else: 
            return False