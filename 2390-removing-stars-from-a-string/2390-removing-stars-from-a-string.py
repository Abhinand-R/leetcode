class Solution:
    def removeStars(self, s: str) -> str:
        stack=[]
        st=""
        for i in s:
            if i=='*':
                stack.pop()
            else:
                stack.append(i)
        for j in stack:
            st+=j
        return st
