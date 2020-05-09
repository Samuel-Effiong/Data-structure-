"""There is still lot of functionality to implement in it to improve the
performance of linked list operations. They include:
1) Having a L.middle variable: The list automatically detects the middle
node in length n node
to increase the speed of searching in sorted linked list 


2)You can add two different list instance together to create in new list
containing the values of both nodes

3) Sorting the values of a list in either increasing or decreasing values
and returning a new list containing the sorted list

4) And more to come

"""


class DoublePointerNode:
    def __init__(self, data):
        self._data = data
        self._next = None
        self._prev = None

    def get_data(self):
        return self._data

    def get_next(self):
        return self._next

    def returnself(self):
        return self

    def set_next(self, node):
        if isinstance(node, type(self)):
            self._next = node
        else:
            print("Invalid Node")

    def get_prev(self):
        return self._prev

    def set_prev(self, node):
        if isinstance(node, type(self)):
            self._prev = node
        else:
            print("Invalid Node")


class DoublyLinkedList:
    """Love Inheritance!!!"""

    def __init__(self, simple_interface=True):  # Shoud I use sentinel node?
        # Yes, I know sentinel nodes will make my life easier
        # But I love the challenge of not having to use it
        self._head = None
        self._tail = None
        self._simple_interface = simple_interface
        self._size = 0

    def __len__(self):
        return self._size

    def __str__(self):
        x = "A Linked List with nodes containing data and two pointer"
        return x

    def __iter__(self):
        if not self._simple_interface:
            x = self._head
            while x is not None:
                yield x
                x = x.get_next()

    def __add__(self):
        return "hey"

    def get_head(self):
        return self._head

    def _set_head(self, node):
        self._head = node

    def get_tail(self):
        return self._tail

    def get_state_of_list(self):
        return self._simple_interface

    """ I just made a significant change to the program!! Instead of the
user having to keep a copy of the long unique node instances to be able to
perform insertions, they can easily use the node data instead which is easier
to remember and cool huh.

Also the user doesn't have to instantiate the node, you just have to
supply the data itself and the code will instantiate it itself.

Both this altercation are useful for automated purposes



I give up... I will maintain two functionality in this program

first the user can access, insert and delete using the data value directly
as the parameter, this makes the operation simple and completely enscapulates
and restricts manipulating the inner workings but reduces the performance
to O(n)

Secondly the user can access, insert and delete using the __Position instance
of the node containing the data, the enscapulation is not as absolute as the
first instance as the user can access and manipulates the inner working of the
data (which I would not advice you to do so as to retain data integrity unless
you know what you are doing). But this method greatly increases the performance
of the operation to O(1)
"""

    def isempty(self):
        if self._size > 0:
            return False
        return True

    def _insert_at_beginning(self, value):
        """
"""
        if self._simple_interface:
            node = DoublePointerNode(value)
        else:
            node = value
        node._next = self._head
        if self._head is not None:  # fuck you logical bug, muhahahaaaha! I rule
            self._head._prev = node
        if not self._tail:
            self._tail = node
        self._head = node
        self._size += 1
        return node

    # insert at beginning has already been taken care of by inheritance!

    def _insert_at_end(self, value):
        if self._simple_interface:
            node = DoublePointerNode(value)
        else:
            node = value
        if self._tail is not None:
            self._tail._next = node
            node._prev = self._tail
            self._tail = node
            self._size += 1
            return node
            # time complexity is O(1)
        elif self._head is None:
            if self._simple_interface:
                self._insert_at_beginning(value)
            else:
                return self._insert_at_beginning(node)
            # time complexity is O(1)
        else:
            x = self._head
            while x is not None and x.get_next() is not None:
                x = x._next
            node._prev = x
            x._next = node
            self._tail = node
            self._size += 1
            return node
            # time complexity is O(1)

    """Hmmm it seems I am having problem implementing that cool
functionality in all doubly linked list method without having to
increase it time complexity to O(n)

It seems I would have to risk it, since I was able to implement it in
the other method
"""

    def _insert_at_middle(self, displace_this, with_this=None):
        if self._simple_interface:
            x = self._head
            node = DoublePointerNode(with_this)
            # looking for the displaced node instance
            while x is not None and x.get_data() != displace_this:
                if (x.get_prev() is not None) and (x.get_prev().get_data() == displace_this):
                    x = x.get_prev()
                    break
                if x.get_next().get_next() is None:
                    x = x.get_next()
                else:
                    x = x.get_next().get_next()
            # time complexity is O(n/2)
            if not with_this:
                del node
                return x
        else:
            if not with_this:
                return displace_this

            x = displace_this
            node = with_this
            # time complexity is O(1)
        displaced = x
        node._next = displaced
        node._prev = displaced._prev
        displaced._prev._next = node
        displaced._prev = node
        self._size += 1
        return node

    def _del_at_beginning(self):
        x = self._head
        if x._next is not None:
            self._head = x._next
        self._head._prev = None
        x._next = None
        if x == self._tail:  # This means it has gotten to the last node
            self._tail = None
            self._head = None
        self._size -= 1
        return x

    def _del_at_end(self):
        if self._tail is not None:
            x = self._tail
            x._prev._next = None
            self._tail = x._prev
            x._prev = None
            self._size -= 1
            return x
        else:
            x = self._head
            while x is not None and x.get_next() is not None:
                x = x.get_next()
            x._prev._next = None
            x._prev = None
            self._size -= 1
            return x

    def _del_at_middle(self, target):
        x = self._head
        if self._simple_interface:
            while x is not None and x.data != target:
                x = x._next
        else:
            x = target
        x._prev._next = x._next
        x._next._prev = x._prev
        x._prev = None
        x._next = None
        self._size -= 1
        return x

    def delete(self):
        while self._head is not None:
            x = self._head
            self._head = x.get_next()
            del x
        self._tail = None
        self._size = 0


