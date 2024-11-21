### Integers:

1 - careful with 0 and NoneType

```Python
 a = 0
 if a:
    print("won't enter here, but we want to as 0 is important to use")

 b = None
 if b: 
    print("won't enter here, as expected")

if a is not None:
    print("will enter here")

```  


### Lists / Hashes :

1 - Using from collections import defaultdict makes us able to access a key in the dict even if it doesn't exist

```Python
ans = defaultdict(list)    
ans['a'].append(1)  # No KeyError; 'a' is initialized with an empty list
print(ans)  # Output: {'a': [1]}  
```  
![1.png](../_resources/1.png)  
2 - Two hashes can be equal even if their elements aren't in order 

```Python
 {a:1, b:2} == {b:2, a :1} 
```  


3 - A list can't be stored in a set in python, because lists are  not hashable
hash based structures ( set, dicts ) require their elements to be hashable ( immutable )

4 - 
Immutable objects are objects whose content can't be changed
Hashable means an object has a fixed hash value during its lifetime and can be used as a key in dict or elements in sets

```Python
Hashable?    Mutable?
  Yes           No      --> str, int, float, tuple (if elements hashable), frozenset
  No            Yes     --> list, dict, set
```

SET REQUIRE ITS ELEMENTS TO BE HASHABLE/IMMUTABLE
DICT REQUIRE ITS KEYS TO BE HASHABLE/IMMUTABLE


5 - Difference Between for and while in Handling Changing Sizes:

* <span style="color: #26B260"> **for _ in range(len(...)):**

The len(...) is evaluated once at the start, and the loop runs a fixed number of iterations, even if the size of the underlying structure changes during the loop.

* <span style="color: #26B260">**while loop with len(...):**

The len(...) is re-evaluated on each iteration, so the loop dynamically adapts to changes in the size of the structure.


# Preserving order of dictionnary creation : 
In python 3.7 and later, sorted_dict will preserve the order given by the sorted function ( sroted sequence )
Before python 3.7, dictionnaries did not guarantee order preservation and sorted_dict might not preserve insertion order.


Instead of
```Python
sorted_dict = {
    k: v
    for k, v in sorted(counter.items(), key=lambda item: item[1], reverse=True)
}

```

Use:
```Python
sorted_items = sorted(counter.items(), key=lambda item: item[1], reverse=True)
res = [key for key, _ in sorted_items[:k]]
```

### Hashability VS Immutability 
1 - Hashability vs. Immutability
    - Hashability =/= Immutability and Immutability =/= Hashability.
    - Objects can be hashable but mutable ( default created classes )
    - Objects can be immutable but unhashable if they lack a proper __hash__() method ( definin __eq__ breaks __hash__ ( __hash__ = None))
    
2 - Default behavior in Python 
    - By default, user defined objects are hashable based on their identity ( id(), hashing function uses id ) making them usable in dictinnaries and sets even if they are mutable
    - if __eq__ is overriden, Python automatically disables __hash__ making the object unhashable to prevent inconsistencies

3 - Mutability and hashbility relationship
    - Mutable objects can be hashable if their hash is based on identity rather than content
    - Mutable objects are dangerous to use in hash based structures

4 - Immutability Considerations:
    - Python doesn't enforce immutability, private attributes (_var) are only a convention
    - True Immutability can be achieved using techniques @dataclass(frozen=True) or read only property with @property

```Python
    class ImmutableNode:
        def __init__(self, value):
            self._value = value # Encapsulation 
        
        @property
        def value(self):
            return self._value # Read only property
    
    node = ImmutableNode(10)
    node.value = 20 # AttributeError : can't set attribute 
```

5 - Best practices:
    - If objects should be hashable by content, explicitely define __hash__() and __eq__()
    - For reliable behavior in hash-based collections, favor immutability to prevent accidental modifications

### Python changes over versions
 Important Python Version Differences

Python 3 vs Python 2 differences: Integer division, print, unicode.
Python 3.6: F-strings, improved dict behavior.
Python 3.7: Dict order officially preserved, dataclasses.
Python 3.8: Walrus operator (:=), positional-only params.
Python 3.9: Union types (int | float), dict merge.
Python 3.10+: Pattern matching, performance improvements.

Current : Python 3.13.1

Use Python 3.7+ for coding interviews to leverage ordered dicts.


