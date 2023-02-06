class BoyerMoore:
    def __init__(self):
        self.BCT = []
        self.GST = dict()

    def bad_character_rule(self, S, alphabet):
        alphabet = list(alphabet)
        self.BCT.append([S[i] for i in range(len(S))])
        self.BCT[0] = ["*"] + self.BCT[0]
        for c in alphabet:
            self.BCT.append([c] + [0] * len(S))

        for i in range(1, len(alphabet) + 1):
            k=0
            for j in range(1, len(S) + 1):
                if self.BCT[i][0] == self.BCT[0][j]:
                    k = 0
                else:
                    k = k + 1
                self.BCT[i][j] = k

        return self.BCT

    def good_suffix_rule(self, S):
        for i, c in enumerate(S):
            self.GST[i] = (c, 0)
        for i in range(len(S) - 1, 0, -1):
            max_occurrence = 0
            suffix = S[i:len(S)]
            for j in range(len(suffix), len(S)):
                if S[j - len(suffix):j] == suffix and (
                        S[i - 1] != S[j - len(suffix) - 1] or j == len(suffix)) and j - 1 != len(S) - 1:
                    max_occurrence = j - 1
            self.GST[i] = (self.GST[i][0], max_occurrence)

        H = dict()
        for i, c in enumerate(S):
            H[i] = (c, 0)
        for i in range(len(S) - 1, -1, -1):
            if S[i:len(S)] == S[0:len(S) - i]:
                for j in range(i + 1):
                    H[j] = (H[j][0], len(S) - i)

        return self.GST, H

    def string_search(self, S, T):
        alphabet = list(set([S[i] for i in range(len(S))]))
        BCT = self.bad_character_rule(S, alphabet)
        GST, H = self.good_suffix_rule(S)
        print(BCT)
        print(GST)
        print(H)

        matches = []

        k = len(S) - 1
        previous_k = -1  # Galil's rule
        while k < len(T):
            print(k)
            i = k  # Index on T
            j = len(S) - 1  # Index on S

            while j >= 0 and i > previous_k and T[i] == S[j]:
                i = i - 1
                j = j - 1
            if j == -1 or i == previous_k:
                matches.append(k)
                k += len(S) - H[1][1] if len(S) > 1 else 1
            elif T[i] not in alphabet:
                k += len(S)
            else:
                char_shift = BCT[alphabet.index(T[i])+1][j+1]
                if j + 1 == len(S):
                    suffix_shift = 1
                elif GST[j + 1] == 0:
                    suffix_shift = len(S) - H[j + 1][1]
                else:
                    suffix_shift = len(S) - GST[j + 1][1] - 1
                shift = max(char_shift, suffix_shift)
                previous_k = k if shift >= j + 1 else previous_k
                k += shift
        return matches


print(BoyerMoore().string_search("banana", "nananabanananonaoninabanananoniananodfinabananaopidbananbanananananonibananoninabanana"))
