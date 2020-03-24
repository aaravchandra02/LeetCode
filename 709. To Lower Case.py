"""Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

Example 1:
Input: "Hello"
Output: "hello"

Example 2:
Input: "here"
Output: "here"

Example 3:
Input: "LOVELY"
Output: "lovely" """


class Solution:
    def toLowerCase(self, str: str) -> str:
        ans = ""
        for i in str:
            tmp = ord(i)
            if(tmp >= 65 and tmp <= 90):
                tmp += 32
            ans = ans+chr(tmp)
        return(ans)