### Hashing 
Hashing is the technique used to map data to a fixed size value ( hash ), which allows efficient storage and retrieval in data structures like hashtables enabling O(1) lookups.

# Why O(1) lookup ?
1 . Key Hashing
2 . Index Calculation 
3 . Direct Access

# Common Hashing algos:
- MurMurHash
- SipHash ( cryptographic hash function used to prevent hash collision attacks )

# Collision Management
Chaining is a collision resolution technique where each slot in the hash table stores a linkedList of key value pairs that hash to the same index. If multiple keys produce the same hash, they are stored in the same slot but linked together.

Steps: 

    1 - Compute the hash and determine the index
    2 - If the index is empty, store the key value pair
    3 - If a collision occurs ( Index is occupied), append the new key value to a linked list at that index.
    4 - During the lookup, the algorithm searches the linked list at the index

Advantages of Chaining:

    Handles collisions efficiently without requiring table resizing.
    Easy to implement and extend with different data structures (e.g., linked lists, dynamic arrays).
    Good performance if the hash function evenly distributes keys.

Disadvantages of Chaining:

    Increased memory overhead due to pointers for linked lists.
    Lookup time degrades to O(n) in the worst case (when all keys hash to the same index).

Example of Chaining In action : 


```Python 
Index  |  Key-Value Pairs (Linked List)
---------------------------------------
  0    |  []
  1    |  []
  2    |  []
  3    |  [ ("apple", 50) → ("grape", 20) ]  # Collision handled by chaining
  4    |  []
  5    |  [ ("banana", 30) ]

```
The lookup for grape : 

    the hash value give the index 3, which has already another key
    compare apple with key => no match
    compare grape with key => match return V

pros:

    handles collisions 
    dynamic size ( without resizing of the table)

cons:

    Extra heap memory is required 
    Lookup degrades to O(n) in the worst case


### Sliding Window:

* 1 - Identify if "Fixed Window Size" or "Dynamic Window Size"
* 2 - Use left and right Pointer
* 3 - Maintain relevant info while iterating ( max frequency )
* 4 - Define a condition to adjust the sliding window 
Move left pointer forward till the sliding window satisfies the condition
* 5 - Update results once the sliding window is valid 

```Python
def sliding_window_problem(s, k):
    # Initialize pointers, result, and data structure for the window
    left = 0
    result = 0  # Example: maximum length
    window_data = {}  # Dictionary to track elements in the window
    
    for right in range(len(s)):  # Expand the window
        # Add the current element to the window
        char = s[right]
        window_data[char] = window_data.get(char, 0) + 1
        
        # Check and shrink the window if constraints are violated
        while condition_violated(window_data, k):
            left_char = s[left]
            window_data[left_char] -= 1
            if window_data[left_char] == 0:
                del window_data[left_char]
            left += 1  # Shrink the window
        
        # Update the result based on the current window
        result = max(result, right - left + 1)  # Example: max length
    
    return result

```

### BackTracking : 

Backtracking ensures correctness by enumerating all possibilities, and ensures efficiency by never visiting a state more than once.

Most backtracking solutions can be formulated by adjusting the following pseudocode template:


```Python
def backtrack(candidate):
    if is_valid_solution(candidate):
        output(candidate)
        return
    
    # iterate all possible candidates.
    for next_candidate in list_of_candidates:
        if is_valid(next_candidate):
            # try this partial candidate solution
            place(next_candidate)
            # given the candidate, explore further.
            backtrack(next_candidate)
            # backtrack
            remove(next_candidate)
```

**The backtracking algorithm enumerates a set of partial candidates that, in principle, could be completed in various ways to give all the possible solutions to the given problem. These partial solutions can be represented as a nodes of a tree, called the space tree**.

**This tree is constructed in a recursive DFS manner**. Starting from the root, we try to extend a partial solution by adding to it an additional element. This is called the extension step. After the extension, we must consider whether to continue that path or not by checking two possibilities:

1.  It the new node constitutes a complete solution, we need to somehow keep track of it (for example store it somewhere or print it).
2.  **If the new node cannot be completed to a valid solution due to the violation of the problem constraints, the branch is abandoned**. This technique is called **pruning**.

**In both these cases, the algorithms needs to backtrack, meaning it goes back one step and explores another path from the previous point, which could lead to more solutions. The pruning step is the key to reducing the search time compared to a naive exhaustive search**.

### Monotonic Stack 
![monotonic_stack.png](/_resources/monotonic_stack.png)  

