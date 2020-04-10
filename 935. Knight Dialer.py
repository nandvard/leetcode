# https://leetcode.com/problems/knight-dialer/submissions/

class Solution(object):
    def knightDialer(self, N):
        """
        1. Recursion
        Number of ways from 4 after N=2 hops = Sum of number of ways from 4's neighbors with 1 lesser hop
        = Number of ways of 3, with 2 hops + Number of ways of 9 with 2 hops + Number of ways of 0 with 2 hops
        
        2. Dynamic
        After 1 hop, DP[0] = 2 (04,06) which is DP[4]+DP[6] after 0 hops. DP[4] = 3 (43,49,40) which is DP[3]+DP[9]+DP[0] after 0 hops
        After 2 hops,DP[0] = 6 (040,043,049,061,067,060) which is DP[4]+DP[6] after 1 hop. DP[4] = 6 (434,438,492,494,404,406) (DP[3]+DP[9]+DP[0] after 1 hop)
        """
               
        moves = {0:[4,6], 1:[6,8], 2:[7,9], 3:[4,8], 4:[3,9,0], 5:[], 6:[1,7,0], 7:[2,6], 8:[1,3], 9:[2,4]}

        # Recursive Top-Down
        def knight_(number, rounds):
            if rounds == 1:
                return 1
            return sum( [knight_(next_number, rounds-1) for next_number in moves[number]] )

        # return sum( [knight_(number, N) for number in range(0,10)] ) % (10**9+7)


        # Dynamic Bottom-Up
        DP = [1]*10
        for _ in range(N-1):
            DP = [sum( [DP[next_number] for next_number in moves[number]] ) for number in range(0,10)]

        return sum(DP)%(10**9+7)
