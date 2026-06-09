from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        lp = 0
        res = 0
        hash_count = defaultdict(int)
        # while lp < len(s):
        for rp in range(len(s)):
            hash_count[s[rp]] += 1
            # calculate if condition is valid
            window_size = rp - lp + 1
            cal = window_size - max(hash_count.values())
            if cal <= k:
                res = max(res,window_size)
            else:
                hash_count[s[lp]] -= 1
                lp += 1
        
        return res