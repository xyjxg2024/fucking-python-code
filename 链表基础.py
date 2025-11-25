class ListNode:
    def __init__(self, data):
        self.val = data#链表的数据域
        self.next = None#链表的指针域
def insert_node(node,value):
    if __name__ =='__main__':
        head=ListNode(1)
        head.next=ListNode(2)
        head.next.next=ListNode(3)
        head.next.next.next=ListNode(4)
        head.next.next.next.next=ListNode(5)

        tmp= head
        tmp= tmp.next
        tmp.next=None