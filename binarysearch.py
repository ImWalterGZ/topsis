import time

def binary_search(array, searched):
    start = 0
    end = len(array) - 1

    while start <= end:
        center = (start + end) // 2
        if searched < array[center]:
            end = center - 1
        elif searched > array[center]:
            start = center + 1
        else:
            return center
    return -1

def main():
    array = []
    start = time.time()

    # Apendizar un millón de elementos a la lista
    for i in range(1, 1000001):
        array.append(i)


    result = binary_search(array, 54932)
    print(result)

    end = time.time()
    print(f"\n se tardó {int((end - start) * 1000)} milisegundos")

if __name__ == "__main__":
    main()
