class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        # 如果是数字加入数字栈中，左括号和字符加入字符栈，遇到右括号弹出数字和直到遇到的第一个左括号为止的顶层表达式循环打印，把表达式放入栈中，到字符串尾返回字符栈的结果。
        stnum = []
        stchar = []
        decode_string = ""
        is_digit_pre = False
        for char in s:
            if char == "[":
                stchar.append(char)
                is_digit_pre = False
            elif char.isdigit():
                if (is_digit_pre):
                    ##########错误1：没有注意到多位数字的情况
                    ############ 这个地方的编解码机制需要再好好琢磨下########
                    new_num = int(stnum.pop()) * 10 + int(char)
                    stnum.append(new_num)
                else:
                    stnum.append(char)
                    is_digit_pre = True
            elif char.isalpha():
                is_digit_pre = False
                ########### 错误2：如何处理不需要多次打印的字符，之前是最后把探空，但这会改变顺序，需要及时处理
                if len(stnum) == 0:
                    decode_string += char
                    continue
                stchar.append(char)
            else:
                is_digit_pre = False
                string_mid = []
                the_char = stchar.pop()
                while (the_char != "["):
                    string_mid.insert(0, the_char)
                    the_char = stchar.pop()
                time = int(stnum.pop())
                string_new = "".join(string_mid)
                if (len(stnum) == 0):
                    decode_string += string_new * time
                else:
                    stchar.append(string_new * time)
        print(decode_string)
        return decode_string


sol = Solution()
# sol.decodeString("3[a]2[bc]")
# sol.decodeString("3[a2[c]]")
# sol.decodeString("2[abc]3[cd]ef")
# sol.decodeString("abc3[cd]xyz")
sol.decodeString("100[leetcode]")
