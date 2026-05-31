class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        freq_w = {}
        for w in words:
            freq_w[w] = freq_w.get(w, 0) + 1
            
        offset = len(words[0])
        total_len = len(words) * offset
        answer = []
        
        for i in range(offset):
            start = i
            freq_s = {}
            for end in range(i, len(s) - offset + 1, offset):
                sub_w = s[end:end+offset]
                freq_s[sub_w] = freq_s.get(sub_w, 0) + 1
                
                while freq_s[sub_w] > freq_w.get(sub_w, 0):
                    left_w = s[start:start+offset]
                    freq_s[left_w] -= 1
                    start += offset
                    
                if (end + offset - start) == total_len:
                    answer.append(start)
                    
        return answer
