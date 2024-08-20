class Solution:
    def isValid(self, s: str) -> bool:

        # ---MY ATTEMPT WITH PSEUDOCODE--- 

        ## 1) first store a open paranthesis
        ## 2) then search for a closing
        ## 3) remove them from str
        ## 4) if str is empty, return true
        ## 5) if not (from lack of matching) return false

        # ob = 0
        # while ob < len(s):
        #     print('s after each iter:', s)
        #     if s[ob] == '(':
        #         temp_s = s[ob]
        #         ob+=1
        #         for cb in range(len(s)):
        #             if s[cb] == ')':
        #                 s = s.replace(s[cb], '')
        #                 s = s.replace(temp_s, '')
        #                 ob = 0
        #                 break
        #     elif s[ob] == '[':
        #         print('ob in [:', ob)
        #         temp_s = s[ob]
        #         ob+=1
        #         for cb in range(len(s)):
        #             if s[cb] == ']':
        #                 s = s.replace(s[cb], '')
        #                 s = s.replace(temp_s, '')
        #                 ob = 0
        #                 break
        #     elif s[ob] == '{':
        #         print('ob in {:', ob)
        #         temp_s = s[ob]
        #         ob+=1
        #         for cb in range(len(s)):
        #             if s[cb] == '}':
        #                 s = s.replace(s[cb], '')
        #                 s = s.replace(temp_s, '')
        #                 print(s)
        #                 break
        #     else:
        #         ob+=1
        # if s == "":
        #     return True
        # else:
        #     return False

        
        # ---RETRIEVED SOLUTION WITH MY PERSONAL NOTES---

        stack = []
        for c in s:
            # using in for all possible opening string is good shorthand strategy 
            # I will start considering using in the future
            if c in '({[':
                stack.append(c)
            # learned that \ is used to extend a line for readability
            else:
                if not stack \
                    or c == ')' and stack[-1] != '(' \
                    or c == ']' and stack[-1] != '[' \
                    or c == '}' and stack[-1] != '{':
                    # if stack is empty or neither of the opening brackets are the last 
                    # thing in stack matching its corresponding closing bracket, c, then return false
                    return False
                # otherwise, that implies a match and we can just get rid of only the opening bracket
                stack.pop()
        return not stack

        # This is running at O(n) time because the operations are proportionate 
        # to the num of characters in the string 

        # This is using O(1) space because we are only manipulating one piece of data which is the stack

        # After confirming with ChatGPT, the space complexity is O(n). The stack is still the only
        # piece of data we are manipulating, but because in the worst case it can grow to a maximum 
        # length of O(n/2), that makes the time complexity O(n). 


        
