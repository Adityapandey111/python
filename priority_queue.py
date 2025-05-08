from queue import PriorityQueue

class A:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def __str__(self):
        return f"Name:{self.name}"

# Initialize a priority queue
pq = PriorityQueue()

# obj=A("Aditya",1)
# print(f"{obj.name}")

# Put items: put((priority, value))
pq.put((11,A("Rahul",2)))
pq.put((21,A("Shrestha",5)))
pq.put((1,A("Aditya",1)))
# Get items: get()
while not pq.empty():
    priority,value = pq.get()
    print(f"Priority: {priority} {value}")