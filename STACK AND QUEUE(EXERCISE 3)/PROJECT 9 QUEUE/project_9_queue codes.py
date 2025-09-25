from collections import deque
# create an empty deque of Nyabugogo
Nyabugogo_queue = deque()
print("-- enqueuing in Nyabugogo queue --")
def Nyabugogo_enqueue(item):
    """ add an item to the end of the queue"""
    Nyabugogo_queue.append(item)
    return f" enqueued buses in Nyabugogo queue {item} \n"

# if 2 buses depart
def Nyabugogo_peek():
    """ peek at the two front item of the queue without removing it"""
    if Nyabugogo_queue: # check if there is any item
        remain = Nyabugogo_queue.popleft()
        return f" The bus depart are: {remain} \n"
    return "Queue is empty, nothing to peek"

# add an items
Nyabugogo_enqueue("bus1")
Nyabugogo_enqueue("bus2")
Nyabugogo_enqueue("bus3")
Nyabugogo_enqueue("bus4")

print(Nyabugogo_queue)
print(Nyabugogo_peek())
print(f" after two bus depart it remain: {Nyabugogo_queue} \n")

# BK ATM Queue
print("--- enqueuing in BK ATM queue ---")
BK_ATM_queue = deque()
def BK_ATM_enqueue(item):
    """ add an item to the end of the queue"""
    BK_ATM_queue.append(item)
    return f" enqueued in BK ATM queue {item} \n"

# customer who served at second position
def BK_ATM_serve_second():
    """ serve the second customer in the queue"""
    if len(BK_ATM_queue) < 1:
        return "Not enough customers in the queue to serve the second one"
    served = BK_ATM_queue[2]  # get the second customer(index 1)
    return f"The customer served at second position is: {served} \n"
# add a customers
BK_ATM_enqueue("customer1")
BK_ATM_enqueue("customer2")
BK_ATM_enqueue("customer3")
BK_ATM_enqueue("customer4")
BK_ATM_enqueue("customer5")
BK_ATM_enqueue("customer6")

print(BK_ATM_queue)
print(BK_ATM_serve_second())