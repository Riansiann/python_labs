class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def ll_from_list(values) -> Node | None:
    """
    Create a linked list from a sequence and return its head
    """
    head = None 
    for value in reversed(values):
        head = Node(value, head)
    return head 

def ll_to_list(head: Node | None) -> list:
    """
    Convert a linked list into a Python list
    """
    result = []
    cur = head
    while cur is not None:
        result.append(cur.value)
        cur = cur.next

    return result

def ll_length(head: Node | None) -> int:
    """
    Return the number of nodes in a linked list
    """
    cnt = 0
    cur = head
    while cur is not None:
        cnt += 1
        cur = cur.next
    return cnt

def ll_prepend(head, value) -> Node:
    """
    Add a new node to the beginning and return the new head
    """
    return Node(value, head)

def ll_append(head, value) -> Node:
    """
    Add a new node to the end and return the head
    """
    new_node = Node(value)

    if head is None:
        return new_node

    cur = head
    while cur.next is not None:
        cur = cur.next

    cur.next = new_node

    return head 

def ll_insert(head, idx: int, value) -> Node:
    """
    Insert a node at the specified index and return the head
    Raise IndexError if the index is out of range
    """
    if idx < 0 or idx > ll_length(head):
        raise IndexError(f"Index {idx} is out of range for a list of length {ll_length(head)}")

    if idx == 0:
        return ll_prepend(head, value)

    new_node = Node(value)
    cur = head 

    for _ in range(idx - 1):
        cur = cur.next

    new_node.next = cur.next
    cur.next = new_node

    return head

def ll_remove_at(head, idx: int) -> Node | None:
    """
    Remove a node at the specified index and return the updated head
    Raise IndexError if the index is out of range
    """
    if idx < 0 or idx >= ll_length(head):
        raise IndexError(f"Index {idx} is out of range for a list of length {ll_length(head)}")

    if idx == 0:
        head = head.next

    else:
        cur = head

        for _ in range(idx - 1):
            cur = cur.next

        cur.next = cur.next.next

    return head

def ll_reverse(head) -> Node | None:
    """
    Reverse a linked list in place and return the new head
    """
    prev = None
    cur = head

    while cur is not None:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt

    return prev

def ll_repr(head) -> str:
    """
    Return a string representation of the linked list.
    """
    parts = []
    cur = head
    while cur is not None:
        parts.append(f"{cur.value}")
        cur = cur.next

    if not parts:
        return "None"

    return " -> ".join(parts) + " -> None"

if __name__ == "__main__":
    head = ll_from_list([4, 5, 6])
    print("from list:", ll_to_list(head))

    print("to list:", ll_to_list(head))

    print("length:", ll_length(head))

    head = ll_prepend(head, 0)
    print("\nprepend 0:", ll_to_list(head))

    head = ll_append(head, 4)
    print("append 4:", ll_to_list(head))

    head = ll_insert(head, 2, 99)
    print("insert(2, 99):", ll_to_list(head))

    head = ll_remove_at(head, 2)
    print("remove_at(2):", ll_to_list(head))

    head = ll_reverse(head)
    print("reverse:", ll_to_list(head))

    print("repr:", ll_repr(head))

    # errors
    try:
        ll_insert(head, 100, 8)
    except IndexError as e:
        print("\ninsert invalid index:", e)

    try:
        ll_remove_at(head, 100)
    except IndexError as e:
        print("remove invalid index:", e)

        
    
