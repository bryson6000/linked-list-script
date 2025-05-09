class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def insertAtFirst(listHead, val):
    new = Node(val)
    new.next = listHead
    return new

def insertAtEnd(listHead, val):
    if listHead is None:
        new = Node(val)
        return new
    if listHead.next is None:
        new = Node(val)
        listHead.next = new
        return listHead
    insertAtEnd(listHead.next, val)
    return listHead

def insertInBetween(temp, val, pos):
    if temp is None and pos > 0:
        return temp
    if pos == 0:
        new = Node(val)
        new.next = temp
        return new
    if pos == 1:
        new = Node(val)
        new.next = temp.next
        temp.next = new
        return temp
    insertInBetween(temp.next, val, pos - 1)
    return temp

def printll(head):
    if head == None:
        return
    print(head.val, end='  ->  ')
    printll(head.next)

if __name__ == '__main__':
    pass
