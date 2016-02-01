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
                # Initially, all the scores of each rating is initialized to 1
                # traverse from left to right and find the new score for each element
                # If the two elements are in increasing order,
                # update the second element's score by first element's score + 1
                # if a < b
                # score[b] = score[a] + 1
                score = list()
                score = [1]*len(ratings)
                prev = ratings[0]
                idx = 1
                while idx <= len(ratings)-1:
                    current = ratings[idx]
                    if prev < current:
                        score[idx] = score[idx-1]+1
                    prev = current
                    idx += 1
                # now traverse from right to left and find the real score
                # same approach. If a > b then store the score of a = max(score[a] , score[b]+1)
                # finally sum the output.
                idx = len(ratings)-1
                candies = 1
                total_candies = 1
                while idx > 0:
                    idy = idx - 1
                    if idy < 0:
                        idy = idx+1
                    current = ratings[idx]
                    prev = ratings[idy]
                    #print current, prev
                    if prev > current:
                        score[idx-1] = max(score[idx]+1, score[idx-1])
                    idx -= 1
                #print score
                return sum(score)
