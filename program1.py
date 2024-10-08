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
                top_element = stack.pop() if stack else '#' 
                if mapping[char] != top_element:
                    return False
            else:  # It's an opening bracket
                stack.append(char)
        
        return not stack  # Return True if the stack is empty (all brackets matched)

# Example usage
sol = Solution()
print(sol.isValid("()"))      # Output: True
print(sol.isValid("()[]{}"))  # Output: True
print(sol.isValid("(]"))      # Output: False






    



  

