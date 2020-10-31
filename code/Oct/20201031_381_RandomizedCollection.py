import random


class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val_dict = dict()  # 用来存储val, 和对应的所有下标, 下标用set
        self.val_list = list()  # 用来存储所有的val(允许重复)
        self.cur_len = -1

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.val_list.append(val)
        self.cur_len += 1
        if val in self.val_dict:
            self.val_dict[val].add(self.cur_len)
            return False
        else:
            self.val_dict[val] = {self.cur_len}
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        # 这部分是关键:
        if (val not in self.val_dict) or len(self.val_dict[val]) == 0:
            return False
        # 1. 随机从此对象位置集合里面剔除一个
        pos = self.val_dict[val].pop()
        # 2. 将队列最后一个元素放到剔除的位置;
        if pos != self.cur_len:
            last_val = self.val_list[self.cur_len]
            self.val_dict[last_val].remove(self.cur_len)
            self.val_dict[last_val].add(pos)
            self.val_list[pos] = last_val
        self.val_list.pop(-1)
        self.cur_len -= 1
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.val_list)


# Your RandomizedCollection object will be instantiated and called as such:
obj = RandomizedCollection()
print(obj.insert(1))
print(obj.insert(1))
print(obj.insert(2))
print(obj.getRandom())
print(obj.remove(1))
