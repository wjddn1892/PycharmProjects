class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def peek(self):
        return self.items[len(self.items) - 1]
    def size(self):
        return len(self.items)
    def pop(self):
        return self.items.pop()

def divideBy2(decNumber):
    lst = Stack()

    while decNumber != 0:
        lst.push(decNumber % 2)
        decNumber = decNumber // 2

    binString = ""
    while not lst.isEmpty():
        binString = binString + str(lst.pop())

    return binString

def infixToPrefix(infixexpr):
    prec = {'/':3,'*':3,'+':2,'-':2,'^':4,'(':1}
    opStack = Stack()

    prefixList = []
    temp = []
    for token in infixexpr:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            prefixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                temp.append(topToken)
                topToken = opStack.pop()
            prefixList = temp + prefixList
            temp = []
        else:
            while (not opStack.isEmpty()) and \
                  (prec[opStack.peek()]>= prec[token]):
                temp.append(opStack.pop())
            prefixList = temp + prefixList
            temp = []
            opStack.push(token)
    while not opStack.isEmpty():
        temp.append(opStack.pop())
    prefixList = temp + prefixList
    return ''.join(prefixList)

def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

print(infixToPrefix("(A+B)*C-(D-E)*(F+G)"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
print(infixToPostfix("A * B + C * D"))
