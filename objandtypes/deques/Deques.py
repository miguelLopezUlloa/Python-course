from collections import deque

d = deque(["a", "b", "c"])
print(d)

d.append("ra")
d.appendleft("lft")
print(d)

d.pop()
d.popleft()
print(d)

d.clear()
print(d)

