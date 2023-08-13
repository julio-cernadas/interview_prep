# Algorithms
## Problem Solving

------

### Seven Steps

1. Listen for clues, you'll hear big details from interviewer
2. Confirm your understanding, provide i/o examples
3. Describe your approach - data structure type, algorithm type
4. Walk through algo, before you code
5. Write your code
6. Verification
7. Optimization

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

### O(1) Constant Time

An algorithm that will always **execute in the same time** (or space) regardless of the size of the input data set.

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

There is single loop iteration and then a nested loop that is limited to the range of the underlying iteration element.

### O(n^2) Quadratic Time 

Operations are directly proportional to the square of the size of the input data set. This is common with algos that involve nested iterations over the data set. The power number is proportional to the number of nested iterations, so this can eventually become Cubic complexity too. This includes some less efficient ordering algorithms such as: bubble sort, selection sort, and insertion sort.

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

Space Complexity - recursions takes up a lot of memory, 1000 calls is max for Python.

### Explanation

A *recursive* thing is something whose definition includes itself. That is, it has a self-referential definition. To identify a recursive solution, first identify the recursive case and the base case. 

You can take a top-down approach by breaking the problem into subproblems that are similar to the original problem but smaller; this is your *recursive case*. 

Then consider when the subproblems are small enough to have a trivial answer; this is your *base case*. Your recursive function may have more than one recursive case or base case, but all recursive functions will always have at least one recursive case and at least one base case.

Always answer the following questions to generate a recursive solution:

1. **What is the base case?**
2. **What argument is passed to the recursive function call?** 
3. **How does this argument become closer to the base case?**

### **Base & Recursive Case**

When you write a recursive function, you have to tell it when to stop recursing. That’s why *every recursive function has two parts: the base case, and the recursive case.* 

The base case is when the function doesn’t call itself again... so it doesn’t go into an infinite loop. The important thing to know is that reaching the base case doesn’t necessarily mean reaching the end of the recursive algorithm. It only means the base case won’t continue to make recursive calls (for the passed parameters).

The recursive case is when the function calls itself. The recursive case can be split into 2 (sometimes 3) parts: 

- The code before the recursive call
- The code between the recursive calls (in case you run more than one recursive call)
- The code after the recursive call

### The Call Stack

Your computer uses a stack internally called the call stack. This is important when doing recursion.

Every time a function call is made, a new frame object with information related to the call (such as local variables and a return address for the execution to move to when the function returns) is added to the call stack. The call stack, being a stack data structure, can be altered only by having data added to or removed from its “top.”

<img src="./assets/recursion.png" style="zoom:25%;" />



### Applications

Three features of a programming problem, when present, make it especially suitable to a recursive approach:

- It involves a tree-like structure.
- It involves backtracking.
- It isn’t so deeply recursive as to potentially cause a stack overflow.

A tree has a *self-similar* structure: the branching points look similar to the root of a smaller subtree. Recursion often deals with self-similarity and problems that can be divided into smaller, similar subproblems. The root of the tree is analogous to the first call to a recursive function, the branching points are analogous to recursive cases, and the leaves are analogous to the base cases where no more recursive calls are made.

A maze is also a good example of a problem that has a tree-like structure and requires backtracking. In a maze, the branching points occur wherever you must pick one of many paths to follow. If you reach a dead end, you’ve encountered the base case. You must then backtrack to a previous branching point to select a different path to follow.

Another example is a filesystem, which has a tree-like structure; the subfolders look like the root folders of a smaller filesystem. Searching for a specific filename in a folder is a recursive problem: you search the folder and then recursively search the folder’s subfolders. Folders with no subfolders are the base cases that cause the recursive searching to stop. If your recursive algorithm doesn’t find the filename it’s looking for, it backtracks to a previous parent folder and continues searching from there.

Other applications include:

- Permutations and Combinations
- Path Finding
- Graph Traversal
- Matrix Traversal

### Strategies

**Head & Tail Approach** - this technique splits the recursive function’s array argument into two parts: the *head* (the first element of the array) and the *tail* (a new array including everything after the first element).

**Backtracking & Tree Traversal Algorithms** - a recursive function call is analogous to traversing to a child node in a tree, while returning from a recursive function call is analogous to backtracking to a previous parent node. Backtracking can be thought of as a selective tree / graph traversal method. At each node, we eliminate choices that are obviously not possible and proceed to recursively check only those that have potential. This way, at each depth of the tree, we mitigate the number of choices to consider in the future.

<img src="./assets/backtracking.png" style="zoom:50%;" />

**Divide & Conquer Algorithms** - split large problems into smaller subproblems, then divide those subproblems into ones that are smaller yet, until they become trivial to conquer. One benefit of this approach is that these problems can be worked on in parallel, allowing multiple central processing unit (CPU) cores or computers to work on them.

**Permutations & Combinations** -  *permutation* of a set is a specific ordering of all elements in the set. A *combination* is a selection of elements of a set. Keep in mind that, both with and without repetition, you can think of permutation as a certain arrangement of all elements in a set, while a combination is an orderless selection of certain elements from a set. Permutations have an ordering and use all the elements from a set, while combinations don’t have an ordering and use any number of elements from a set. 

<img src="./assets/permutations_combinations.png" style="zoom:100%;" />

<img src="./assets/permutations_combo_calc.png" style="zoom:100%;" />

### Warning

