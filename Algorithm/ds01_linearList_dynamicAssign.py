"""
Dynamic assignment of linear list
"""


class SqList:
    def __init__(self):
        self.data = []  # Dynamic list, initially empty
        self.length = 0  # The length of the list, which has stored elements

    def init_list(self, max_size=10):
        self.data = [0] * max_size  # Initialize with a specified size
        self.length = 0

    def change_list_element(self, i, value):
        if i < 0 or i >= len(self.data):
            print("Location Error")
            return
        self.data[i] = value
        self.length += 1

    def is_empty(self):
        return self.length == 0

    def __str__(self):
        return f"SqList: {self.data}, Length: {self.length}"


# Test the dynamic SqList data structure
# Initialize the list with a dynamic size
sq_list_dynamic = SqList()
sq_list_dynamic.init_list(12)  # Initializing with size 12, can be any size

print(sq_list_dynamic)

# Look what is inside the list
for i in range(len(sq_list_dynamic.data)):
    print(f'the {i}th element is {sq_list_dynamic.data[i]}')

# Insert 10 elements into the list dynamically
for i in range(len(sq_list_dynamic.data)):
    sq_list_dynamic.change_list_element(i, i + 1)
    print(f'the {i}th inserted element is {sq_list_dynamic.data[i]}')

# Display the final state of the list
sq_list_dynamic.__str__()
