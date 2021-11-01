class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):  # проверка стека на пустоту
        if self.stack == []:
            return True
        else:
            return False

    def push(self, item):  # добавляет новый элемент на вершину стека
        self.stack.append(item)

    def pop(self):  # удаляет верхний элемент стека
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]  # возвращает верхний элемент стека, но не удаляет его

    def size(self):  # возвращает количество элементов в стеке
        return len(self.stack)


def find_balance(bracket):
    list_opened = ['(', '[', '{']
    list_closed = [')', ']', '}']
    bracket_stack = Stack()
    for i in bracket:
        if i in list_opened:
            bracket_stack.push(i)
        elif i in list_closed:
            el = list_closed.index(i)
            if not bracket_stack.isEmpty() and list_opened[el] == bracket_stack.peek():
                bracket_stack.pop()
            else:
                return 'Несбалансированно'
    if bracket_stack.isEmpty():
        return 'Сбалансированно'
    else:
        return 'Несбалансированно'


print(find_balance('(((([{}]))))'))
print(find_balance('[([])((([[[]]])))]{()}'))
print(find_balance('{{[()]}}'))
print(find_balance('{{[(])]}}'))
print(find_balance('}{}'))
print(find_balance('[[{())}]'))
