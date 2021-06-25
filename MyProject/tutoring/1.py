class calculator:
    def __init__(self):
        self.value = 0

    def add(self, a, b):
        c = a + b
        self.value = c

    def sub(self, a, b):
        c = a - b
        self.value = c

    def reset(self):
        self.value = 0

c = calculator()
print(c.value)

c.sub(100, 555)
print(c.value)

c.reset()
print(c.value)
