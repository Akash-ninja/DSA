# Data Structure and Algorithms

This repository is dedicated for -

- learning data structure fundamentals in popular languages (C, C++, Java, JavaScript, Python)
- learning proven patterns to solve problems in DSA
- centralized place for storing various problems and solutions encountered in Interviews and Coding competitive platforms.

## For running code -

For any lanuages, install this extension to run code in VS code easily -

**Code Runner** </br>
VS Marketplace Link: <https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner>

Except in one case for python wherein you need to run differently -
For example, there is a file named stack_using_linked_list.py

Standing in root i.e., Python/, you need to run - </br>
`python -m Stack.fundamentals.stack_using_linked_list` </br>
because of its importing system

### Some points about Python

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

### 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a new branch (git checkout -b feature-branch)
3. Commit your changes (git commit -m "Added a new feature")
4. Push to your branch (git push origin feature-branch)
5. Open a Pull Request
