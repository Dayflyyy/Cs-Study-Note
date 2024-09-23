class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = []
        for i in range(0, len(s)):
            if (s[i] == "(" or s[i] == "{" or s[i] == "["):
                st.append(s[i]);
            elif (s[i] == ")"):
                if (len(st) == 0): return False;
                if (st.pop() == "("):
                    continue
                else:
                    return False;
            elif (s[i] == "}"):
                if (len(st) == 0): return False;
                if (st.pop() == "{"):
                    continue
                else:
                    return False;
            elif (s[i] == "]"):
                if (len(st) == 0): return False;
                if (st.pop() == "["):
                    continue
                else:
                    return False;
        return len(st) == 0


sol = Solution();
print(sol.isValid("()[]{}"))
print(sol.isValid("([)]"))
print(sol.isValid("{[]}"))
print(sol.isValid("]"))
print(sol.isValid("}"))
print(sol.isValid("("))
print(sol.isValid("[]}"))

