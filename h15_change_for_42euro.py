"""HARD - Change for 42€"""


# Solution 1 - my first
def changes(amount, coins):
    """Returns how many set of change can be made for a given amount and a set of coins"""
    e = sorted([c for c in coins if c <= amount], reverse=True)
    res = 0
    if len(e) <= 1:
        return 1
    for c in range(0, amount + 1, e[0]):
        res += changes(amount - c, e[1:])
    return res


# Solution 2 - my second - condensed & improved
def changes2(amount, coins):
    """Returns how many set of change can be made for a given amount and a set of coins"""
    res = 0
    for c in range(0, amount + 1, coins[-1]):
        res += 1 if len(coins) <= 2 else changes2(amount - c, coins[:-1])
    return res


# Solution 3 - my third - fast enough!
from functools import lru_cache
@lru_cache()
def changes3(amount, coins):
    """Returns how many set of change can be made for a given amount and a set of coins"""
    return sum([1 if len(coins) < 3 else changes3(amount - c, coins[:-1]) for c in range(0, amount + 1, coins[-1])])


# Solution 4 - best way (optimized memoization)
def changes4(amount, coins):
    """Returns how many set of change can be made for a given amount and a set of coins"""

    # dp[i] will be storing the number of solutions for
    # value i. We need sum+1 rows as the dp is
    # constructed in bottom up manner using the base case
    # (sum = 0)
    dp = [0] * (amount + 1)

    # Base case (If given value is 0)
    dp[0] = 1

    # Pick all coins one by one and update the table[]
    # values after the index greater than or equal to the
    # value of the picked coin
    for coin in coins:
        for j in range(coin, amount + 1):
            dp[j] += dp[j - coin]
            
    return dp[amount]


# Other Solutions:
# ----------------------------------------------------

# Python program for coin change problem.
# using recursion
def countRecur5(coins, n, sum):
  
    # If sum is 0 then there is 1 solution
    # (do not include any coin)
    if sum == 0:
        return 1

    # 0 ways in the following two cases
    if sum < 0 or n == 0:
        return 0

    # count is sum of solutions (i)
    # including coins[n-1] (ii) excluding coins[n-1]
    return countRecur5(coins, n, sum - coins[n - 1]) + \
  			countRecur5(coins, n - 1, sum)

def count5(coins, sum):
    return countRecur5(coins, len(coins), sum)


# ----------------------------------------------------

# Python program for coin change problem.
# using memoization
def countRecur6(coins, n, sum, memo):
  
    # If sum is 0 then there is 1 solution
    # (do not include any coin)
    if sum == 0:
        return 1

    # 0 ways in the following two cases
    if sum < 0 or n == 0:
        return 0

    # If the subproblem is previously calculated then
    # simply return the result
    if memo[n - 1][sum] != -1:
        return memo[n - 1][sum]

    # count is sum of solutions (i)
    # including coins[n-1] (ii) excluding coins[n-1]
    memo[n - 1][sum] = (countRecur6(coins, n, sum - coins[n - 1], memo) + 
                        countRecur6(coins, n - 1, sum, memo))
    return memo[n - 1][sum]


def count6(coins, sum):
    memo = [[-1 for _ in range(sum + 1)] for _ in range(len(coins))]
    return countRecur6(coins, len(coins), sum, memo)

# ----------------------------------------------------

if __name__ == "__main__":
    for y in range(2, 43):
        x = changes4(y, (1, 2, 5, 10, 20, 50, 100, 200, 500))
        print(f"{y}: {x}")
