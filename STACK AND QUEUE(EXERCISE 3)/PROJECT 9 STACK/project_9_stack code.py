# declaration of the valiable hold the stack
irembo_stack = []
print("----- pushing in irembo stack -----")
def irembo_push(item):
    """ push an item in irembo stack """
  
    irembo_stack.append(item)
    return f" pushed items in irembo stack {item} \n"

print("---- pop a last item from irembo stack ----")
def irembo_pop():
    """ pop an item from irembbo stack"""
    if irembo_stack:
        removed = irembo_stack.pop(-1)  # pop the last item
        print (f" popped item from irembo stack: {removed}") 
        return "popped successfully"
    return "Stack is empty, nothing to pop"
      
    
# push items in irembo stack
irembo_push("Upload ID")
irembo_push("Fill form")
irembo_push("Comfirm")

print(irembo_stack)
print(irembo_pop())
print(f" after popped item it remain: {irembo_stack} \n")

# declare the valiable hold UR stack
print("----- pushing in UR stack push ----")
ur_stack = []
def ur_push(item):
    """ push an item in UR stack"""
    ur_stack.append(item)
    return f" pushed items in UR stack {item} \n"

# pop a last item from UR stack
def ur_pop():
    """ pop an item from UR stack"""
    print("----- pop all items from UR stack -----")
    """ pop all an items from UR stack"""

    if not ur_stack:
        return "Stack is empty, nothing to pop"
    while ur_stack:
        removed = ur_stack.pop()
    print(f"popped all items from UR stack start at: {removed}")
    return "All items are popped successfully"


# Push challange
def pop_multiple_items(n=len(ur_stack)):
    """ pop multiple items from UR stack"""
    
    if len(ur_stack) < 2:
        return "Not enough items in the stack to pop"
    popped_items = []
    for _ in range(2):
        popped_items.append(ur_stack.pop())
    return f"Popped items: {popped_items}"
# push items in UR stack
ur_push("Answer1")
ur_push("Answer2")
ur_push("Answer3")
print(ur_stack)
print(ur_pop())
print(f" after popped all items it remain: {ur_stack} \n")

