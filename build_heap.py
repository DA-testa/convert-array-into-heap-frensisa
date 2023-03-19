# python3


def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    # use min heap and not max heap
    # use the swaps list to store the swaps
    # swaps.append((i, j))
    # where i and j are the indexes of the elements that were swapped
    n = len(data)
    for i in range(n // 2 - 1, -1, -1):
        heapify(data, i, n, swaps)

    return swaps

def heapify(arr, i, heap_size, swaps):
    left = 2 * i + 1
    right = 2 * i + 2
    smallest = i
    if left < heap_size and arr[left] < arr[smallest]:
        smallest = left
    if right < heap_size and arr[right] < arr[smallest]:
        smallest = right
    if smallest != i:
        swaps.append((i, smallest))
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, smallest, heap_size, swaps)

def main():
    input_type = input()
    if input_type == 'I\r':
        # input from keyboard
        n = int(input())
        data = list(map(int, input().split()))

    elif input_type == 'F\r':
        # input from file
        input_file = input()
        file = open(input_file, 'r')
        n = int(file.readline())
        data = list(map(int, file.readline().split()))
    else:
        print('Wrong input type')
        exit(1)

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))
    # and the swaps should be in the form of (i, j)

    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
#haha