```Python
def monotonicIncreasing(nums):
    stack = []
    result = []

    # Traverse the array
    for num in nums:
        # While stack is not empty AND top of stack is more than the current element
        while stack and stack[-1] > num:
            # Pop the top element from the stack
            stack.pop()
        # Push the current element into the stack
        stack.append(num)

    # Construct the result array from the stack
    while stack:
        result.insert(0, stack.pop())

    return result

# Example usage:
nums = [3, 1, 4, 1, 5, 9, 2, 6]
result = monotonicIncreasing(nums)
print("Monotonic increasing stack:", result)
```

### Binary Search Template :

Suppose we have a search space. It could be an array, a range, etc. Usually it's sorted in ascend order. For most tasks, we can transform the requirement into the following generalized form:

Minimize k , s.t. condition(k) is True

```Python 
def binary_search(array) -> int:
    def condition(value) -> bool:
        pass

    left, right = 0, len(array)
    while left <= right:
        mid = (right + left) // 2
        if condition(mid):
            right = mid - 1
        else:
            left = mid + 1
    return left or high 
```



### Tree Traversal Techniques
![tree_traversal.png](/_resources/tree_traversal.png)  

![tree_traversal_2.png](/_resources/tree_traversal_2.png)  

* PreOrder    :   <span style="color: #26B260">**Root**</span>    ->  Left  ->    Right
* InOrder     :   Left    ->  <span style="color: #26B260">**Root**</span>  ->    Right
* PostOrder   :   Left    ->  Right  ->   <span style="color: #26B260"> **Root**</span>


* Binary Tree =/= Binary Search Tree

### Recursion :

* If you want to return a value and use recursion for it, you need to return the recursive calls of it 

```Python 
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0  # Initialize the counter

        def inorder(node):
            nonlocal count
            if node is None:
                return None
            
            # Traverse the left subtree
            left = inorder(node.left)
            if left is not None:
                return left  # If the left subtree returns a value, propagate it up
            
            # Increment the counter
            count += 1
            if count == k:
                return node.val  # Return the k-th smallest value
            
            # Traverse the right subtree
            return inorder(node.right)
        
        # Start the in-order traversal
        return inorder(root)
```

* If you want to call recursive function without the keyword return, you can use local variable or instance attributes to store the values, once the value is found, you can call " return "

```Python 
def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Initialize a counter and a variable to store the result
        self.count = 0
        self.result = None

        def inorder(node):
            # Base case: if the node is None, return
            if not node:
                return
            
            # Traverse the left subtree
            inorder(node.left)
            
            # Increment the counter
            self.count += 1
            
            # If count equals k, we've found the k-th smallest element
            if self.count == k:
                self.result = node.val
                return
            
            # Traverse the right subtree
            inorder(node.right)
        
        # Start the in-order traversal
        inorder(root)
        
        # After traversal, result should hold the k-th smallest element
        return self.result
```

or 

```Python 
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Initialize the counter and result variables
        count = 0
        result = None

        def inorder(node):
            nonlocal count, result
            if node is None or result is not None:
                return
            # Traverse the left subtree
            inorder(node.left)
            # Increment the counter
            count += 1
            # If count equals k, we've found the k-th smallest element
            if count == k:
                result = node.val
                return
            # Traverse the right subtree
            inorder(node.right)

        # Start the in-order traversal
        inorder(root)
        return result

```


## Python Gotcha's / Tricks:

### <span style="color: #26B260">Avoid mutable default arguments :

with the following code :

```Python
class WordDictionary:

    def __init__(self, children={}):
        self.children = children

```
the default value of children is a mutable dictionnary {}.
In python, default mutable arguments are shared accross all instances of the class.
It means that if you modify self.children in one instance of the class, the change will also be reflected in all other instances.

```Python
wd1 = WordDictionary()
wd2 = WordDictionary()

wd1.addWord("apple")  # Adds "apple" to wd1's Trie
wd2.addWord("banana")  # Supposed to add "banana" to wd2's Trie

print(wd1.children)  # {'a': {'p': {'p': {'l': {'e': {'*': {}}}}}}, 'b': {'a': {'n': {'a': {'n': {'a': {'*': {}}}}}}}}
print(wd2.children)  # Same as wd1.children!

```
The fix will be to use None as default value for the constructor 

```Python 
class WordDictionary:

    def __init__(self, children=None):
        self.children = children if children is not None else {}

```

