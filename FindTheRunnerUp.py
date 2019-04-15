if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    max_length = len(set(arr))
    print(sorted(set(arr))[max_length - 2])