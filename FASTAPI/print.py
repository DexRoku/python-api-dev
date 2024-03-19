import threading
import multiprocessing
import time

def count_down(name, n):
    for i in range(n, 0, -1):
        print(f'{name}: {i}')
        time.sleep(1)

def square_numbers(numbers):
    for num in numbers:
        print('Square:', num * num)

def cube_numbers(numbers):
    for num in numbers:
        print('Cube:', num * num * num)

if __name__ == "__main__":
    # Example using threading
    print("Threading Example:")
    t1 = threading.Thread(target=count_down, args=('Thread 1', 5))
    t2 = threading.Thread(target=count_down, args=('Thread 2', 3))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    # Example using multiprocessing
    print("\nMultiprocessing Example:")
    numbers = [1, 2, 3, 4, 5]
    p1 = multiprocessing.Process(target=square_numbers, args=(numbers,))
    p2 = multiprocessing.Process(target=cube_numbers, args=(numbers,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Done")