When children=None, a new dictionary {} is created for each instance of WordDictionary.
This ensures that each instance of the class has its own independent children dictionary.

* Key Takeaway: Always use None to initialize an instance *

### <span style="color: #26B260">The use of is:

Use *==* to compare integers values, not *is*, unless you explicitly want to check identity ( id )

### <span style="color: #26B260">Default arguments are evaluated once, at function definition time, not at call time.

```Python
import datetime

def get_current_time(time=datetime.datetime.now()):
    return time

print(get_current_time())  # Returns the same time, even if called later

```
Fix : 

```Python
def get_current_time(time=None):
    if time is None:
        time = datetime.datetime.now()
    return time

```

### <span style="color: #26B260">+= and -= work with mutable objects only ( modifies the object in place)
```Python
lst = [1, 2, 3]
def append_value(a):
    a += [4]
append_value(lst)
print(lst)  # [1, 2, 3, 4]

```

```Python 
a = (1, 2, 3)  # Tuple (immutable)
def append_value(a):
    a += (4,)
append_value(a)
print(a)  # (1, 2, 3) (no modification)

```

### <span style="color: #26B260">Never modify a list while iterating

Modifiying a list while iterating will result in a wrong behavior, elements can be skipped
* Correct Solution 

#### <span style="color: #26B260">Use List Comprehension
```Python
numbers = [1, 2, 3, 4, 5, 6]
numbers = [num for num in numbers if num % 2 != 0]
print(numbers)  # Output: [1, 3, 5]

```


#### <span style="color: #26B260">Iterate over a copy 
```Python
numbers = [1, 2, 3, 4, 5, 6]
for num in numbers[:]:  # Iterate over a copy of the list
    if num % 2 == 0:
        numbers.remove(num)

print(numbers)  # Output: [1, 3, 5]

```

## If you want to store sets in a set:

use frozenset
```Python
nums = [1, 2, 3, 4, 3, 2]
target = 5
seen = set()
pairs = set()

for num in nums:
    complement = target - num
    if complement in seen:
        pairs.add(frozenset([num, complement]))
    seen.add(num)

print([list(pair) for pair in pairs])  # Output: [[2, 3], [1, 4]]

```

## if you want to store lists in set

Python does not have a built-in "frozen list" like frozenset for sets, but you can use a tuple as an immutable equivalent of a list. Tuples are hashable if they contain only hashable elements, so you can store them within a set or use them as dictionary keys.

```Python
# Original data
lists = [[1, 2], [2, 3], [1, 2]]

# Convert lists to tuples and store in a set
unique_tuples = set(tuple(lst) for lst in lists)

print(unique_tuples)  # Output: {(1, 2), (2, 3)}

# Convert back to lists if needed
unique_lists = [list(tpl) for tpl in unique_tuples]
print(unique_lists)  # Output: [[1, 2], [2, 3]]

```

Key Points

*   Use tuples when you need a "frozen list."
*   Tuples can contain mixed types, unlike frozenset, which requires all elements to be hashable.


## Nonlocal keyword

Python follows LEGB ( Local, Enclosing, Global, Built-in )

* nonlocal is needed when you do a reassignement inside a function to inform Python that you are refering the var inside the enclosing scope. 

If you are only doing a mutable operation on a variable on the local scope, you don't need to use nonlocal 

```Python
def outer():
    x = 10
    
    def inner():
        # This would throw an UnboundLocalError without nonlocal
        nonlocal x
        x += 1  # Rebinding x
        print(x)
    
    inner()
    print(x)

outer()

```



```Python
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None

        cloned = {}

        def dfs(node):
            cloned_node = Node(node.val)
            cloned[cloned_node.val] = cloned_node
            for child in node.neighbors:
                if child.val in cloned:
                    cloned_node.neighbors.append(cloned[child.val])
                else:
                    # clone it first
                    cloned_child = dfs(child)
                    cloned_node.neighbors.append(cloned_child)

            return cloned_node

        return dfs(node)

```

Key Points:

- No Reassignment: The dfs function does not reassign the cloned variable. Instead, it updates the dictionary (e.g., using cloned[cloned_node.val] = cloned_node), which is a mutable operation. Reassignment would require the nonlocal keyword.

- Enclosing Scope: The variable cloned is in the enclosing scope of the dfs function, making it accessible within dfs unless shadowed by a local variable.

