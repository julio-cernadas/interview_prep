# Data Structures

## Operations

---

### Inserts

With linked lists, it’s as easy as changing what the previous element points to.

But for arrays, you have to shift all the rest of the elements down.



### Deletes

Again, linked lists are better, because you just need to change what the previous element points to. 

With arrays, everything needs to be moved up when you delete an element.



### Traversing

**Traversing** means to search (visit) each vertex (node) in a specific order, the process of visiting a vertex can include both reading and updating it. As you traverse a graph, an unvisited vertex is undiscovered, yet after a visit the vertex becomes discovered. The order of the searches determines the kind of search performed, algorithms are used in this sense. 



## Linear Structures

---

### General Concept

In python, a simple list can be used for all 4 types of linear structures. So just go with that unless told to do so.

### Arrays

#### Explanation

- Insert at end
- Index math. Two pointers, swapping
- Subarrays and matrices
- Hash tables

```      python
matrix[col][row]
```

#### Application

- 2D arrays: creation, indexing, etc
- Sorting
- Get min & max
- Partioning, merging, slicing
- List comprehension, lambda, reduce, map, filter, etc



### Linked List

#### Explanation

- A linked list is like a chain of nodes, where each unit referred to as a node (data + pointer) contains information like data and a pointer to the next node in the chain.
- There’s a head pointer, which points to the first element of the linked list. If the list is empty then it simply points to null or nothing.
- Dynamic memory allocation is referred for linked lists
- First Node is called the Head, Last Node is called the Tail
- Used to implement file systems, stacks, queues, hash tables, graphs and trees.
- Types of linked lists:
       - Singly Linked List (Unidirectional): Here each node in the list stores the contents of the node and a pointer to the next node in the list. It does not store any pointer to the previous node.
       - Doubly Linked List (Bi-directional): These contain a pointer to the previous node and the next node.
- Strengths:
    - Fast operations on the ends, adding items at either end is 0(1) time.
    - You don’t need to know the size in advance. The more elements you add, the bigger the chain gets.

```python
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
```



#### Array vs Linked List

- Size of arrays is fixed, Linked Lists are dynamic.
- Inserting and deleting a new element in an array is expensive. Whereas both insertion and deletion can easily be done in Linked Lists (no movements of nodes required).
- Reading is faster with Araray. Random access is not allowed in linked lists, you need to go through all the nodes that come before the node you need.
- Array uses less memory. Extra memory space for a pointer is required with each element of the linked list.
  



### Stacks

#### Explanation

- Think of a stack of plates!
- Stack is a linear data structure which the order LIFO are used for accessing elements.
- Operations include:
    - Push (inserts element at the top)
    - Pop (returns the top element, after removing it from the stack)
    - Peek (returns value of the first item without removing the element)
    - isEmpty (returns true if empty)
    

```python
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)
```

#### Application

- Used to reverse our work.
- Is balanced. 
- Reverse an array: you push a given word to stack, letter-by-letter, then pop letters from the stack into an array or list.
- Undo Mechanism in Text Editors: keeping all text changes in a stack.
- Backtracking: at each point you store choices, then backtracking means popping a previous choice from the stack.

​    

### Queue

#### Explanation

- Think of a cafeteria line!
- Queue is a linear structure which follows the order FIFO to access elements.
- Operations include:
    - En-Queue (insert item into the back of the queue)
    - De-Queue (remove item from the front of the queue)
    - Front (returns first element)
    - Rear (returns last element)
    - isEmpty (returns true if empty)
    

```python
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def front(self):
        if not self.is_empty():
            return self.items[0]
      
    def is_empty(self):
        return len(self.items) == 0
```

#### Application

- Process items in the order they appear.
- Print Queues
- Call center phone systems
- In a multitasking operating system, the CPU cannot run all jobs at once, so jobs must be scheduled or queued.
- Breadth first search in a graph; an algorithm for traversing or searching graph data structures. It starts at some arbitrary node of the graph and explores the neighbor nodes first, before moving to the next level neighbors.



## Non-Linear Structures

---

### Hash Maps

#### Explanation

Also known as dictionary in Python.

First understand a hash function, which is where you input a string and get back a number (hash). Combining hash function with arrays gives you a hash map (or also called hash table).

Hash tables have really fast search, insert, and delete.

Collisions are bad. You need a hash function that minimizes collisions.

#### Application

- Use hash maps for caching.
- Lookups by key
- Counting how many times, great for catching duplicates



### Binary Search Tree

#### Explanation

A Binary Tree is where each node has 0 to 2 children, thus being binary (either no children or 2 children). 

A Binary Search Tree is where, for each node, all children on the left are lesser and on the right are greater.

Thus this makes BST an easily understood balanced approach to storing the keys. BST tends to work best in situations in which you spend more time searching and less time building the tree. 

```python
class Node:
    def __init__(self, key, left=None, right=None):
        self.left = left
        self.right = right
        self.val = key
```



<img src="./assets/bst.png" style="zoom:75%;" />

#### Application

- Hierarchal data
- Perfect candidate to use recursion



### Tries

#### Explanation

An ordered tree data structure that is used to store a dynamic set or associative array where the keys are usually strings. Unlike a binary search tree, no node in the tree stores the key associated with that node; instead, its position in the tree defines the key with which it is associated.

<img src="./assets/tries.png" style="zoom:75%;" />

```python
class TrieNode:
    def __init__(self, char: str):
        self.char = char
        self.is_end = False
        self.counter = 0
        self.children = {}
```

#### Application

- String problems, is this a valid word or prefix
- Be comfortable with recursion
- Spell check
- Autocomplete suggestions



### Heaps

#### Explanation

A special type of binary tree. There are two types max and min heap.

It is a great system for being able to continously extract the minimum or maximum value. 

Implement as an array approach, which is more efficient and takes up less memory.

<img src="./assets/heap.png" style="zoom:50%;" />

<img src="./assets/heap_2.png" style="zoom:50%;" />

#### Application

- Whenever you need quick access to max or min.

    

### Graphs

#### Explanation

There are two types of graphs: 

- Directed - the relationship is only one way
- Undirected - the relationship is both ways

Graphs are made up of nodes (vertices) and edges. A node can be directly connected to many other nodes. Those nodes are called its *neighbors*. Graphs are a way to model how different things are connected to one another.

<img src="./assets/graphs_1.png" style="zoom:50%;" />

<img src="./assets/graphs_2.png" style="zoom:120%;" />

#### Application

- Relationships and routes



