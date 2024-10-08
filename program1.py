class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping:  # It's a closing bracket
                top_element = stack.pop() if stack else '#'  # Pop the top of the stack, or use a dummy char
                if mapping[char] != top_element:
                    return False
            else:  # It's an opening bracket
                stack.append(char)
        
        return not stack  # Return True if the stack is empty (all brackets matched)








    



  

