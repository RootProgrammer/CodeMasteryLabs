class RandomizedCollection:
    def __init__(self):
        self.elements = []
        self.index_map = defaultdict(set)

    def insert(self, value: int) -> bool:
        self.elements.append(value)
        self.index_map[value].add(len(self.elements) - 1)
        return len(self.index_map[value]) == 1

    def remove(self, value: int) -> bool:
        if not self.index_map[value]:
            return False

        remove_index = self.index_map[value].pop()
        last_element = self.elements[-1]

        if remove_index != len(self.elements) - 1:
            self.elements[remove_index] = last_element
            self.index_map[last_element].add(remove_index)
            self.index_map[last_element].remove(len(self.elements) - 1)

        self.elements.pop()
        if not self.index_map[value]:
            del self.index_map[value]

        return True

    def getRandom(self) -> int:
        return random.choice(self.elements)

        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()