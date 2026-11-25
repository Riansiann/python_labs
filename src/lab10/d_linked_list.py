class DoublyNode:
    def __init__(self, value, prev = None, next = None):
        self.value = value
        self.prev = prev
        self.next = next

def dll_from_list(values) -> DoublyNode | None:
    """
    Create a doubly linked list from a sequence and return its head
    """
    head = None
    for value in reversed(values):
        new_node = DoublyNode(value, next = head)

        if head is not None:
            head.prev = new_node

        head = new_node

    return head


def dll_append(head, value) -> DoublyNode:
    """
    Add a new node to the end of a doubly linked list and return the head
    """
    new_node = DoublyNode(value)


    if head is None:
        return new_node

    cur = head
    while cur.next is not None:
        cur = cur.next

    cur.next = new_node
    new_node.prev = cur 

    return head

def dll_repr(head) -> str:
    """
    Return a string representation of the doubly linked list
    """
    parts = []
    cur = head
    while cur is not None:
        parts.append(f"[{cur.value}]")
        cur = cur.next

    if not parts:
        return "None"

    return "None <- " + " <-> ".join(parts) + " -> None"



if __name__ == "__main__":
    # dll_from_list
    head = dll_from_list(["A", "B", "C"])
    print("from list ['A', 'B', 'C']:", dll_repr(head))

    # dll_append
    head = dll_append(head, "D")
    print("append D:", dll_repr(head))

    # dll_repr
    print("repr:", dll_repr(head))