- When nonlocal is Needed: If you needed to rebind cloned (e.g., cloned = {}) inside dfs, you would have to declare nonlocal cloned to inform Python that you are referring to the cloned in the enclosing scope. Without nonlocal, Python would assume cloned is a local variable, leading to an UnboundLocalError.

* Python passes references to mutable objects.


# Top Down Backtracking ( memoization )
- Solves the problem recursively by breaking it into smaller problems.
- Start from original problem -> explores smaller subproblems
- TC O(n * target)
- SC O(n × target) for memo table + O(n) recursion stack 
- recursive calls may invole stack overhead ( deep recursion trees )


# Bottom Up ( Tabulation using DP)
- Build the solution iteratively from smaller subproblems results to the full problem using a DP table 
- TC O(n * target)
- SC (target)
- Avoids recursion stack overrhead 


# Recursion stack vs heap in memory:

Memory is divided into two regions: The stack and the heap

| **Aspect**            | **Recursion Stack**                         | **Heap**                                   |
|------------------------|---------------------------------------------|-------------------------------------------|
| **Purpose**            | Stores function calls, local variables, and return addresses. | Stores dynamically allocated objects and data. |
| **Lifespan**           | Memory is automatically allocated and deallocated with function calls. | Memory persists until explicitly deallocated or garbage collected. |
| **Size**               | Limited (smaller than heap).               | Large (limited by system memory).         |
| **Management**         | Managed automatically by the language.     | May require manual management (not in Python). |
| **Performance**        | Fast due to direct memory access.          | Slower because it involves dynamic allocation. |
| **Error Risk**         | Stack overflow if recursion depth is too large. | Memory leaks if allocated memory isn’t properly freed. |


# Trees notes:

- In a binary tree with n nodes, there are at most n/2 leaf nodes.
## Height
- For a balanced binary tree, the height is O(log⁡(n)).
- for a skewed tree, the height is O(n)

## Recursion stack space:
- Skewed tree: O(n) space in call stack
- balanced tree O(log(n))


# Balanced Tree
![balanced.jpg](_resources/balanced.jpg)  

It is a type of BT in which the difference between the height of the left and right subtree of each node is  <= 1 ( either 0 or 1)

A Binary tree is balanced if the height of the tree is O(Log(n))
# Self Balancing Binary Search Trees 

Self Balancing Binary Search Tree are height balanced binary search trees that automatically keep thet height as small as possible when insertion and deletion operations

## AVL Tree
![avl.jpg](_resources/avl.jpg)  

an AVL tree is a regular binary search tree BST that is balanced 


# Advanced Graphs:

- A topological sort is a linear ordering of vertices such that for every directed edge (u,v), vertex u appears before vertex v in the ordering

- len(topological_sort) = number_vertices
- len(topological_sort_1) = len(topological_sort_2) for every topological sort


# Summary of CPU, Core, Logical Processor, Process, and Thread

### **Key Concepts**

| Element             | Description                                                      | Interaction with Others                                      |
|--------------------|------------------------------------------------------------------|--------------------------------------------------------------|
| **CPU (Processor)** | The physical chip that processes instructions; contains cores.   | Manages cores, executes processes, schedules tasks.           |
| **Core**            | Independent processing unit within a CPU.                        | Executes processes/threads; multiple cores enable parallelism.|
| **Logical Processor** | A virtual processor created via hyper-threading (SMT).          | Shares physical core resources to run multiple threads.       |
| **Process**         | An independent program with its own memory space.                 | Runs on cores, contains threads, does not share memory.       |
| **Thread**          | The smallest unit of execution within a process.                  | Shares memory within a process; runs on logical processors.   |

---

### **How They Interact**

1. **The CPU contains multiple cores**, allowing it to run multiple processes or threads concurrently.  
2. **Each core can run one or more threads** (with hyper-threading, it can handle multiple logical threads).  
3. **Processes run independently** and do not share memory, while **threads share memory** within a process.  
4. **The operating system schedules processes and threads** onto available cores/logical processors.  

---

### **Example Interaction Flow**
- A quad-core CPU with hyper-threading has **8 logical processors**.  
- It can run **multiple processes**, each having multiple threads.  
- The OS distributes these threads across logical processors for efficiency.



important materials : 

Creating the course 
Module Production 
How to test the prototype ( audience )
Infographic tool ( Produce diagram )
Databases of free images 

