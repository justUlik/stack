class MyStack:
    def __init__(self):
        self.data = []

    def is_empty(self) -> bool:
        return self.data == []

    def size(self) -> int:
        return len(self.data)

    def top(self) -> int:
        return self.data[len(self.data) - 1]

    def pop(self) -> int:
        self.data.pop(-1)

    def push(self, element: int) -> None:
        self.data.append(element)

    def __repr__(self) -> str:
        s = ""
        if self.is_empty():
            s = "MyStack('empty')"
        else:
            s = "MyStack(" + str(self.data)[1:-1] + ")"
        return s
