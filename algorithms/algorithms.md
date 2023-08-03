# Algorithms
1. Logarithm (Complexity Analysis)
2. Graph Traversals (BFS & DFS)
3. Binary Search
4. Sliding Window
5. Recursion
6. 2 Algorithms (Inverting a binary tree & Reverse a Linked List)
7. Suffix Trees
8. Heaps
9. Dynamic Programming
10. Sorting Algorithms (Quick & Merge)



## Problem Solving

------

### Seven Steps

1. Listen for clues, you'll receive vital details 
2. Draw an example: large and generic (avoid special cases)
3. Try brute force
4. Then optimize
5. Walk through algo, before you code
6. Code
7. Verification

### Tips & Tricks

- Don't just dive in. Make sure you know the little details (i.e algo details, data structures, indices, etc).

- Use the built in features of your programming language! Ask for permission though.

- Think about error cases, boundary checks, etc.

### Verification

- Don't just dive in
- Check for hot spots, high risk lines:
    - Math
    - Moving indices
    - Parameters when calling recursion
    - Bases cases
- Test cases:
    - Small test cases first
    - Edge cases



## Big O Notation

---

### What is it Big O

It's about how your algo scales. N = number of inputs, function output = total number of operations required. 

In other words it provides a way to analyze the efficiency of algorithms as the input size grows. Big O specifically describes the worst-case scenario, and can be used to describe the execution time required or the space used (e.g. in memory or on disk) by an algorithm.

### Rules & Tips

- Include all functions/operations
- Define the variables you need
- Adding vs multiplying
- We drop constants
- Remember the call stack  
- Drop non-dominant terms:
    - O(n + n^2) = O(n^2)
    - O(n^5 + n^2) = O(n^5)
    - O(2^n + n^2) = O(2^n)
    - O(k + n^2) = O(k + n^2)

### O(1)  Constant Time

Describes an algorithm that will always **execute in the same time** (or space) regardless of the size of the input data set.

```python
def returns_null(lst):
  	return null
```

### O(n) Linear Time

Operations grow with the input in a 1:1 ratio. A typical example is **iteration**.

```java
bool iterateThenReturn(IList<string> elements, string value) {
    foreach (var element in elements) {
        if (element == value) return true;
    }
    return false;
}
```

### O(n k) Linear Time V2

This is where we have a single loop and then a nested loop that is limited to the range of the underlying iteration element.

### O(n^2) Quadratic Time 

Operations are directly proportional to the square of the size of the input data set. This is common with algos that involve nested iterations over the data set. The power number is proportional to the number of nested iterations, so this can eventually become Cubic complexity too. This includes some less efficient ordering alogirthms such as: bubble sort, selection sort, and insertion sort. 

```java
bool ContainsDuplicates(IList<string> elements) {
    for (var outer = 0; outer < elements.Count; outer++) {
        for (var inner = 0; inner < elements.Count; inner++) {
            if (outer == inner) continue;
            if (elements[outer] == elements[inner]) return true;
        }
    }
    return false;
}
```

### O(2^n) Exponential Time 

Operations growth doubles with each addition to the input data set. The operations growth is exponential, starting off shallow and then rising significantly. A typical example of this is the recursive calculations of Fibonacci numbers. 

```java
int Fibonacci(int number) {
    if (number <= 1) return number;
    return Fibonacci(number - 2) + Fibonacci(number - 1);
}
```

### O(log n) Logarithmic Time 

**Logarithms** - logs are the flip of exponentials. How many 10s do we multiply together to get 100? The answer is 2: 10 × 10. So log base 10 100 = 2

The number of operations grows at a slower rate than the input. However, it requires many operations during initial processing followed by continously less as the input grows, following the same shape of logarithmic graph equation. This makes the algorithm less efficient with small inputs but very efficient with larger ones. A typical example is a **binary search**. 

### O(n log n) Linearithmic Complexity 

Complexity is a mix between logarithmic and linear complexity. It is typical of some smart algorithms used to order data, such as Mergesort, Heapsort, and Quicksort. 

<img src="./assets/big_o.png" style="zoom:50%;" />

<img src="./assets/big_o_performance.png" style="zoom:50%;" />



## Recursion

------

### Complexity

Time Complexity - at least O(n) but could get into O(2^n)

Space Complexity - recursions takes up a lot of memory

### **Base & Recursive Case**

When you write a recursive function, you have to tell it when to stop recursing. That’s why *every recursive function has two parts: the base case, and the recursive case.* The recursive case is when the function calls itself. The base case is when the function doesn’t call itself again ... so it doesn’t go into an infinite loop.

