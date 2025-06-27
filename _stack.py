# Написать стек с методами push, pop, top, get_min (мин элемент) за время O(n)

# class Element:
#     def __init__(self) -> None:


class Stack:
    def __init__(self) -> None:
        self.elements = []
        self.mins = []

    def push(self, e: int) -> None:
        self.elements.append(e)
        self.mins.append(min([self.mins[-1], e] if self.mins else [e]))

    def pop(self):
        if not self.elements:
            return None
        self.mins.pop()
        return self.elements.pop()

    def top(self):
        return self.elements[-1] if self.elements else None

    def get_min(self):
        return self.mins[-1] if self.mins else None


s = Stack()
s.push(1)
s.push(-2)
print(s.get_min())

s.pop()
print(s.get_min())
s.pop()
print(s.get_min())
