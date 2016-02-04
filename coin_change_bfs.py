'''
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.

Approach: BFS
EXACT APPROACH WHAT I DID IN PERFECT SQUARES CODE
https://leetcode.com/discuss/76432/fast-python-bfs-solution
'''
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if len(coins) == 0:
            return -1
        elif amount == 0:
            return 0
        else:
            nodes = set()
            nodes.add(amount)
            counter = 1
            visited = [False]*(amount+1)
            visited[0] = True
            coins = set(coins)
            while len(nodes) != 0:
                #print counter
                new_nodes = set()
                for parent_node in nodes:
                    for child_node in coins:
                        new_val = parent_node - child_node
                        if parent_node == child_node:
                            return counter
                        if parent_node < child_node:
                            continue
                        if not visited[new_val]:
                            visited[new_val] = True
                            new_nodes.add(new_val)
                nodes = new_nodes
                counter += 1
            return -1
