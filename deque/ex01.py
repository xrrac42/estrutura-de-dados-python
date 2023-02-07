from collections import deque
from operator import is_
queue = deque([])

a = input()

for i in a:
    if i.isdigit():
        queue.append(i)
    if i.isalpha() or i == ' ':
        queue.appendleft(i)
    if i == '*':
        queue.appendleft(i)
        queue.popleft()
    if i == '+':
        queue.append(i)
        queue.pop()

for j in queue: print(j,end='')