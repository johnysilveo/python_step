import queue
import threading
import time
from concurrent.futures import ProcessPoolExecutor


# def print_numbers():
#     for i in range(1,6):
#         print(f"{threading.current_thread().name}\nNumber: {i}")
#         time.sleep(1)
#
# def print_letters():
#     for letter in "ABCD":
#         print(f"{threading.current_thread().name}\nLetter: {letter}")
#         time.sleep(1.5)
#
# # print_numbers()
# # print_letters()
#
# t1 = threading.Thread(target=print_numbers,name="print_numbers")
# t2 = threading.Thread(target=print_letters,name="print_letters")
# t1.start()
# t2.start()
#
# for j in range(6):
#     print(f"\nMain tick {j}. Active thread{threading.} = {threading.active_count()}")
#     time.sleep(0.5)
# t1.join()
# t2.join()
# print("All threads are finished")


def demo_lock_race(iterations:int = 50000,workers:int = 5) -> None:
    counter = 0
    lock = threading.Lock()
    def inc()-> None:
        nonlocal counter
        for i in range(iterations):
            with lock:
                counter += 1
    threads = [threading.Thread(target=inc,name=f"INC-{counter}") for i in range(workers)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(f"Lock is waiting for {iterations*workers} result {counter}")
#demo_lock_race()

def demo_queue()-> None:
    task_queue: queue.Queue[object] = queue.Queue()
    sentinel = object()
    def worker()-> None:
        for task in iter(task_queue.get,sentinel):
            try:
                print(f"[{threading.current_thread().name} ]working with {task}",flush=True)
                time.sleep(0.25)
            finally:
                task_queue.task_done()
        task_queue.task_done()
    for i in range(8):
        task_queue.put(f"Task-{i}")
    threads = [threading.Thread(target=worker,name=f"W{i}")for i in range(3)]
    for i in threads:
        i.start()
    for _ in threads:
        task_queue.put(sentinel)

    task_queue.join()
    for t in threads:
        t.join()

        print(f"All tasks are finished")

# demo_queue()

def cpu_task(n:int) -> None:
    s = 0
    for _ in range(n):
        s+=1
    return s

def benchmark_cpu_test(work:int = 1000000,workers:int=4) -> None:
    print(f"CPU - bound: work={work}, workers={workers}")
    start = time.perf_counter()
    result_t=[]
    def run_thread():
        result_t.append(cpu_task(work))
    threads = [threading.Thread(target=run_thread,name=f"CPU_T{i}")for i in range(workers)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    t_time = time.perf_counter() - start
    print(f"THreads: {t_time:.3f}s")

    #============Processors+++++++++++++++++++

    start = time.perf_counter()
    with ProcessPoolExecutor(max_workers=workers)as ex:
        result_p = list(ex.map(cpu_task,[work]*workers))
    p_time = time.perf_counter() - start
    print(f"ProcessPool: {p_time:.3f}s")
if __name__ == '__main__':
    benchmark_cpu_test()