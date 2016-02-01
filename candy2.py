'''
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

Example: 
1 3 3 
score : 4

1 3 3 3
score: 5
'''
class Solution(object):
    def candy(self, ratings):
            """
            :type ratings: List[int]
            :rtype: int
            """
            if len(ratings) == 1:
                return 1
            else:
                '''
                Same approach: But it traverses only once.
                Traverses from left to right and then from right to left simultaneously
                '''
                score = list()
                score = [1]*len(ratings)
                prev = ratings[0]
                idx = 1
                idy = len(ratings)-1
                while idx <= len(ratings)-1 and idy > 0:
                    if ratings[idx] > ratings[idx-1]:
                        score[idx] = max(score[idx], score[idx-1]+1)
                    if ratings[idy-1] > ratings[idy]:
                        score[idy-1] = max(score[idy-1], score[idy]+1)
                    idx += 1
                    idy -= 1
                print score
                return sum(score)
