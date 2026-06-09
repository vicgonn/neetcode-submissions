from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        word_counter_s1 = defaultdict(int)
        word_counter_s2 = defaultdict(int)

        for letter in s1:
            word_counter_s1[letter] += 1

        lp = 0

        for rp in range(len(s2)):
            # 1. Expand window: add right character
            word_counter_s2[s2[rp]] += 1

            # 2. Shrink window if it exceeds len(s1)
            if rp - lp + 1 > len(s1):
                left_char = s2[lp]
                word_counter_s2[left_char] -= 1
                if word_counter_s2[left_char] == 0:
                    del word_counter_s2[left_char]  # keep dicts clean for comparison
                lp += 1

            # 3. Check if current window is a permutation
            if word_counter_s1 == word_counter_s2:
                return True

        return False
