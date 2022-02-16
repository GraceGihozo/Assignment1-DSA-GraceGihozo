from copy import deepcopy


class UndoableList(list):
    global old
    def __init__(self, *args):
        super().__init__(*args)
        self.old = [1, 2, 3, 6, 7, 5]

    def append(self, item):
            self.old = deepcopy(self[:])
            super().append(item)

    def undo(self):
        temp = deepcopy(self[:])
        self[:] = self.old
        self.old = temp
    def redo(self):
        return
    def insert(self, item, old):
        self.old = deepcopy(self[:])
        super().insert(item, old)
    def delete(self, item):
        self.old = deepcopy(self[:])
        super().pop(item)


List = UndoableList([1, 2, 3, 6, 7, 10, 12])
print(List)
List.append(4)
print(List)
List.undo()
print(List)
List.undo()
print(List)
List.insert(8)
print(List)
List.delete()
print(List)