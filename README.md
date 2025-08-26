# Data Structure and Algorithms

This repository is dedicated for -

- learning data structure fundamentals in popular languages (C, C++, Java, JavaScript, Python)
- learning proven patterns to solve problems in DSA
- centralized place for storing various problems and solutions encountered in Interviews and Coding competitive platforms.

***

## For running code -

For any lanuages, install this extension to run code in VS code easily -

**Code Runner** </br>
VS Marketplace Link: <https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner>

Except in one case for python wherein you need to run differently -
For example, there is a file named stack_using_linked_list.py

Standing in root i.e., Python/, you need to run - </br>
`python -m Stack.fundamentals.stack_using_linked_list` </br>
because of its importing system

***

### Some points about Python -

1. **Import system**-

   - Python has absolute and relative import system

   - Easily importing files which is nested inside folders is a bit of mess here.

2. About `__init__.py` file -

   - It is created intentionally here - to mark directories on disk as Python package directories.

   - If you remove the init.py file, Python will no longer look for submodules inside that directory, so attempts to import the module will fail.

3. Difference between python script, package and modules -

   **Module** - contains collections of functions and global variables </br>
   **Package** - Simple directory having collection of modules</br>
   **Script** - executed directly with main function in it.

***

### 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a new branch (git checkout -b feature-branch)
3. Commit your changes (git commit -m "Added a new feature")
4. Push to your branch (git push origin feature-branch)
5. Open a Pull Request

***

### List of Problems - 

1. **Array-**
```
1. Max-Consecutive Ones 
2. Best time to buy and sell a stock
3. Product of Array except self
4. Maximum Sum Subarray
5. Maximum Product Subarray
```

- **2D array(Matrix)-**
```
1. Set Matrix 0’s
2. Valid Sudoku
3. Rotate Array
4. Spiral Matrix
```

2. **Two Pointers-**
```
1. Trapping Rain Water
2. Two Sum II (Input array is sorted)
3. Container with Most Water
4. Valid Palindrome
```

3. **Sorting-**
```
1. Sort Colors
2. Majority Element
3. Move Zeroes 
4. Find the duplicate Number
```

4. **Linked list-**
```
1. Linked list operations (in fundamentals folder)
2. Linked list cycle
3. Linked list cycle II
4. Merge 2 sorted list
5. Reverse linked list
6. Palindrome linked list
7. Remove Nth node from End of list
8. Intersection of 2 linked list
```

5. **Hash Table-**
```
1. Two Sum 
2. Three sum
3. Valid Anagram
4. Longest consecutive sequence (time limit failing)
5. Contains duplicate
6. Group Anagrams
```

6. **Stacks-**
```
1. Stack as array (in-built language push, pop methods - no script)
2. Stack as linked list
3. Vali parenthesis
4. Min Stack
5. Next Greater Element II
6. Merge Intervals
```
