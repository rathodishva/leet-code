class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False  # Early return for negative numbers
        reversed = int((str(x)[::-1]))
        return x == reversed
            

