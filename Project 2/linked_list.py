"""
LAB2
CPE 202
John Wright
"""

class Node:
    """Linked List is one of None or Node
    Attributes:
        val (int): an item in the list
        next (Node): a link to the next item in the list (Linked List)
    """
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt

    def __repr__(self):
        return "Node({},{})".format(self.val, self.next)

    def __eq__(self, other):
        if other is None:
            return False
        if isinstance(other, Node) is False:
            return False
        if other.val == self.val and other.next == self.next:
            return True
        return False

def insert(lst, val, pos):
    """inserts the integer at the position pos in the linked list recursively.
    Args:
        lst (Node): the list
        val (int): the value to be inserted in the list
        pos (int): the position
    Returns:
        Node: the head of a LinkedList
    Raises:
        IndexError: when the position is out of bound ( > num_items).
    """
    if lst is None:
        return Node(val)
    if pos > size(lst):
        raise IndexError('Index Out of Range')
    if pos == 0:
        temp = Node(val)
        temp.next = lst
        return temp
    if pos == size(lst):
        temp = lst
        while temp.next is not None:
            temp = temp.next
        temp.next = Node(val)
        return lst
    if 0 < pos < size(lst):
        temp = lst
        idx = 0
        while idx != pos-1:
            temp = temp.next
            idx += 1
        temp.next = Node(val, temp.next)
        return lst


def get(lst, pos):
    """gets an item stored at the specified position recursively.
    Args:
        lst (Node): a head of linked list
        pos (int): the specified position
    Returns:
        int: the value of the item at the position pos.
    Raises:
        IndexError: when the position is out of bound ( >= num_items).
    """
    if lst is None:
        return None
    if pos >= size(lst) or pos < 0:
        raise IndexError
    if pos == 0:
        return lst.val
    return get(lst.next, pos-1)

def search(lst, val, idx=0):
    """searches for a specified value in a given list.
    Args:
        lst (Node): an object of Node (LinkedList)
        val (int): a value to search for
    Returns:
        int: the position where the value is stored in the list.
    It returns None if the value is not found.
    """
    if lst is None:
        return None
    if lst.val == val:
        return idx
    return search(lst.next, val, idx + 1)

def contains(lst, val):
    """checks if a specified value exists in a given list.
    This function calls search function.
    Args:
        lst (Node): the head of a LinkedList
    Returns:
        bool: True if the value is found or False if not.
    """
    if lst is None:
        return False
    if lst.val == val:
        return True
    return contains(lst.next, val)

def remove(lst, val):
    """removes the first occurrence of a specified value in a given list recursively.
    Args:
        lst (Node): the head of a LinkedList
        val (int): a value to be removed
    Returns:
        Node: the head of the linked list with the first occurrence of the value removed.
    """
    if lst is None:
        return None
    if lst.val == val:
        return lst.next
    return Node(lst.val, remove(lst.next, val))

def pop(lst, pos):
    """removes the item at a specified position in a given list recursively
    Args:
        lst (Node): the head of a LinkedList
        pos (int): the position in the list where an item is removed
    Returns:
        Node: the head of the LinkedList with the item removed
        int: the removed item’s value.
    Raises:
        IndexError: when the position is out of bound ( >= num_items).
    """
    if lst is None:
        return None
    if pos >= size(lst) or pos < 0:
        raise IndexError('Index out of Range')
    if pos == 0:
        return (lst.next, lst.val)
    if 0 < pos < size(lst):
        temp = lst
        idx = 0
        while idx != pos - 1:
            temp = temp.next
            idx += 1
        temp2 = temp.next
        temp.next = temp2.next
        return (lst, temp2.val)

def size(lst):
    """returns the number of items stored in the LinkedList recursively.
    Args:
        lst (Node): the head of a LinkedList
    Returns:
        int: the number of items stored in the list
    """
    if lst is None:
        return 0
    return 1 + size(lst.next)
