# 20. VALID PARENTHESES

class Solution:
    """
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.


    Example 1:

    Input: s = "()"
    Output: true
    Example 2:

    Input: s = "()[]{}"
    Output: true
    Example 3:

    Input: s = "(]"
    Output: false
    """
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ['(', '{', '[']:
                stack.append(i)
            if len(stack)!=0:

            elif i == ')' and len(stack)!=0 and stack[-1] == '(':
                stack.pop()
            elif i == '}' and len(stack)!=0 and stack[-1] == '{':
                stack.pop()
            elif i == ']' and len(stack)!=0 and stack[-1] == '[':
                stack.pop()
            else:
                return False 
        if len(stack) > 0:
            return False
        return True
