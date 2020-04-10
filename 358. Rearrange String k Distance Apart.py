# https://leetcode.com/problems/rearrange-string-k-distance-apart

class Solution(object):
    def rearrangeString(self, s, k):
        """
        Like dealing cards to people
        e.g. aaaabbbbccdde
        Deal the most frequent characters into that many buckets
        a,4 & b,4
        a, a, a, a
        ab, ab, ab, ab
        Deal the remaining characters ccdd into 4-1 = 3 buckets (except the last)
        abc, ab, ab, ab
        abc, abc, ab, ab
        abc, abc, abd, ab
        abcd, abc, abd, ab
        abcd, abce, abd, ab
        
        If any bucket (except last) has length < k, return False
        """
       
        # Sort characters by frequencies - highest first
        counts = sorted(collections.Counter(s).items(), key = lambda x:x[1], reverse = True)
        
        max_freq = counts[0][1]                     # Get max freq
        buckets = ['' for _ in range(max_freq)]     # and create that many buckets
        
        max_chars    = ''.join([char*freq for char,freq in counts if freq == max_freq])     # aaaabbbb
        remain_chars = ''.join([char*freq for char, freq in counts if freq < max_freq])     # ccdde
        
        # Distribute the max-freq characters into all buckets
        for i, c in enumerate(max_chars):
            buckets[i%max_freq] += c
        
        # Distribute remaining characters (ordered by frequency) into all but last bucket
        for i, c in enumerate(remain_chars):
            buckets[i%(max_freq-1)] += c
        
        # If any bucket has length < k, then rearrangement with gap at least k is not possible
        if any([len(bucket) < k for bucket in buckets[:-1]]):
            return ''
        
        return ''.join(buckets)
