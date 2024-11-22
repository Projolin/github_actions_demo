def add_arrays(arr1, arr2):
    return [x + y for x, y in zip(arr1, arr2)]

if __name__ == "__main__":
    print(add_arrays([1, 2, 3], [4, 5, 6]))
