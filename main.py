import sys
import random
# ********************* 3. Efficient Algorithms *********************
# an efficient algorithm has a single for-loop that goes through the input from left to right
# the code inside the loop is efficient so that each round in the loop takes O(1) time
# loops should not contain (other loops going through input, slow operations such as count and [:], slow func calls (sum, min, max) applied to entire input)

# Example: Stock Trading
# You are given the price of a stock for n days. Your task is figure out the highest profit you could have made if you had bought the stock on one day and sold it on another day.
# example arr: [3,7,5,1,4,6,2,3]
# example output: 5
# explanation: The highest profit is 6-1 achieved by buying on day3 and selling on day 5

# WRONG
def bestPriceMyAlg(prices: list): 
    # figure out the largest difference between two numbers and return that profit
    n = len(prices)
    largestDifference = prices[0]
    for i in range(1, n):
        currentPrice = prices[i]
        largestDifference = max(largestDifference, currentPrice - largestDifference)

    return largestDifference

# First MOOC ALG (0(n2))
def bestPrice(prices: list):
    n = len(prices)
    best = 0
    for i in range(n):
        for j in range(i + 1, n):
            best = max(best, prices[j] - prices[i])
    return best

# Second MOOC Alg (0(n2))
def bestPriceRefined(prices: list):
    n = len(prices)
    best = 0
    for i in range(n):
        min_price = min(prices[0:i+1])
        best = max(best, prices[i] - min_price)
    return best

def bestPriceOptomized(prices: list):
    n = len(prices)
    best = 0
    min_price = prices[0]
    for i in range(n):
        min_price = min(min_price, prices[i])
        best = max(best, prices[i] - min_price)
    return best

def isBestPriceOptomized():
    while True:
        n = random.randint(1, 20)
        prices = [random.randint(1, 10) for _ in range(n)]

        result_brute = bestPrice(prices)
        result_fast = bestPriceRefined(prices)

        print(prices, result_brute, result_fast)
    
        if result_brute != result_fast:
            print("ERROR")
            break

# Example: Bit String
# You are given a bit string consisting of the characters 0 and 1. How many ways can you select two positions in the bit string so that the left position contains the bit 0 and the right position contains the bit 1?
# Bit String "01001011"
# output: 12 such pairs of positons

def bitStringOptomized(bitString: str):
    n = len(bitString)
    result = 0
    zeros = 0
    for i in range(len(bitString)):
        if bitString[i] == '0':
            zeros += 1
        if bitString[i] == '1':
            result += zeros
    return result

print(bitStringOptomized("01001011"))

# Example: List Splitting
# You are given a list containing n integers. Your task is to count how many ways one can split the list into two parts so that both parts have the same total sum of elements.
# input: [1,-1,1,-1,1,-1,1,-1]
# output: 3
# explanation: split the list between pos 1 and 2, between 3 and 4, between pos 5 and 6

# Corrent
def listSplitsMyAlg(aList: list):
    n = len(aList)
    ways = 0
    for i in range(1, n):
        firstHalf = sum(aList[0:i])
        secondHalf = sum(aList[i:])
        if firstHalf == secondHalf:
            ways += 1

    return ways

def listSplitsRefined(aList: list):
    n = len(aList)
    ways = 0
    left_sum = 0
    for i in range(n - 1):
        left_sum += aList[i]
        right_sum = sum(aList[i+1:])
        if left_sum == right_sum:
            ways += 1

    return ways

def listSplitsOptomized(aList: list):
    n = len(aList)
    ways = 0
    left_sum = 0
    total_sum = sum(aList)
    for i in range(n - 1):
        left_sum += aList[i]
        right_sum = total_sum - left_sum
        if left_sum == right_sum:
            ways += 1
    return ways

# Example: SubLists
# You are given a list containing n integers. How many ways can we choose a sublist that contains exactly two distinct integers?
# input: [1, 2, 3, 3, 2, 2, 4, 2]
# output: 14

def count_lists(numbers):
    n = len(numbers)
    a = b = -1
    result = 0
    for i in range(1, n):
        if numbers[i] != numbers[i - 1]:
            if numbers[i] != numbers[a]:
                b = a
            a = i - 1
        result += a - b
    return result