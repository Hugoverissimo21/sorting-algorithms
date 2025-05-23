# ========== Sorting Algorithms ==========
# This module contains implementations of various sorting algorithms.
# Each function takes a list and returns a sorted list.

# ========== Bubble Sort ==========

def bubble_sort(arr):
    n = len(arr)
    count = 0

    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            count += 1  # comparison
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                count += 1  # swap
                swapped = True
        if not swapped:
            break
    return arr, count

# ========== Selection Sort ==========

def selection_sort(arr):
    n = len(arr)
    count = 0

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            count += 1  # comparison
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            count += 1  # swap
    return arr, count

# ========== Insertion Sort ==========

def insertion_sort(arr):
    count = 0

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0:
            count += 1  # comparison
            if arr[j] > key:
                arr[j + 1] = arr[j]
                count += 1  # shift
                j -= 1
            else:
                break
        arr[j + 1] = key
    return arr, count

# ========== Counting Sort ==========

def counting_sort(arr):
    count_ops = 0

    max_val = max(arr)
    count = [0] * (max_val + 1)

    for num in arr:
        count[num] += 1
        count_ops += 1  # increment count

    sorted_arr = []
    for i, c in enumerate(count):
        count_ops += 1  # loop iteration
        if c > 0:
            sorted_arr.extend([i] * c)
            count_ops += c  # extending sorted_arr by c elements

    return sorted_arr, count_ops

# ========== Radix Sort ==========

def radix_sort(arr):
    count_ops = 0

    def counting_sort_radix(arr, exp):
        nonlocal count_ops
        n = len(arr)
        output = [0] * n
        count = [0] * 10

        for i in range(n):
            index = (arr[i] // exp) % 10
            count[index] += 1
            count_ops += 1  # counting increment

        for i in range(1, 10):
            count[i] += count[i - 1]
            count_ops += 1  # prefix sum update

        for i in range(n - 1, -1, -1):
            index = (arr[i] // exp) % 10
            output[count[index] - 1] = arr[i]
            count[index] -= 1
            count_ops += 2  # placement + decrement

        for i in range(n):
            arr[i] = output[i]
            count_ops += 1  # copy back

    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort_radix(arr, exp)
        exp *= 10
    return arr, count_ops

# ========== Quick Sort ==========

def quick_sort(arr):
    count = 0

    def _quick_sort(items, low, high):
        nonlocal count
        if low < high:
            pivot_index = partition(items, low, high)
            _quick_sort(items, low, pivot_index - 1)
            _quick_sort(items, pivot_index + 1, high)

    def partition(items, low, high):
        nonlocal count
        pivot = items[high]
        i = low - 1
        for j in range(low, high):
            count += 1  # comparison
            if items[j] <= pivot:
                i += 1
                items[i], items[j] = items[j], items[i]
                count += 1  # swap
        items[i + 1], items[high] = items[high], items[i + 1]
        count += 1  # swap
        return i + 1

    _quick_sort(arr, 0, len(arr) - 1)
    return arr, count

# ========== Merge Sort ==========

def merge_sort(arr):
    count = 0

    def _merge_sort(arr):
        nonlocal count
        if len(arr) > 1:
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]

            _merge_sort(left)
            _merge_sort(right)

            i = j = k = 0
            while i < len(left) and j < len(right):
                count += 1  # comparison
                if left[i] <= right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1
                count += 1  # copy

            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1
                count += 1  # copy

    _merge_sort(arr)
    return arr, count

# ========== Heap Sort ==========

def heap_sort(arr):
    count = 0

    def heapify(arr, n, i):
        nonlocal count
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n:
            count += 1  # comparison
            if arr[left] > arr[largest]:
                largest = left

        if right < n:
            count += 1  # comparison
            if arr[right] > arr[largest]:
                largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            count += 1  # swap
            heapify(arr, n, largest)

    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        count += 1  # swap
        heapify(arr, i, 0)

    return arr, count

# ========== Timsort ==========

def timsort(arr):
    MIN_RUN = 32
    count = 0

    def insertion_sort(left, right):
        nonlocal count
        for i in range(left + 1, right + 1):
            key = arr[i]
            j = i - 1
            while j >= left:
                count += 1  # comparison
                if arr[j] > key:
                    arr[j + 1] = arr[j]
                    count += 1  # shift
                    j -= 1
                else:
                    break
            arr[j + 1] = key

    def merge(left, mid, right):
        nonlocal count
        left_part = arr[left:mid + 1]
        right_part = arr[mid + 1:right + 1]
        i = j = 0
        k = left
        while i < len(left_part) and j < len(right_part):
            count += 1  # comparison
            if left_part[i] <= right_part[j]:
                arr[k] = left_part[i]
                i += 1
            else:
                arr[k] = right_part[j]
                j += 1
            k += 1
        while i < len(left_part):
            arr[k] = left_part[i]
            i += 1
            k += 1
            count += 1  # copy
        while j < len(right_part):
            arr[k] = right_part[j]
            j += 1
            k += 1
            count += 1  # copy

    n = len(arr)
    for start in range(0, n, MIN_RUN):
        insertion_sort(start, min(start + MIN_RUN - 1, n - 1))

    size = MIN_RUN
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min(n - 1, left + 2 * size - 1)
            if mid < right:
                merge(left, mid, right)
        size *= 2

    return arr, count


if __name__ == "__main__":
    # Example usage
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr)
    sorted_arr, count = bubble_sort(arr.copy())
    print("Bubble Sort:", sorted_arr, "Comparisons:", count)
    sorted_arr, count = selection_sort(arr.copy())
    print("Selection Sort:", sorted_arr, "Comparisons:", count)
    sorted_arr, count = insertion_sort(arr.copy())
    print("Insertion Sort:", sorted_arr, "Comparisons:", count)
    sorted_arr, count = counting_sort(arr.copy())
    print("Counting Sort:", sorted_arr, "Operations:", count)
    sorted_arr, count = radix_sort(arr.copy())
    print("Radix Sort:", sorted_arr, "Operations:", count)
    sorted_arr, count = quick_sort(arr.copy())
    print("Quick Sort:", sorted_arr, "Comparisons:", count)
    sorted_arr, count = merge_sort(arr.copy())
    print("Merge Sort:", sorted_arr, "Comparisons:", count)
    sorted_arr, count = heap_sort(arr.copy())
    print("Heap Sort:", sorted_arr, "Comparisons:", count)
    sorted_arr, count = timsort(arr.copy())
    print("Timsort:", sorted_arr, "Comparisons:", count)