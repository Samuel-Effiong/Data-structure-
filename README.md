# Data-structure-
Implementing various data structure in python 
## Doubly Linked List Operations

This Python code implements a doubly linked list data structure along with additional features. The `DoublePointerNode` class represents the nodes in the doubly linked list, containing data and pointers to the next and previous nodes. The `DoublyLinkedList` class is the main implementation of the doubly linked list, providing various methods for operations like insertion, deletion, and traversal.

## Features to Implement
The code mentions several features yet to be implemented to enhance the performance and functionality of the linked list:

1. **Middle Node Detection:**
   - Implementing a `L.middle` variable to automatically detect the middle node in a list of length n, aiming to increase the speed of searching in a sorted linked list.

2. **List Concatenation:**
   - Ability to concatenate two different list instances to create a new list containing the values of both nodes.

3. **Sorting:**
   - Implement sorting functionality to arrange the values of a list in either increasing or decreasing order and return a new list containing the sorted values.

4. **More to Come:**
   - The code mentions that there are more functionalities to be added in the future.

## Classes

### DoublePointerNode
- Represents a node in the doubly linked list with data, a pointer to the next node (`_next`), and a pointer to the previous node (`_prev`).

### DoublyLinkedList
- Main class implementing the doubly linked list.
- Supports both simple and advanced interfaces for node manipulation.
- Provides methods for insertion at the beginning, end, and middle of the list.
- Allows deletion from the beginning, end, and middle of the list.
- Contains methods for checking if the list is empty and for obtaining the head and tail of the list.
- Inherits from the `DoublyLinkedList` class to create a more advanced `PositionalADT` class.

### PositionalADT
- An advanced version of the `DoublyLinkedList` class, providing a positional interface for node manipulation.
- Allows operations like getting the first and last elements, adding elements before or after a given position, and popping elements.
- Implements a special `__Position` class to encapsulate node positions and keep them hidden from the user.
- Inherits from the `DoublyLinkedList` class.

### Stack
- Inherits from `DoublyLinkedList` and represents a stack data structure.
- Implements methods for pushing (adding at the beginning), popping (removing from the beginning), and getting the top element.

### Queue
- Inherits from `DoublyLinkedList` and represents a queue data structure.
- Implements methods for enqueueing (adding at the end) and dequeuing (removing from the beginning).
- Overrides the `first` method to return the front element of the queue.

## Usage Guidelines
- The code allows two interfaces for node manipulation: a simple interface using data directly and an advanced interface using the `PositionalADT` class.
- Users can choose between the two interfaces based on their preference and performance requirements.

## Future Enhancements
- The code mentions plans to implement additional features, and the user is encouraged to explore further enhancements, particularly in the context of trees.
