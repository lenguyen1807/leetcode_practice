class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq_t = {}
        for c in t:
            freq_t[c] = freq_t.get(c, 0) + 1

        freq_s = {}
        start = 0
        answer = [-1, len(s)]
        need = len(freq_t)
        have = 0

        for end in range(len(s)):
            c = s[end]
            freq_s[c] = freq_s.get(c, 0) + 1
            if c in freq_t and freq_s[c] == freq_t[c]:
                have += 1

            while start <= end and have == need:
                if (end - start + 1) < (answer[1] - answer[0] + 1):
                    answer = [start, end]
                left = s[start]
                freq_s[left] -= 1
                if left in freq_t and freq_s[left] < freq_t[left]:
                    have -= 1
                start += 1

        return s[answer[0]:answer[1] + 1] if answer[0] != -1 else ""
