class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sp,tp=0,0
        while tp<=len(t)-1:
            if s[sp]==t[tp]:
                sp+=1
            tp+=1
            
        return sp==len(s)
            