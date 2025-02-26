import sys
import random

# ********************* 6. Own DS *********************

class Stack:
    def __init__(self):
        self.array: list = []
    
    def push(self, element):
        self.array.append(element)
    
    def pop(self):
        if len(self.array) == 0:
            raise IndexError("pop from empty stack")
        return self.array.pop()

    def top(self):
        if len(self.array) == 0:
            raise IndexError("top from empty stack")
        return self.array[-1]
    
    def __repr__(self):
        return str(self.array)

    def __len__(self):
        return len(self.array)

def useStack():
    stack = Stack()
    stack.push(10)
    stack.push(20)
    print(stack)
    print(f"Removing Pop: {stack.pop()}")
    print(len(stack))

useStack()

# ********************* 5. Sorting *********************
# --- arr.sort() => in place sorting
# --- sorted(arr) => returns a sorted array
# --- arr.sort(key=abs) => sorts according to a key
# def cmp(a, b):
#    print("compare", a, b)
#    return a - b
#
# numbers = [4, 1, 3, 2]
# numbers.sort(key=functools.cmp_to_key(cmp))

def restaurantSet(arrivals: list, departures: list):
    # find the highest number of customers in rhe rest at the same tmime
    # if a customer departs at the same moment another arrives you are in the rest at the same moment

    # store the target customers in some array (customers are represented by the index)
    events = []
    for time in arrivals:
        events.append((time, 1))
    for time in departures:
        events.append((time, 2))
    print(events)
    events.sort()
    print(events)
    counter = 0
    result = 0
    for event in events:
        if event[1] == 1:
            counter += 1
        if event[1] == 2:
            counter -= 1
        result = max(result, counter)
    return result

    
class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __lt__(self, other):
        return (self.x, self.y) < (other.x, other.y)

    def __repr__(self):
        return str((self.x, self.y))

def hashingVSorting(numbers: list):
    return len(set(numbers))

def smallestNumbers(numbers: list):
    n = len(numbers)
    numbers = sorted(numbers)
    result = float('inf')
    for i in range(1, n):
        before = numbers[i - 1]
        after = numbers[i]
        result = min(result, after - before)
    print(result)


# ********************* 4. Hashing *********************
# Sets: All operations (add, in, remove) is O(1) because of hashing
# dicts: adding, acessing, and removing data is all 0(1)


# Common Ways To Use A Dictionary 

#1. Has an element occured
def hasElementOccuredHashing():
    # dicts
    seen = dict()
    for x in [1, 2, 3]:
        seen[x] = True

    # Sets
    seen = set()
    for x in [1, 2, 3]:
        seen.add(x)

#2. Has an element occured
def countingOccurences():
    count = {}
    for x in [1, 2, 3, 3]:
        if x not in count:
            count[x] = 0
        count[x] += 1
#3. Position of occurence
def posOfOccurence():
    pos = {}
    for index, element in enumerate([1, 2, 3, 4, 4]):
        pos[index] = element

# Example. how many numbers?

def howManyNumbersMyAlg(numbers: list):
    return len(set(numbers))

# Example: Mode

def findModeHashingMyAlg(numbers: list):
    mostFreq = numbers[0]
    freq = dict()
    for number in numbers:
        if number not in freq:
            freq[number] = 0
        freq[number] += 1
        
        if freq[number] > freq[mostFreq]:
            mostFreq = number
    print(mostFreq)

# Example. Rounds

def rounds(numbers: list):
    # collecting numbers from smallest to largest in n rounds
    n = len(numbers)
    pos = {}
    for i, x in enumerate(numbers):
        pos[x] = i
        
    rounds = 1
    for i in range(1, n):
        if pos[i + 1] < pos[i]:
            rounds += 1



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