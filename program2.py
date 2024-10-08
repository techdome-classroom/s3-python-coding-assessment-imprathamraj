class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:  # Handle the empty string case explicitly
            return 0
        
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        total = 0
        n = len(s)
        
        for i in range(n):
            # If current numeral is smaller than the next, subtract its value
            if i < n - 1 and roman_map[s[i]] < roman_map[s[i + 1]]:
                total -= roman_map[s[i]]
            else:
                total += roman_map[s[i]]
        
        return total
