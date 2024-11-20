import numpy as np
import matplotlib.pyplot as plt
import time

class PriorityQueueHeap:
    def __init__(self):
        self.array = []

    def insert(self, x, p):
        self.array.append((x, p))
        self.heap_up(len(self.array) - 1)

    def extractMax(self):
        if not self.array:
            raise Exception("Priority queue is empty")
        max_element = self.array[0][0]
        self.array[0] = self.array[-1]
        self.array.pop()
        self.heap_down(0)
        return max_element

    def heap_up(self, index):
        parent_index = (index - 1)//2
        if index > 0 and self.array[index][1] > self.array[parent_index][1]:
            self.array[index], self.array[parent_index] = self.array[parent_index], self.array[index]
            self.heap_up(parent_index)

    def heap_down(self, index):
        largest = index
        lс = 2*index + 1
        rс = 2*index + 2
        if lс < len(self.array) and self.array[lс][1] > self.array[largest][1]:
            largest = lс
        if rс < len(self.array) and self.array[rс][1] > self.array[largest][1]:
            largest = rс
        if largest != index:
            self.array[index], self.array[largest] = self.array[largest], self.array[index]
            self.heap_down(largest)

class PriorityQueueLazy:
    def __init__(self):
        self.array = []

    def insert(self, x, p):
        self.array.append((x, p))

    def extractMax(self):
        if not self.array:
            raise Exception("Priority queue is empty")
        max_index = 0
        for i in range(1, len(self.array)):
            if self.array[i][1] > self.array[max_index][1]:
                max_index = i
        return self.array.pop(max_index)[0]

def count_time(queue, num_operations):
    for i in range(num_operations):
        queue.insert(i, np.random.randint(0, num_operations))

    insert_times = []
    extract_times = []
    trials = 10

    for i in range(trials):
        start = time.time_ns()
        queue.insert(1, np.random.randint(0, num_operations))
        end = time.time_ns()
        insert_times.append(end - start)

        start = time.time_ns()
        queue.extractMax()
        end = time.time_ns()
        extract_times.append(end - start)

    return sum(insert_times) / trials, sum(extract_times) / trials


sizes = [10000, 20000, 30000, 40000, 50000]
heap_insert_times = []
heap_extract_times = []

lazy_insert_times = []
lazy_extract_times = []

for size in sizes:
    heap_queue = PriorityQueueHeap()
    lazy_queue = PriorityQueueLazy()

    insert_time, extract_time = count_time(heap_queue, size)
    heap_insert_times.append(insert_time)
    heap_extract_times.append(extract_time)

    insert_time, extract_time = count_time(lazy_queue, size)
    lazy_insert_times.append(insert_time)
    lazy_extract_times.append(extract_time)

plt.figure(figsize=(10, 6))
#plt.plot(sizes, heap_insert_times, label="Вставка в бинарную кучу", marker='o')
#plt.plot(sizes, heap_extract_times, label="Извлечение из бинарной кучи", marker='o')
plt.plot(sizes, lazy_insert_times, label="Вставка в массив ленивые вычисления", marker='o')
plt.plot(sizes, lazy_extract_times, label="Извлечение из массива ленивые вычисления", marker='o')
plt.xlabel("Количество")
plt.ylabel("Время")
plt.legend()
plt.grid(True)
plt.show()