class PositionalADT(DoublyLinkedList):
    """If simple_interface is set to False the argument should be where
asked in nodes instances and it's corresponding node position instance
eg x = PositionalADT(True)
node = Node(5)
first_position = x.add(node)
second_position = x.add_after(new_node, first_position)



Otherwise in it's default state which is True let the argument be it
plain data of the node"""

    #    def __init__(self):
    #        """love, peace"""
    def __iter__(self):
        # peace
        if self._simple_interface:
            current = self.get_head()
            while current is not None:
                yield current.get_data()
                current = current.get_next()
        else:
            current = self.first()
            while current is not None:
                yield current
                current = self.after(current)

    class __Position:
        """This special class enscapulate the node and keep it hidden
from the user to be inteferred with
"""

        def __init__(self, _container, node):
            self._container = _container  # This contain the instantiates of the __PositionalADT
            self._node = node

        def get_node(self):
            return self._node

    def __make_position(self, node):
        """This method creates a cover around the node """
        return self.__Position(self, node)

    def __validate(self, __Position):
        """This method __validates if the cover around the node is either
valid or belong to the list and return the node to be further
processed if it does

The returned value is not to be made available to the user to be tampered with
"""
        if not isinstance(__Position, self.__Position):
            print("This is not a valid __Position")
            return False
        if __Position._container != self:
            print('This node does not belong to this list')
            return False
        if isinstance(__Position, self.__Position) and __Position._container == self:
            return __Position.get_node()

    def first(self):
        """Return the first data in the list or an error message if
the list is empty
"""
        if self._head is not None:
            if self._simple_interface:
                return self._head.get_data()
            return self.__make_position(self._head)
        print("Error! Linked list is empty")

    def last(self):
        """Return the last data in the list or an error message if the list
is empty
"""
        if self._tail:
            if self._simple_interface:
                return self._tail.get_data()
            else:
                return self.__make_position(self._tail)
        elif self._head:
            x = self._head
            while x != None and x._next != None:
                if x._next._next == None:
                    x = x._next
                else:
                    x = x._next._next
            self._tail = x
            if self._simple_interface:
                return self._tail.data
            else:
                return self.__make_position(self._tail)
        print("Error! Linked list is empty")

    def after(self, position):
        if self._simple_interface:
            x = super()._insert_at_middle(position)._next
            if x is not None:
                return x.get_data()
        else:
            x = super()._insert_at_middle(self.__validate(position))._next
            if x is not None:
                return self.__make_position(x)

    def before(self, position):
        if self._simple_interface:
            x = super()._insert_at_middle(position)._prev
            if x is not None:
                return x.get_data()
        else:
            x = super()._insert_at_middle(self.__validate(position))._prev
            if x is not None:
                return self.__make_position()

    def add(self, value):
        if self._simple_interface:
            super()._insert_at_end(value)
        else:
            return self.__make_position(super()._insert_at_end(value))

    def add_first(self, value):
        if self._simple_interface:
            super()._insert_at_beginning(value)
        else:
            super()._insert_at_beginning(value)
            return self.__make_position(self._head)
        if not self._tail:
            self.last()

    def add_after(self, add_this, after_this):
        if self._simple_interface:
            if after_this == self.last():
                self.add(add_this)
            else:
                super()._insert_at_middle(self.after(after_this), add_this)
        else:
            security_check = self.__validate(after_this)
            if security_check:
                valid_position = security_check
                del (security_check)
                if valid_position == self.last().get_node():
                    self.add(add_this)
                    del (valid_position)
                else:
                    del (valid_position)
                    return self.__make_position(super()._insert_at_middle(self.after(after_this).get_node(), add_this))

    def add_before(self, add_this, before_this):
        if self._simple_interface:
            if before_this == self.first():
                self.add_first(add_this)
            else:
                super()._insert_at_middle(before_this, add_this)
        else:
            security_check = self.__validate(before_this)
            if security_check:
                valid_position = security_check
                del (security_check)
                if valid_position == self.first().get_node():
                    self.add_first(add_this)
                    del (valid_position)
                else:
                    return self.__make_position(super()._insert_at_middle(valid_position, add_this))

    def pop(self, target):
        if self._simple_interface:
            if target is None:
                return self._del_at_end().get_data()
            else:
                return self._del_at_middle(target).get_data()
        elif target == None:
            return self.__make_position(self._del_at_end())
        else:
            security_check = self.__validate(target)
            if security_check:
                valid_position = security_check
                del (security_check)
                return self.__make_position(self._del_at_middle(valid_position))

    def pop_first(self):
        if self._simple_interface:
            return self._del_at_beginning().get_data()
        return self.__make_position(self._del_at_beginning())

    def pop_all(self):
        self.delete()

    def get_position_by_node_value(self, value):
        if not self._simple_interface:
            x = self.first()
            while x is not None and x.get_node().get_data() != value:
                x = self.after(x)
            return x
        print("This method can't be runned if you are working with pure data instead of nodes")


