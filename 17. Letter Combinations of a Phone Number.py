#Title : Letter Combinations of a Phone Number
#Problem : https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitMap = {
            "2" : "abc","3" : "def","4" : "ghi", "5" : "jkl","6":"mno","7":"pqrs","8" : "tuv", "9" : "wxyz"
        }
        res = []

        def backtrack(d, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            for j in digitMap[digits[d]]:
                backtrack(d + 1 , curStr + j)

        if digits:
            backtrack(0, "")
        return res
        