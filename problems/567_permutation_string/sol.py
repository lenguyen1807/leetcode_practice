class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_budget = {}
        for c in s1:
            s1_budget[c] = s1_budget.get(c, 0) + 1
            
        s2_budget = {}
        start = 0
        
        for end in range(len(s2)):
            c = s2[end]
            s2_budget[c] = s2_budget.get(c, 0) + 1
            
            while s2_budget[c] > s1_budget.get(c, 0):
                left_char = s2[start]
                s2_budget[left_char] -= 1
                start += 1
                
            if end - start + 1 == len(s1):
                return True
                
        return False
