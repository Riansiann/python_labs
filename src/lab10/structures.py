from collections import deque
from typing import Any

# stack
def stack_push(st, item) -> None:
    """
    Add an item to the top of the stack
    """
    st.append(item)

def stack_pop(st) -> Any:
    """
    Remove and return the top item of the stack
    Raise IndexError if the stack is empty
    """
    if not st:
        raise IndexError("The element cannot be removed: stack is empty")
    return st.pop()

def stack_peek(st) -> Any | None:
    """
    Return the top item without removing it, or None if empty
    """
    if not st:
        return None
    return st[-1]

def stack_is_empty(st) -> bool:
    """
    Return True if the stack is empty, otherwise False
    """
    return len(st) == 0

# queue

def queue_enqueue(q, item) -> None:
    """
    Add an item to the end of the queue
    """
    q.append(item)

def queue_dequeue(q) -> Any:
    """
    Remove and return the first item of the queue
    Raise IndexError if the queue is empty
    """
    if not q:
        raise IndexError("The element cannot be removed: queue is empty")
    return q.popleft()

def queue_peek(q) -> Any | None:
    """
    Return the first item without removing it, or None if empty
    """
    if not q:
        return None
    return q[0]

def queue_is_empty(q) -> bool:
    """
    Return True if the queue is empty, otherwise False
    """
    return len(q) == 0

# task

def is_balanced(s: str) -> bool:
    """
    Check whether brackets in a string are correctly balanced.
    Return True if balanced, otherwise False.
    """
    pairs = {
        ")" : "(",
        "]" : "[",
        "}" : "{"
    }
    st = []
    for ch in s:
        if ch in "([{":
            stack_push(st, ch)
        elif ch in pairs:
            if stack_is_empty(st) or stack_pop(st) != pairs[ch]:
                return False

    return stack_is_empty(st)

if __name__ == "__main__":
    print("stack")
    st = []
    stack_push(st, 5)
    stack_push(st, 6)
    stack_push(st, 7)
    print("stack after push 5, 6, 7:", st)

    print("\nstack peek:", stack_peek(st))
    print("stack empty stack peek:", stack_peek([]))
    print("stack pop:", stack_pop(st), "->", st)
    print("stack is empty:", stack_is_empty(st))

    try:
        stack_pop([])
    except IndexError as e:
        print("empty stack pop: IndexError", e)

    print("\nqueue")
    q = deque()
    queue_enqueue(q, "q")
    queue_enqueue(q, "w")
    queue_enqueue(q, "e")
    print("queue after enqueue q, w, e:", q)

    print("\nqueue peek:", queue_peek(q))
    print("empty queue peek:", queue_peek(deque()))
    print("queue dequeue:", queue_dequeue(q), "->", q)
    print("queue is empty:", queue_is_empty(q))

    try:
        queue_dequeue(deque())
    except IndexError as e:
        print("empty queue dequeue: IndexError", e)


    print("\nbracket sequence")
    for text in ["{[](){}}", "{[}]()", "{{{", ")("]:
        print(f"{text} -> {is_balanced(text)}")


