if __name__ == '__main__':
    n = int(input())
    for i in range(0,n+1):
        arr =map(int, input())
        arr=list(arr)
        arr.sort()
    print(arr[-2])