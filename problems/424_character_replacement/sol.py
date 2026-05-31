class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        start = 0
        max_len = 0

        for end in range(len(s)):
            c = s[end]
            freq[c] = freq.get(c, 0) + 1
            max_c = max(freq, key=freq.get)

            while start <= end and (end - start + 1) - freq[max_c] > k:
                freq[s[start]] -= 1
                start += 1
                max_c = max(freq, key=freq.get)

            max_len = max(max_len, end - start + 1)

        return max_len
