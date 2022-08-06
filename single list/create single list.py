class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
class SinggleLinkList(object):
    def __init__(self, head=None):
        self.head = head

    def headadd(self, val):  # 头插
        node = Node(val)
        node.next = self.head
        self.head = node

    def tailadd(self, val):  # 尾插
        node = Node(val)
        cur = self.head
        if cur is None:
            self.headadd(val)
        while cur.next is not None:
            cur = cur.next
        cur.next = node

    def middleadd(self, val, pos):
        node = Node(val)
        if pos <= 0:
            node.next = self.head
            self.head = node
        else:
            cur = self.head
            for i in range(pos - 1):
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def travel(self):
        cur = self.head
        while cur is not None:
            print(cur.val, ">")
            cur = cur.next

    def removeNthFromEnd(self, n):
        #虚拟头节点的方式
        dummy = Node(0)
        dummy.next=self.head
        first = second = dummy

        for i in range(n + 1):  # 想让快指针先跑，这样能保证两个指针间的距离是n
            first = first.next
            print("i",i)
        while first:  # 让快指针跑到结尾，慢指针跑到要跳过的元素前一个元素
            first = first.next
            second = second.next
        print(second.val)
        second.next = second.next.next  # 跳过一个元素

        return dummy.next



        # cur = self.__headhead
        # count = 0
        # if cur is not None:
        #     cur = cur.next
        #     count += 1
        # n_inorder = count - n + 1
        #
        # pre = None
        # cur = self.__head
        # count1 = 1
        # while cur is not None:
        #     if count1 == n_inorder:
        #         if pre is None:
        #             self.__head = cur.next
        #         else:
        #             pre.next = cur.next
        #             break
        #     else:
        #         count1 += 1
        #         pre = cur
        #         cur = cur.next
        # return self.__head

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index < 0:
            index = 0
        elif index > self._count:
            return

        # 计数累加
        self._count += 1

        add_node = Node(val)
        prev_node, current_node = None, self._head
        for _ in range(index + 1):
            prev_node, current_node = current_node, current_node.next

        prev_node.next, add_node.next = add_node, current_node


alink = SinggleLinkList()
alink.headadd(1)
alink.tailadd(2)
alink.tailadd(3)
alink.tailadd(4)
alink.tailadd(5)
alink.tailadd(6)
#
alink.addAtIndex(5,10)
alink.travel()
alink.removeNthFromEnd(5)
alink.travel()
