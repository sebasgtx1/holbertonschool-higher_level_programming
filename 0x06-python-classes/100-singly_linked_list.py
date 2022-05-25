#!/usr/bin/python3
"""7. Singly linked list:
    Write a class Node that defines a node of a singly linked list
    And, write a class SinglyLinkedList that defines a singly linked list
"""


class Node:
    """Class to define a node """
    def __init__(self, data, next_node=None):
        """Constructor Method to define data and next_node
            Args:
                param1 (int): data
                param2 (Node): next_node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Data getter: Property to retrieve data
            Return:
                the data value
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Data setter: Sets the data value if recives and integer
            Args:
                value (int): value to be stored in the SLL"""
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """next_node getter_ Property to retrieve the next_node
            Return:
                the next_node value
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """next_node setter: Setrs the next_node value (it has to be an
            integer or a Node object)
            Args:
                value (Node or None): the value for the next_node
        """
        if isinstance(value, Node) or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """ Class to define a SLL """
    def __str__(self):
        """Method to use print or str for the SLL
            Return:
                the SLL"""
        SLL = ""
        temp = self.__head
        while temp:
            SLL += str(temp.data)
            temp = temp.next_node
            if temp:
                SLL += "\n"
        return SLL

    def __init__(self):
        """Method that define and sets the Head node of a SLL
            to None(NULL)"""
        self.__head = None

    def sorted_insert(self, value):
        """Method that inserts a new node at the begginning of a SLL
            Args:
                value (int): value to be inserted"""
        temp = self.__head
        while(temp):
            if temp.data > value:
                break
            save = temp
            temp = temp.next_node

        newNode = Node(value, temp)
        if temp == self.__head:
            self.__head = newNode
        else:
            save.next_node = newNode

    def printLL(self):
        """Method to print a SLL"""
        current = self.head
        while(current):
            print(current.data)
            current = current.next_node