"""NICE I AM THROUGH, TIME TO START FINESSING MY PROGRAM

Now to make it more intelligent and less verbose


I AM THROUGH!!!!! THANK YOU GOD, NOW ON TO TREES!!!!
"""


class Stack(DoublyLinkedList):
    def push(self, node):
        self._insert_at_beginning(node)

    def pop(self):
        if not self.isempty():
            return self._del_at_beginning()
        return "Stack is empty"

    def top(self):
        return self.first()


class Queue(DoublyLinkedList):
    def enqueue(self, node):
        self._insert_at_end(node)

    def dequeue(self):
        x = self.isempty()
        if not self.isempty():
            return self._del_at_beginning()
        return "Queue is empty"

    def first(self):
        if not self.isempty():
            return self.get_head()
        return "Queue is empty"

# L = PositionalADT()
# for i in range(5):
#    L.add(i)

# for a in L:
#    print(a)

# M = PositionalADT()
# for i in range(5, 11):
#    M.add(i)

# for a in M:
#    print(a)


# queue = Queue(False)
# nodes = [DoublePointerNode(i) for i in range(5)]
# queue.enqueue(nodes[4])
# queue.enqueue(nodes[3])
# queue.enqueue(nodes[2])
# queue.enqueue(nodes[1])
# queue.enqueue(nodes[0])



# nodes = [DoublePointerNode(i) for i in range(5)]
# stack = Stack(False)
# stack.push(nodes[4])
# stack.push(nodes[3])
# stack.push(nodes[2])
# stack.push(nodes[1])
# stack.push(nodes[0])






# print(stack.pop().get_data())
