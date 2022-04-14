class SingleNode(object):
    def __init__(self, item):
        self.item = item
        self.next = None


class SingleLinkList():
    def __init__(self):
        self.head = None

    def is_empty(self):  # 是否为空
        return self.head == None

    def length(self):  # 长度
        cur = self.head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self.head
        while cur != None:
            print(cur.item)
            cur = cur.next

    def add(self, item):
        """头部添加元素 """
        node = SingleNode(item)
        node.next = self.head
        self.head = node

    def append(self, item):
        """尾部添加元素"""
        node = SingleNode(item)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = node

    def insert(self, pos, item):
        """指定位置添加元素"""
        node = SingleNode(item)
        length = self.length()
        if pos <= 0:
            self.add(item)
        elif pos >= self.length() - 1:
            self.append(item)

        else:
            cur = self.head
            count = 0
            while (count != pos - 1):
                cur = cur.next
                count += 1
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        """按照取值删除，其他操作与取值类似"""
        cur = self.head
        pre = None
        length = 1
        if self.length() == 0:
            print("空表无法删除")
            return None
        while cur != None:
            if cur.item == item:
                break
            else:
                length += 1
                pre = cur
                pre = cur.next
        if length == 1:
            self.head = cur.next
        elif length == self.length():
            print("未找到元素")
            return None
        else:
            pre.next = cur.next

    def search(self, item):
        """判断节点是否存在"""
        cur = self.head
        while cur == None:
            if cur.item == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == "__main__":
    first = SingleLinkList()
    first.add(1)
    first.add(2)
    first.append(3)
    first.insert(2, 4)
    print("length:", first.length())
    first.travel()
    print(first.search(3))
    print(first.search(5))
    first.remove(1)
    print("length:", first.length())
    first.travel()