### The Call Stack

Your computer uses a stack internally called the call stack. This is important when doing recursion.

```python
def countdown(i):
  	print(i)
		if i <= 0: 		# Base case 
    		return
		else: 				# Recursive case 
    		countdown(i-1)
```

### Applications

- Choices. Do I go left or right? Which should I try first?
- Superlatives. Biggest, longest, shortest?
- Divide and conquer. Can you solve for parts separately?
- Fibonacci

```python
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
```

### 

## Sorting

------

### Typical Applications

- Getting Nth biggest or smallest
- Order ascending or descending



### Bubble Sort 

#### Complexity 

O(n^2)

#### Explanation

Walk through array, comparing pairs. If out of order, swap. Repeat until array is sorted.

```python
arr = [9, 5, 7, 4, 2, 8, 1, 10, 6, 3]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
```

<img src="./assets/bubble_sort.png" style="zoom:70%;" />



### Merge Sort 

#### Complexity 

O(n log n)

#### Explanation

This applys the divide and conquer approach. The sort begins by breaking the dataset into individual pieces and sorting the pieces. It then merges the pieces in a manner that ensures that it has sorted the merged piece. The sorting and merging continues until the entire dataset is again a single piece. 

Keep halving an array until it consists of only one element, then take the smallest element between two adjacent subarrays and repeat until all the elements are taken, resulting in a sorted subarray, the process is repeated until all elements are sorted.

```python
# Time Complexity - O(n log n)
data = [9, 5, 7, 4, 2, 8, 1, 10, 6, 3]

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left_half = merge_sort(arr[:middle])
    right_half = merge_sort(arr[middle:])

    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1

    merged.extend(left[left_idx:])
    merged.extend(right[right_idx:])
    return merged


mergeSort(data)
```

<img src="./assets/merge_sort.png" style="zoom:20%;" />



### Quick Sort 

#### Complexity 

Average-case time complexity of O(n log n)

Worst-case time complexity of O(n^2)

#### Explanation

Considered one of the fastest methods of sorting data. Start with the left most element as the pivot point. We then compare each next element with the pivot point. When we find the smaller element, we move it to the left; moving is performed by swapping the element with the first element after the pivot point, and then swapping the pivot point with the element after it. We then take all the points to the left and right and call the same quicksort function.

The key process in quickSort is partition(). Target of partitions is, given an array and an element x of array as pivot, put x at its correct position in sorted array and put all smaller elements (smaller than x) before x, and put all greater elements (greater than x) after x. All this should be done in linear time.

```python
data = [9, 5, 7, 4, 2, 8, 1, 10, 6, 3]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

quickSort(data, 0, len(data)-1)
```

<img src="./assets/quick_sort.png" style="zoom:70%;" />



## Traversal

------

### Binary Tree Traversal

Pre-Order

Post-Order

In-Order



## Searching

------

### Binary Search 

#### Explanation

Its input is a sorted list of elements, this is required otherwise won't work. With binary search, you guess the middle number and eliminate half the remaining numbers every time. It takes two inputs, the sorted array and an item to search. If the item is in the array it returns the position (index), otherwise returns null.

- First you get the low and high index
- For each iteration, you'll take the middle position between the low and high, this is called the guess
- If the guess is correct your return, otherwise:
    - If guess is larger than target item, you make the high = mid - 1, this is to exclude the already processed high point
    - If guess is smaller than target item, you make the low = mid + 1, this is to exclude the already processed high point

```python
def binary_search(lst,item):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) / 2
        guess = lst[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1,3,5,6,9]

print(binary_search(my_list,6))
print(binary_search(my_list,-1))
```

<img src="./assets/binary_search.png" style="zoom:60%;" />

#### Application

- Sorted data as input.
- Guesses can be over / under estimated.



### Depth First Search 

#### **Explanation**

Search each node in graph as deep as you can fore visiting its neighbors

Use a hash map or flag to mark visited nodes.

Challenges - you might go really deep, when there is actually a really obvious one

<img src="./assets/dfs.png" style="zoom:70%;" />

#### **Application**

- Relationships between items



### Breadth First Search 

#### **Explanation**

Finds the shortest path, leverages a queue to keep track of nodes.

<img src="./assets/bfs.png" style="zoom:70%;" />

#### **Application**

- Relationships between items



## Greedy Algorithms

------

### **Explanation**

We make a decision based on what we know right now, and don't care about what happens down the road.

Best seen in contrast to dynamic programming.

### **Application**

Tbd

