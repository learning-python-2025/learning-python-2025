"""
Очереди
"""


#
from threading import Thread
from queue import Queue

q1 = Queue()

q1.put(1)
q1.put(2)


print(f"Item 1 from queue = {q1.get()}")
print(f"Item 2 from queue = {q1.get()}")
print(f"Item 3 from queue = {q1.get()}")  # очередь заблокируется
print(f"Item 4 from queue = {q1.get()}")
# в линейной , не многопоточной схеме использовать бессмысленно

#
numbers_queue = Queue()
pows_queue = Queue()


def gen_numbers(from_num: int, to_num: int, n_queue: Queue):
    while from_num <= to_num:
        print(f"T1: put {from_num} to queue")
        n_queue.put(from_num)
        from_num += 1


def pow_numbers(num_q: Queue, pow_queue: Queue):
    while True:
        number = num_q.get()
        if number % 2 == 0:

            pow_queue.put(number ** 2)
            print(f"T2: put {number} **2 to queue")


def print_result(res_q: Queue):
    while True:
        print(f"T3: Result: {res_q.get()}")


t1 = Thread(target=gen_numbers, args=(1, 10, numbers_queue))
t2 = Thread(target=pow_numbers, args=(numbers_queue, pows_queue))

t1.start()
t2.start()

print_result(pows_queue)
