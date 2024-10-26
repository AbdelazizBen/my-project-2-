import random
import time


def bubble_sort_basic(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    for i in range(n):
        for j in range(n - 1 - i):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
    return comparisons, swaps


def bubble_sort_optimized(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                swapped = True
        if not swapped: 
            break
    return comparisons, swaps


def create_datasets():
    return {
        "Sorted": [list(range(1, 101)), list(range(1, 501)), list(range(1, 1001))],
        "Reverse Sorted": [list(range(100, 0, -1)), list(range(500, 0, -1)), list(range(1000, 0, -1))],
        "Random": [random.sample(range(1, 101), 100), random.sample(range(1, 501), 500), random.sample(range(1, 1001), 1000)],
    }


def collect_data():
    datasets = create_datasets()
    results = []

    for dataset_type, dataset_list in datasets.items():
        for dataset in dataset_list:
           
            data_basic = dataset.copy()
            data_optimized = dataset.copy()

         
            start_time = time.time()
            comparisons_basic, swaps_basic = bubble_sort_basic(data_basic)
            time_basic = time.time() - start_time

        
            start_time = time.time()
            comparisons_optimized, swaps_optimized = bubble_sort_optimized(data_optimized)
            time_optimized = time.time() - start_time

           
            results.append({
                "Dataset Type": dataset_type,
                "Size of Dataset": len(dataset),
                "Time Basic (s)": time_basic,
                "Time Optimized (s)": time_optimized,
                "Comparisons Basic": comparisons_basic,
                "Comparisons Optimized": comparisons_optimized,
                "Swaps Basic": swaps_basic,
                "Swaps Optimized": swaps_optimized,
            })

    return results


results = collect_data()


print(f"{'Dataset Type':<20} {'Size of Dataset':<15} {'Time Basic (s)':<15} {'Time Optimized (s)':<18} {'Comparisons Basic':<20} {'Comparisons Optimized':<25} {'Swaps Basic':<15} {'Swaps Optimized':<15}")
for result in results:
    print(f"{result['Dataset Type']:<20} {result['Size of Dataset']:<15} {result['Time Basic (s)']:<15.6f} {result['Time Optimized (s)']:<18.6f} {result['Comparisons Basic']:<20} {result['Comparisons Optimized']:<25} {result['Swaps Basic']:<15} {result['Swaps Optimized']:<15}")
