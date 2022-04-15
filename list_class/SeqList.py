class LinearList:
    def __init__(self, data, last):
        self.data = data
        self.last = last

    def Getdata(self, i):
        return self.data[i - 1]

    def checklist(self):
        if self.data:
            print(self.data)
        else:
            print("为空")

    def Locate(self, aim):
        place = 0
        length = len(self.data)
        for i in self.data:
            if i == aim:
                print("找到")
                return place
            place = place + 1

    def Inslist(self, i, e):  # i为位置，e为要插入的元素
        if 0 > i > self.last + 2:
            print("插入位置错误")
            return 0
        temp = self.last
        self.data.append(i)
        while temp >= i-1:
            self.data[temp + 1] = self.data[temp]
            temp = temp - 1
        self.data[i-1] = e
        self.last = self.last + 1
if __name__ == '__main__':
    data=[1,2,3]
    last=2
    seqlist=LinearList(data,last)

    seqlist.Inslist(2,5)
    seqlist.checklist()