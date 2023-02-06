def partial_match_table(S):
    i = 1  # (index on S)
    j = 0  # (moving index through prefixes)
    W = [-1] * len(S)
    while i < len(S):
        j = 0
        if S[i] == S[0]:
            W[i] = -1
            i = i + 1
        else:
            W[i] = 0
            for k in range(i - 1, 0, -1):
                j = j + 1
                if S[k] == S[0]:
                    if S[0:j] == S[k:k + j]:
                        W[i] = j
                    else:
                        break
            for k in range(i - W[i] + 1, i):
                if S[k] == S[0] or W[k]>=W[i]:
                    break
                W[k] = 0
            if W[i] == 1 and S[1] == S[i]:
                W[i] = 0
            i = i + 1
    return W


def kmp_search(S, T):
    # input:
    #  an array of characters, T (the text to be searched)
    #  an array of characters, S (the word sought)
    # output:
    # first occurrence position

    i = 0  # (the position of the current character in T)
    k = 0  # (the position of the current character in S)
    W = partial_match_table(S)  # an array of integers, W (the table, computed elsewhere)
    print(W)
    P = []

    while i < len(T):
        if S[k] == T[i]:
            i = i + 1
            k = k + 1
            if k == len(S):
                P.append(i - k)
                k = W[k - 1]
        else:
            k = W[k]
            if k < 0:
                i = i + 1
                k = k + 1
    return P


print(kmp_search("PARTICIPATE IN PARACHUTE", "LATELY I HAVE BEEN PARTICIPATING IN MANY ACTIVITIES, /"
                                             "BUT WHAT I WANT MOST IT TO PARTICIPATE IN PARACHUTE, /"
                                             "I THINK PARACHUTES ARE AWESOME."))
