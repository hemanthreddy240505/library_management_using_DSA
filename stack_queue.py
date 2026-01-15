from collections import deque

demand_stack = []   # Track demanded books
waiting_queue = deque()  # Users waiting for books

def sort_demand_stack():
    global demand_stack
    demand_stack = sorted(demand_stack, key=lambda x: demand_stack.count(x), reverse=True)
    print("Sorted demand stack:", demand_stack)
