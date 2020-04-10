# https://leetcode.com/problems/minimum-window-subsequence

class Solution(object):
    def minWindow(self, S, T):
        """
        Find subsequence containing T, and return ending index in S
        Improve subsequence by searching from right-left, to find best starting index in S
        Length = end-start index, check if it's minimum
        
        e.g. S = abacbcdfeg . T = bcde
                 0123456789
        find subsequence   - bacbcdfe, end = 8
        improve subsequence- bcdfe, start = 4
        length = 5
        
        Repeat next subsequence search after start 5
        """
        
        # Find - Get ending point of subsequence starting on/after index s
        def find_subseq(s):
            t = 0
            while s < len(S):                       # Search forward
                if S[s] == T[t]:
                    t += 1
                    if t == len(T):
                        break
                s += 1
            
            return s if t == len(T) else None       # Ensure last character of T was found before loop ended
        
        # Improve - Get best starting point of subsequence ending at index s
        def improve_subseq(s):
            t = len(T) - 1
            while t >= 0:                           # Search backward
                if S[s] == T[t]:
                    t -= 1
                s -= 1
            
            return s+1
        
        
        s, min_len, min_window = 0, float('inf'), ''
        
        while s < len(S):
            end = find_subseq(s)            # Find end-point of subsequence

            if not end:
                break
                
            start = improve_subseq(end)     # Improve start-point of subsequence

            if end-start+1 < min_len:       # Track min length
                min_len = end-start+1
                min_window = S[start:end+1]
            
            s = start+1                     # Start next subsequence search

        return min_window
