def solution(A):
    ans = 1001


    for i in range(1, len(A)):
        print(A[i])
        if A[i] < ans:
            ans = A[i]

    return ans


if __name__ == '__main__':
    

    A = [-1, 1, -2, 2]
    print(solution(A))
