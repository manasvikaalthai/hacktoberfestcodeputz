/*

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 */
 
 
 class Solution:
    def isValid(self, s: str) -> bool:
        d = {")": "(", "}": "{", "]": "["}
        st = []
        for i in range(len(s)):
            if s[i] not in d:
                st.append(s[i])
            else:
                try:
                    t = st.pop()
                    if t != d[s[i]]:
                        return False
                except:
                    return False

        return True if len(st) == 0 else False
