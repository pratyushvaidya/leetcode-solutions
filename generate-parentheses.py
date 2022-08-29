#22. GENERATE PARENTHESES

class Solution:
    """
    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

    Example 1:
    Input: n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]

    Example 2:
    Input: n = 1
    Output: ["()"]
    """
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0: return ['']
        
        paranthesis = []
        for i in range(n):
            for left in self.generateParenthesis(i):
                for right in self.generateParenthesis(n-1-i):
                    paranthesis.append('({}){}'.format(left, right))
        return paranthesis
