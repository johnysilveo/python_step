import os
import threading
import queue
import time
import re
import random

#>>>>>>>>>>>>>>>>>>================<<<<<<<<<<<<<<<<<<<
#>>>>>>>>>>>>>>>>>>  TASK1 threads <<<<<<<<<<<<<<<<<<<
#>>>>>>>>>>>>>>>>>>================<<<<<<<<<<<<<<<<<<<

def input1():
    numbers = []
    print("Enter numbers one by one. Type 'exit' to stop.")
    while True:
        value = input('Enter a numer (or exit): ')
        if value.lower() == 'exit':
            break
        numbers.append(int(value))
    return numbers

def max_number(nums):
    return max(nums)

def min_number(nums):
    return min(nums)

# def main():
#     nums = input1()
#     print(max_number(nums))
#     print(min_number(nums))
# if __name__ == '__main__':
#     main()

def worker_max(nums,out_q):
    out_q.put(max_number(nums))

def worker_min(nums,out_q):
    out_q.put(min_number(nums))

def main():
    nums = input1()
    if not nums:
        print("No numbers entered.")
        return
    q_max = queue.Queue()
    q_min = queue.Queue()
    t_max = threading.Thread(target=worker_max, args=(nums,q_max))
    t_min = threading.Thread(target=worker_min, args=(nums,q_min))
    t_max.start();t_min.start()
    t_max.join();t_min.join()
    time.sleep(3)
    max_v = q_max.get()
    min_v = q_min.get()
    print(f'min= {min_v}, max= {max_v}')

# if __name__ == '__main__':
#     main()

#>>>>>>>>>>>>>>>>>>================<<<<<<<<<<<<<<<<<<<
#>>>>>>>>>>>>>>>>>>  TASK2 threads <<<<<<<<<<<<<<<<<<<
#>>>>>>>>>>>>>>>>>>================<<<<<<<<<<<<<<<<<<<

def write_evens(nums, out_path, q):
    count = 0
    with open(out_path, "w", encoding="utf-8") as f:
        for n in nums:
            if n % 2 == 0:
                f.write(str(n) + "\n")
                count += 1
    q.put(count)

def write_odds(nums, out_path, q):
    count = 0
    with open(out_path, "w", encoding="utf-8") as f:
        for n in nums:
            if n % 2 != 0:
                f.write(str(n) + "\n")
                count += 1
    q.put(count)

def main():
    path = input("Enter path to file with numbers: ").strip()
    if not os.path.isfile(path):
        print("File not found")
        return
    with open(path, "r", encoding="utf-8") as f:
        numbers = [int(x) for x in f.read().split()]
    q_e, q_o = queue.Queue(), queue.Queue()
    even_path = os.path.splitext(path)[0] + "_evens.txt"
    odd_path  = os.path.splitext(path)[0] + "_odds.txt"
    t_e = threading.Thread(target=write_evens, args=(numbers, even_path, q_e), name="EVEN")
    t_o = threading.Thread(target=write_odds,  args=(numbers, odd_path,  q_o), name="ODD")
    t_e.start(); t_o.start()
    t_e.join();  t_o.join()
    even_count = q_e.get()
    odd_count = q_o.get()
    print(f"Even numbers: {even_count}")
    print(f"Odd numbers: {odd_count}")
    print(f"Files created: {even_path}, {odd_path}")

# if __name__ == "__main__":
#     main()

#>>>>>>>>>>>>>>>>>>================<<<<<<<<<<<<<<<<<<<
#>>>>>>>>>>>>>>>>>>TASK3 no threads<<<<<<<<<<<<<<<<<<<
#>>>>>>>>>>>>>>>>>>================<<<<<<<<<<<<<<<<<<<

