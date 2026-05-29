class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        max_len = 0
        last_seen = {}
        for end in range(len(s)):
            char = s[end]
            if char in last_seen and last_seen[char] >= start:
                start = last_seen[char] + 1
            max_len = max(max_len, end - start + 1)
            last_seen[char] = end
        return max_len