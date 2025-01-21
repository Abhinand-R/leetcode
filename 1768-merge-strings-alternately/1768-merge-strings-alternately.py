class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mer=""
        s=""
        i=0
        while i< min(len(word1),len(word2)):
            mer+=(word1[i]+word2[i])
            i+=1
        j=max(len(word1),len(word2))-min(len(word1),len(word2))
        if max(len(word1),len(word2))==len(word2) and j!=0:
            mer+=word2[-j:]
        if max(len(word1),len(word2))==len(word1) and j!=0 :
            mer+=word1[-j:]
        return mer
