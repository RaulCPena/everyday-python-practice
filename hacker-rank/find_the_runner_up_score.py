# you are given a score sheet of a university sports day and you need to find the runner-up, however you are only given n scores. Store them in a list and find the score of the runner-up


# Constraints
# 2<=n <= 10
# --100<=A[i]<=100
"""
Sample Input of
>>> list = [2, 3, 6, 6, 5]
Expected output of
>>> 5

"""
# map(function, iterable...)
# given list [2,3,6,6,5] The maximum score is 6, second maximum is 5 Hence we print 5 as the runner-up score



# def runner_up(a):
#     l = list(input())
#     print(max(list(filter(lambda x: x != max(l), l))))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    count = arr.count(arr[0])
    print(arr[count])
