"""
static assign linear list
"""


class SqList:
    def __init__(self, max_size=10):
        self.data = [0] * max_size  # Using list to simulate array
        self.length = 0  # The length of the list,which has stored elements

    def init_list(self):
        for i in range(len(self.data)):
            self.data[i] = 0  # Initialize all elements to 0
        self.length = 0  # Set length to 0

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


'''
test the SqList data structure
'''
# initialize the list
sq_list = SqList()
sq_list.init_list()

# Display the state of the list after initialization
sq_list.__str__()
print(sq_list)

# look what is inside the list
for i in range(len(sq_list.data)):
    print(f'the {i}th element is {sq_list.data[i]}')

# Insert 10 elements into the list
for i in range(len(sq_list.data)):
    sq_list.change_list_element(i, i + 1)
    print(f'the {i}th inserted element is {sq_list.data[i]}')