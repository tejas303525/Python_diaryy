class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class linkedlist:  
    def __init__(self):
        self.head=None
        
    def linkedlist(self,val):
        new_node=Node(val)   
        if self.head == None:
            self.head=new_node
        else:
            current=self.head
            while current.next!=None:
                current=current.next
            current.next=new_node
    def display(self):
        result=[]
        curr=self.head
        while curr!=None:
            result.append(curr.val)
            curr=curr.next
        return result
    def rev_linked_list(self):
        prev=None
        curr=self.head
        while curr!=None:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        self.head=prev


linked_list=linkedlist()
linked_list.linkedlist(1)
linked_list.linkedlist(2)
linked_list.linkedlist(3)
linked_list.linkedlist(4)
print(linked_list.display())
linked_list.rev_linked_list()
print(linked_list.display())
