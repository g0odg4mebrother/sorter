
import random
import time

def bubble_sort(arr):
    n = len(arr)
    swaps = 0
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
    return swaps

def insertion_sort(arr):
    n = len(arr)
    swaps = 0
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
            swaps += 1
        arr[j+1] = key
    return swaps

def selection_sort(arr):
    n = len(arr)
    swaps = 0
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        swaps += 1
    return swaps

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    return merge(merge_sort(left), merge_sort(right))

def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left)
    result.extend(right)
    return result

def shaker_sort(arr):
    n = len(arr)
    swaps = 0
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
        for j in range(n-i-2, -1, -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
    return swaps

def generate_array(size):
    return [random.randint(0, 10) for _ in range(size)]

def sort_and_measure(arr, sort_func):
    start_time = time.time()
    swaps = sort_func(arr.copy())
    end_time = time.time()
    return end_time - start_time, swaps

def main():
    n = int(input("введите число\n"))
    b = int(input("введите число\n"))
    g = int(input("введите число\n"))
    sizes = [n,b,g]
    for size in sizes:
        arr = generate_array(size)
        print(f"Array size: {size}")
        for sort_func in [bubble_sort, insertion_sort, selection_sort, quick_sort, merge_sort, shaker_sort]:
            times = []
            swaps = []
            for _ in range(5):
                time_taken, swap_count = sort_and_measure(arr, sort_func)
                times.append(time_taken)
                swaps.append(swap_count)
            best_time = min(times)
            best_swaps = swaps[times.index(best_time)]
            print(f"{sort_func.__name__}: {best_time:.6f} sec, {best_swaps} swaps")
main()


