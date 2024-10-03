#myfunc(2):
    # M = list(range(2,0,-1))
    # P = M                            
    # print(M)                [2, 1]
    # M[0] = n+1              [3, 1] P = M -> If M is affected then P also affected too
    # print(P)                [3, 1]
    # Q = P + [10]            [3, 1, 10]
    # Q.sort()                [1, 3, 10]
    # print(Q)                [1, 3, 10]
    # P.pop()                 [3] P popped 1 out, meaning M also popped 1 out
    # print(P)                [3]
    # return [P, M, Q]        [[3], [3], [1, 3, 10]]

def myfunc(n):
    M = list(range(2,0,-1))
    P = M
    print(M)
    M[0] = n+1
    print(P)
    Q = P + [10]
    Q.sort()
    print(Q)
    P.pop()
    print(P)
    return [P, M, Q]

print(myfunc(2))