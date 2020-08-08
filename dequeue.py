class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None



class Deque:
   
    def __init__(self):
        self.size = 0
        self.head = ListNode("head")
        self.tail = ListNode("tail")
        self.head.next = self.tail
        self.tail.prev = self.head


   
    def isEmpty(self):
        return self.getSize() == 0

    
    def getSize(self):
        return self.size

   
    def addFirst(self, item):
        

        new_node = ListNode(item)
        prev_first = self.head.next
        
        self.head.next.prev = new_node
        
        self.head.next = new_node
        
        new_node.prev = self.head
        new_node.next = prev_first
        self.size += 1

    
    def addLast(self, item):
        

        new_node = ListNode(item)
        prev_last = self.tail.prev
        
        self.tail.prev.next = new_node
        
        self.tail.prev = new_node
        
        new_node.next = self.tail
        new_node.prev = prev_last
        self.size += 1

    
    def removeFirst(self):
        
        if self.isEmpty():
            print("trying to remove from empty list")
            return

        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next
        self.size -= 1



   
    def removeLast(self):
       
        if self.isEmpty():
            print("trying to remove from empty list")
            return


        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev
        self.size -= 1

    
    def asList(self):
        lst = []
        cur = self.head.next
        while(cur.next):
            lst.append(cur.val)
            cur = cur.next
        return lst




if __name__ == '__main__':
   
    dq = Deque()
    for i in range(1,6):
        dq.addFirst(i)
    for i in range(6,11):
        dq.addLast(i)

    
    print(dq.asList())
    dq.removeFirst()
    print(dq.asList())
    
    dq.removeLast()
    print(dq.asList())
   