Avoid **Tail Call Optimization** - never use it in your code. 

To make use of tail call optimization, a function must use tail recursion. In tail recursion, the recursive function call is the last action of a recursive function. In code, this looks like a `return` statement returning the results of a recursive call.



## Sorting

------

### Typical Applications

- Getting Nth biggest or smallest
- Order ascending or descending



### Bubble Sort

#### Complexity

Time: O(n^2)

#### Explanation

Walk through array, comparing pairs. If out of order, swap. Repeat until array is sorted.

<img src="./assets/bubble_sort.png" style="zoom: 50%;" />



### Merge Sort 

#### Complexity 

Time: O(n log n)

#### Explanation

This applys the divide and conquer approach. The sort begins by breaking the dataset into individual pieces and sorting the pieces. It then merges the pieces in a manner that ensures that it has sorted the merged piece. The sorting and merging continues until the entire dataset is again a single piece. 

Keep halving an array until it consists of only one element, then take the smallest element between two adjacent subarrays and repeat until all the elements are taken, resulting in a sorted subarray, the process is repeated until all elements are sorted.

<img src="./assets/merge_sort.png" style="zoom:20%;" />



### Quick Sort 

#### Complexity 

Average-case time complexity of O(n log n)

Worst-case time complexity of O(n^2)

#### Explanation

Divide and conquer approach, it finds the element called the Pivot which divides the array into two halves in such a way that elements in the left half are smaller than pivot and elements in the right are greater than the pivot.

The pivot is usually the last element of the list

We then recursively perform three steps:

- Bring the pivot to the middle index
- Quick sort the left part
- Quick sort the right part

<img src="./assets/quick_sort.png" style="zoom:70%;" />



## Searching

------

### Binary Search 

#### Complexity 

Time: O(log n)

Space: O(1)

#### Explanation

Its input is a sorted list of elements, this is required otherwise won't work. With binary search, you guess the middle number and eliminate half the remaining numbers every time. It takes two inputs, the sorted array and an item to search. If the item is in the array it returns the position (index), otherwise returns null.

- First you get the low and high index
- For each iteration, you'll take the middle position between the low and high, this is called the guess
- If the guess is correct your return, otherwise:
    - If guess is larger than target item, you make the high = mid - 1, this is to exclude the already processed high point
    - If guess is smaller than target item, you make the low = mid + 1, this is to exclude the already processed high point

<img src="./assets/binary_search.png" style="zoom:60%;" />

#### Application

- Sorted data as input.
- Guesses can be over / under estimated.



### Depth First Search 

#### Complexity 

Time: O(V + E), where V = vertices and E = edges

Space: O(H), where H = maximum height

#### **Explanation**

Can be applied to directed and undirected graphs.

Depth refers to vertical before horizontal. Search each node in graph as deep as you can before visiting its neighbors.

Use a hash map to mark visited nodes. Challenges - you might go really deep, when there is actually a really obvious one.

<img src="./assets/dfs.png" style="zoom:60%;" />

#### **Application**

- Relationships between items



### Breadth First Search 

#### Complexity 

Time: O(V + E), where V = vertices and E = edges

Space: O(V)

#### **Explanation**

Can be applied to directed and undirected graphs.

Breadth means broad or wide, meaning the algo will progress horizontally (same level) before we proceed vertically. 

It finds the shortest distance between two things, if there is one. And leverages a queue to keep track of nodes.

<img src="./assets/bfs.png" style="zoom:70%;" />

#### **Application**

- Relationships between items
- Fewest moves to an element



### Dijkstra Algorithm

#### **Explanation**

Applied for shortest path in weighted graphs. It has four steps:

1. Find the cheapest node. This is the node you can get to in the least amount of time.
2. Check whether there’s a cheaper path to the neighbors of this node. If so, update their costs.
3. Repeat until you’ve done this for every node in the graph.
4. Calculate the final path. 

Breadth means broad or wide, meaning the algo will progress horizontally (same level) before we proceed vertically. 

Dijkstra’s algorithm works when all the weights are positive. If you have negative weights, use the Bellman-Ford algorithm.

#### **Application**

- Shortest path between nodes for a weighted graph.



## Greedy Algorithms

------

### NP Complete Problems

NP-complete problems have no known fast solution. If you have an NP-complete problem, your best bet is to use an approximation algorithm. Greedy algorithms are easy to write and fast to run, so they make good approximation algorithms.

### **Explanation**

A greedy algorithm is simple: at each step, pick the locally optimal solution, and in the end you’re left with the globally optimal solution.

We make a decision based on what we know right now, and don't care about what happens down the road.

The algorithm is fast and efficient with time complexity of O(n log n) or O(n). Therefore applied in solving large-scale problems.

The search for optimal solution is done without repetition – the algorithm runs once.

<img src="./assets/greedy.png" style="zoom:30%;" />

#### **Application**

- Minimum coin change.



## Dynamic Programming

------

### **Explanation**

Dynamic programming is useful when you’re trying to optimize something given a constraint.

You can use dynamic programming when the problem can be broken into discrete subproblems, and they don’t depend on each other.

Some general tips follow:

- Every dynamic-programming solution involves a grid.
- The values in the cells are usually what you’re trying to optimize. 
- Each cell is a subproblem, so think about how you can divide your problem into subproblems. 

Memoization is the process of storing sub-problem results in a top-down approach. So we use hash tables (dictionaries) in DP.
