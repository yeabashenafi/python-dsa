class ListStack:

    # constructor for the List stack class
    def __init__(self):
        self.stack = []
    
    # define a method that checks whether the stack is empty
    def is_empty(self):

        return len(self.stack) == 0
    
    # finds and returns the top value of the stack
    def top(self):

        if self.is_empty() == True:
            raise ValueError("Stack is empty")
        
        return self.stack[-1]

    # removes the top element from the stack
    def pop(self):
        
        top_value = self.top()
        self.stack.remove(top_value)

    # pushes an element to the stack
    def push(self,value):

        self.stack.append(value)

# creates a list stack object
list1 = ListStack()

# pushes elements to the stack
list1.push(10)
list1.push(20)
list1.push(30)

# pops an element from the stack
list1.pop()

# prints the stack of the object
print(list1.stack)