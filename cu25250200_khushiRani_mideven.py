def hamming_distance(a, k):
    return bin(a^k).count('1')
T = int(input())

for _ in range(T):
    N, K = map(int,input().split())
    A = list (map(int,input().split()))
    A.sort(key=lambda x:(hamming_distance(x, K), x))
    print(*A)






