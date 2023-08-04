# Palindrome – Mirrored Numbers (656 vs 656)
def palindrome(n):
    return str(n) == str(n)[::-1]


# Anagram – Same Letters
def check(s1, s2):
    if sorted(s1) == sorted(s2):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")


s1 = "listen"
s2 = "silent"
check(s1, s2)


# Pangram Check – Alphabet
def is_pangram(phrase):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in phrase:
            return False

    return True


is_pangram("The quick brown fox jumps over the lazy dog")


# Coin Check | Dynamic Programming 1D Row
def coinChange(coins, amount):
    tbl = [float("inf")] * (amount + 1)
    tbl[0] = 0  # To make things easier
    for i in range(1, amount + 1):  # i = index
        for coin in coins:  # coin
            print(f"i={i}  coin={coin}")
            if i >= coin:
                tbl[i] = min(tbl[i], tbl[i - coin] + 1)

        if tbl[i] == float("inf"):
            tbl[i] = 0

    if tbl[amount] == 0:
        return -1
    return tbl[amount]


print(coinChange([2, 5], 4))


# Buy and Sell Stocks I
def maxProfit(prices):
    if len(prices) == 0:
        return 0
    else:
        low = float("inf")
        profitmax = 0
        for price in prices:
            if price > low and price - low > profitmax:
                profitmax = price - low
            elif price < low:
                low = price

        return profitmax


print(maxProfit([7, 1, 5, 3, 6, 4]))


# Buy and Sell Stocks II
def maxProfit(self, prices):
    profitmax = 0
    if len(prices) == 0:
        return 0
    else:
        for i in range(1, len(prices)):
            if prices[i] - prices[i - 1] > 0:
                profitmax += prices[i] - prices[i - 1]

    return profitmax


# Reverse Integer
def reverse(x):
    s = str(abs(x))
    reversed = int(s[::-1])

    if reversed < -(2**31) or reversed > (2**31 - 1):
        return 0
    if x > 0:
        return reversed
    else:
        return reversed * -1


print(reverse(1231))


# Reverse Integer + Original ==> Palindrome
def reversDigits(num):
    return int(str(num)[::-1])


def isPalindrome(num):
    return reversDigits(num) == num


def ReverseandAdd(num):
    iterations = 0
    while True:
        iterations += 1
        rev_num = reversDigits(num)
        new_num = num + rev_num
        if isPalindrome(new_num) == True:
            return new_num
        if num > 4294967295 or iterations > 1000:
            return "No palindrome exist"


print(ReverseandAdd(2322))


# 0-1 Knapsack | Dynamic Programming with 2D Board
def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K[n][W]


val = [6, 10, 12]
wt = [1, 2, 3]
W = 5
n = len(val)
print(knapSack(W, wt, val, n))


# Binary Search
def binary_search(lst, item):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = low + high
        print(mid)
        guess = lst[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 3, 5, 6, 9]

print(binary_search(my_list, 6))
print(binary_search(my_list, -1))


def palindrome_test():
    x = input()
    y = input()
    if str(x) == str(y)[::-1]:  # Use class 'str()' to convert to string first
        print("Match")  # Then check if the other matches in reverse order[::-1]
    else:
        print("No Match")


def anagram_test(s1, s2):
    if sorted(s1) == sorted(s2):  # Use function 'sorted()' to sort the words in ascending order
        print("Pass")  # Check to see if they match...
    else:
        print("Fail")


s1 = "silent"
s2 = "listen"


def pangram_test(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in sentence:
            return "Fail"
    return "Pass"


sentence = "the quick brown fox jumps over the lazy dog"


def buy_sell_stock_1(prices):
    if len(prices) == 0:
        print("0")
    else:
        low = float("inf")
        profitmax = 0
        for price in prices:
            if price > low and price - low > profitmax:
                profitmax = price - low
            elif price < low:
                low = price
        return profitmax


prices = [7, 1, 5, 3, 6, 4]


def buy_sell_stock_2(prices):
    profitmax = 0
    if len(prices) == 0:
        return 0
    else:
        for i in range(1, len(prices)):
            if prices[i] - prices[i - 1] > 0:
                profitmax += prices[i] - prices[i - 1]
    return profitmax


def reverse(x):
    s = str(abs(x))
    reverse = int(s[::-1])
    return reverse


# In a list of n numbers, find the largest and 2nd largest number
def find_largest(lst):
    a = lst[0]
    b = None
    for i in range(1, len(lst)):
        if lst[i] > lst[i - 1]:
            b = a
            a = lst[i]
    return f"1st-largest = {a} | 2nd-largest = {b}"


# In a list of number, make even and odd list. Also return how many
# times a number occurs in the list.
def occurrences(lst):
    return [[num, lst.count(num)] for num in set(lst)]


def even_odd_and_occurrences(lst):
    evens, odds = list(), list()
    for num in lst:
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)
    evens_count = occurrences(evens)
    odds__count = occurrences(odds)
    return evens, evens_count, odds, odds__count


# Reverse the sequence of words seperated by spaces in a string,
def reverse_seq(seq):
    return " ".join(seq.split()[::-1])


# Run length encoding of string. See below for example:
# aaaaabbbccd => a5b3c2d1
# xyz => x1y1z1
def letter_encoding(seq):
    encoding = list()
    for char in sorted(set(seq)):
        encoding.append(char + str(seq.count(char)))
    print("".join(encoding))


# given an unsorted array, find the first occurrence of given number
def first_occurence(lst, n):
    for index, num in enumerate(sorted(lst)):
        if num == n:
            return index


lst = [1, 2, 3, 3, 4, 3, 4, 5, 6, 56, 7]


# two string are given had to find the missing string
# String one - "This is an example"
# String two - "is example"
# ans - This, an
def find_missing_string(str1, str2):
    missing_words = list()
    for word in str1.split():
        if word not in str2.split():
            missing_words.append(word)
    return missing_words


# Move all zereos to the end of an array
# 1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0 --> 1, 9, 8, 4, 2, 7, 6, 0, 0, 0, 0
def move_zeros_to_end(seq):
    y = seq.count(0)
    x = [num for num in seq if num != 0]
    return x + ([0] * y)


# Fibonacci Sequence, print the nth number in the sequence
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ...
def fib_nth(n):
    a = 0
    b = 1
    if n == 0:
        print(0)
    elif n == 1:
        print(1)
    else:
        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c
        print(b)


def fib_seq(n):
    a = 0
    b = 1
    seq = [a, b]
    if n == a:
        return seq.pop(b)
    elif n == b:
        return seq
    else:
        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c
            seq.append(b)

        return seq
