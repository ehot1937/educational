

if __name__ == '__main__':

    S = "ababbababa"
    T = "aba"

    def build_prefix_function(t_str: str) -> list:
        prefix = [0] * len(t_str)
        j = 0

        for i in range(1, len(t_str)):
            while j > 0 and t_str[i] != t_str[j]:
                print(t_str[i])
                j = prefix[j - 1]

            if t_str[i] == t_str[j]:
                j += 1

            prefix[i] = j

        return prefix


    def kmp_search(s_str: str, t_str: str) -> list:
        if not t_str:
            return []

        prefix = build_prefix_function(t_str)
        result = []
        j = 0

        for i in range(len(s_str)):
            while j > 0 and s_str[i] != t_str[j]:
                j = prefix[j - 1]

            if s_str[i] == t_str[j]:
                j += 1

            if j == len(t_str):
                result.append(i - j + 1)
                j = prefix[j - 1]

        return result

    print(f"2.1 result: {kmp_search(S, T)}")


    S = "zabcd"
    T = "abcdz"

    def prefix_function(t: str) -> list:
        len_t = len(t)
        pi = [0] * len_t
        j = 0
        for i in range(1, len_t):
            while j > 0 and t[i] != t[j]:
                j = pi[j - 1]
            if t[i] == t[j]:
                j += 1
            pi[i] = j
        return pi


    def kmp_search(doubled_s: str, t: str):
        pi = build_prefix_function(t)
        j = 0
        for i in range(len(doubled_s)):
            while j > 0 and doubled_s[i] != t[j]:
                j = pi[j - 1]
            if doubled_s[i] == t[j]:
                j += 1
            if j == len(t):
                return i - j + 1
        return -1

    def cyclical_shift(s: str, t: str) -> int:
        len_s = len(s)

        if len_s != len(t):
            return -1
        else:
            doubled_s = s + s
            pos = kmp_search(doubled_s, t)

            if pos == -1 or pos >= len(s):
                return -1
            else:
                shift = (len_s - pos) % len_s
                return shift
    print(f"2.2 Cyclical shift result: {cyclical_shift(S, T)}")
