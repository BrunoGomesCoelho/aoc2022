from fastcore.basics import store_attr
from sys import stdin

lines = []
for line in stdin:
    lines.append(line.strip())

class Monkey:
    def __init__(self, items, operation_str, test_num, if_true, if_false):
        store_attr()
        self.inspect_count = 0

    def operation(self):
        old = self.items.pop(0)
        new = eval(self.operation_str)
        new = new % numerao
        return new

    def test(self, item):
        if item % self.test_num == 0:
            return self.if_true
        return self.if_false


monkeys = []
n_monkeys = 8
numerao = 1

for i in range(n_monkeys):
    _, starting, operation_str, test, if_true, if_false, _ = lines[i*7:i*7+7]

    items = starting.split(": ")[1]
    items = items.split(", ")
    items = [int(item) for item in items]

    operation_str = operation_str.split("=")[1].strip()

    if_true = int(if_true.split("monkey ")[1].strip())
    if_false = int(if_false.split("monkey ")[1].strip())
    test_num = int(test.split("by")[1].strip())
    numerao *= test_num

    monkeys.append(Monkey(items, operation_str, test_num, if_true, if_false))

print("big_num", numerao)

#  for j in range(20):
for j in range(10_000): # 1000
    for monkey_idx, monkey in enumerate(monkeys): # 4
        while monkey.items:  #  10
            item = monkey.operation()
            next_monkey = monkey.test(item)
            monkeys[next_monkey].items.append(item)
            monkey.inspect_count += 1


print([m.inspect_count for m in monkeys])


