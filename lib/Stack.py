class Stack:
    def __init__(self, items=None, limit=100):
        self.items = items if items is not None else []  # Initialize stack with given items or an empty list
        self.limit = limit  # Set stack size limit

    def isEmpty(self):
        return len(self.items) == 0  # Check if the stack is empty

    def push(self, item):
        if len(self.items) < self.limit:  # Check if stack is not full
            self.items.append(item)  # Add item to stack

    def pop(self):
        if not self.isEmpty():  # Check if stack is not empty
            return self.items.pop()  # Remove and return the top item

    def peek(self):
        if not self.isEmpty():  # Check if stack is not empty
            return self.items[-1]  # Return the top item without removing it

    def size(self):
        return len(self.items)  # Return the number of items in the stack

    def full(self):
        return len(self.items) == self.limit  # Check if stack is full

    def search(self, target):
        if target in self.items:  # Check if target is in stack
            return len(self.items) - self.items.index(target) - 1  # Return position from the top
        return -1  # Return -1 if target not found
