class Solution:
    def isPalindrome(self, s: str) -> bool:

        t=""
        for i in s:
          if  i.isalnum():
            t=t+i.lower()
        a=t[::-1]
        if a==t:
            return True
        else:
            return False
        