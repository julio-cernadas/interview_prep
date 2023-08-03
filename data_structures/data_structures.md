# Data Structures

## Operations

---

### Inserts

With lists, it’s as easy as changing what the previous element points to.

But for arrays, you have to shift all the rest of the elements down.



### Deletes

Again, lists are better, because you just need to change what the previous element points to. 

With arrays, everything needs to be moved up when you delete an element.



### Traversing

**Traversing** means to search (visit) each vertex (node) in a specific order, the process of visiting a vertex can include both reading and updating it. As you traverse a graph, an unvisited vertex is undiscovered, yet after a visit the vertex becomes discovered.

The order of the searches determines the kind of search performed, algorithms are used in this sense. 



## Linear Structures

---

### General Concept

In python, a simple list can be used for all 4 types of linear structures. So just go with that unless told to do so.

### Arrays

#### Explanation

- Insert at end
- Index math. Two pointers, swapping
- Working with subarrays and matrices
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

#### Array vs Linked List

- Size of arrays is fixed, Linked Lists are dynamic.
- Inserting and deleting a new element in an array is expensive. Whereas both insertion and deletion can easily be done in Linked Lists (no movements of nodes required).
- Random access is not allowed in linked lists, you need to go through all the nodes that come before the node you need.
- Extra memory space for a pointer is required with each element of the linked list.
  



### Stacks

#### Explanation

- Think of a stack of plates!
- Stack is a linear data structure which the order LIFO are used for accessing elements.
- Operations include:
    - Push (inserts element at the top)
    - Pop (returns the top element, after removing it from the stack)
    - Peek (returns value of the first item without removing the element)
    - Swap (swap the two top most elements)
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
- Backtracking: at each point you store on choices, then backtracking means popping a next choice from the stack.

​    

### Queue

#### Explanation

- Think of a cafeteria line!
- Queue is a linear structure which follows the order FIFO to access elements.
- In a stack, we remove the most recent item (last in last out), but in a queue, we remove the least recently item (first in first out).
- Operations include:
    - En-Queue (insert item into the back of the queue)
    - De-Queue (remove item from the front of the queue)
    - Front (returns first element)
    - Rear (returns last element)
    

```python
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def peek(self):
        if not self.is_empty():
            return self.items[0]

    def size(self):
        return len(self.items)
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

* Patterns & Concepts:
    * How do we handle collisions?
    * Hash codes
    * Keys
* Operations:
    * Creation
    * Access
    * Contains
    * Delete

- Application:
    - Lookups
    - Counting how many times

#### Application

- Tbd



### Binary Search Tree

#### Explanation

A Binary Tree is where each node has 0 to 2 children, thus being binary (either no children or 2 children).

A Binary Search Tree is where, for each node, all items on the left are less than its value and all items on the right are greater. 

Thus this makes BST an easily understood balanced approach to storing the keys. BST tends to work best in situations in which you spend more time searching and less time building the tree. 

```python
class Node:
    def __init__(self, val, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

```

<img src="./assets/bst.png" style="zoom:75%;" />

#### Application

- Hierarchal data
- Perfect candidate to use recursion



### Tries

#### Explanation

Tbd

<img src="./assets/tries.png" style="zoom:75%;" />

#### Application

- String problems, is this a valid word or prefix
- Be comfortable with recursion



### Heaps

#### Explanation

Two types max and min heap. It is a great system for being able to continously extract the minimum or maximum value. 

Implemented as an array approach, which is more efficient and takes up less memory.

<img src="./assets/heap.png" style="zoom:50%;" />

<img src="./assets/heap_2.png" style="zoom:50%;" />

#### Application

- Whenever you need quick access to max or min.

    

### Graphs

#### Explanation

Directed and undirected graphs

```python
class Node:
  	pass
  

```

<img src="./assets/graphs_1.png" style="zoom:50%;" />

<img src="./assets/graphs_2.png" style="zoom:120%;" />

#### Application

- Relationships and routes



