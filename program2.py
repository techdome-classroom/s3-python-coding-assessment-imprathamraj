class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Roman numeral mappings
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        total = 0
        n = len(s)
        
        # Iterate through the string
        for i in range(n):
            # If the current value is less than the next one, subtract it
            if i < n - 1 and roman_map[s[i]] < roman_map[s[i + 1]]:
                total -= roman_map[s[i]]
            else:
                # Otherwise, add the value
                total += roman_map[s[i]]
        
        return total

sol = Solution()
print(sol.romanToInt("III"))   
print(sol.romanToInt("LVIII"))  
print(sol.romanToInt("MCMXCIV")) 
