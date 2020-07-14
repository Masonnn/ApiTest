import queue

q = queue.PriorityQueue()

q.put((1, "work"))
q.put((-1, "life"))
q.put((1, "drink"))
q.put((-2, "sleep"))
print(q.get())
print(q.get())
print(q.get())
print(q.get())