def find_word_first_match():
    with open('report.txt','r',encoding="utf-8",errors='ignore') as file:
        content = file.read()
    word_to_find = input("Enter word to find: ").strip().lower()
    pattern = r"\b" + re.escape(word_to_find) + r"\b"
    word = re.search(pattern, content, flags=re.IGNORECASE)
    if word:
        print(f"First match: '{word.group()}' at position {word.start()}")
    else:
        print("No match found")

def find_words_all_matches():
    with open('report.txt','r',encoding="utf-8",errors='ignore') as file:
        content = file.read()
    word_to_find = input("Enter word to find: ").strip().lower()
    pattern = r"\b" + re.escape(word_to_find) + r"\b"
    found = False
    for m in re.finditer(pattern, content, flags=re.IGNORECASE):
        print(f"Found '{m.group()}' at position {m.start()}")
        found = True
    if not found:
        print("No match found")

def main():
    while True:
        print("\nChoose search mode:")
        print("  1) First match")
        print("  2) All matches")
        print("  3) Exit")
        choice = input("Your choice: ").strip()

        if choice == "1":
            find_word_first_match()
        elif choice == "2":
            find_words_all_matches()
        elif choice == "3" or choice == "":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Try again.")

# if __name__ == "__main__":
#     main()

#>>>>>>>>>>>>>>>>>>================<<<<<<<<<<<<<<<<<<<
#>>>>>>>>>>>>>>>>>>  TASK3 threads <<<<<<<<<<<<<<<<<<<
#>>>>>>>>>>>>>>>>>>================<<<<<<<<<<<<<<<<<<<


def search_first_worker(word_to_find: str):
    with open('report.txt', 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    pattern = r"\b" + re.escape(word_to_find) + r"\b"
    m = re.search(pattern, content, flags=re.IGNORECASE)
    if m:
        print(f"First match: '{m.group()}' at position {m.start()}")
    else:
        print("No match found")

def search_all_worker(word_to_find: str):
    with open('report.txt', 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    pattern = r"\b" + re.escape(word_to_find) + r"\b"
    found = False
    for m in re.finditer(pattern, content, flags=re.IGNORECASE):
        print(f"Found '{m.group()}' at position {m.start()}")
        found = True
    if not found:
        print("No match found")

def main():
    while True:
        print("\nChoose search mode:")
        print("  1) First match")
        print("  2) All matches")
        print("  3) Exit")
        choice = input("Your choice [1/2/3]: ").strip()

        if choice == "1":
            word = input("Enter word to find: ").strip().lower()
            t = threading.Thread(target=search_first_worker, args=(word,), daemon=True)
            t.start()
            t.join()
        elif choice == "2":
            word = input("Enter word to find: ").strip().lower()
            t = threading.Thread(target=search_all_worker, args=(word,), daemon=True)
            t.start()
            t.join()
        elif choice in ("3", ""):
            break
        else:
            print("Invalid choice. Try again.")

# if __name__ == "__main__":
#     main()


#>>>>>>>>>>>>>>>>>>================<<<<<<<<<<<<<<<<<<<
#>>>>>>>>>>>>>>>>>>  TASK4 threads <<<<<<<<<<<<<<<<<<<
#>>>>>>>>>>>>>>>>>>================<<<<<<<<<<<<<<<<<<<


import threading
import random

numbers = []
ready_event = threading.Event()

def fill_list():
    global numbers
    numbers = [random.randint(1, 100) for _ in range(10)]
    print(f"Generated list: {numbers}")
    ready_event.set()  # сигнал, що список готовий

def calc_sum():
    ready_event.wait()  # чекаємо, поки список заповниться
    total = sum(numbers)
    print(f"Sum: {total}")

def calc_average():
    ready_event.wait()  # чекаємо, поки список заповниться
    avg = sum(numbers) / len(numbers)
    print(f"Average: {avg:.2f}")

def main():
    t1 = threading.Thread(target=fill_list)
    t2 = threading.Thread(target=calc_sum)
    t3 = threading.Thread(target=calc_average)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

if __name__ == "__main__":
    main()
