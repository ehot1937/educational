
sequence= "())(()"


def correct_sequence(s: str) -> int:
    open_count = 0
    remove_count = 0

    for symbol in s:
        if symbol == '(':
            open_count += 1
        else:
            if open_count > 0:
                open_count -= 1
            else:
                remove_count += 1

    return remove_count + open_count


n = "10"
s = "1232142531"

def nearest_smaller(n: str, s: str) -> list:
    len_s = int(n)
    list_s = [x for x in s]
    stack = []
    result = [-1] * len_s

    for i in reversed(range(len_s)):
        while stack and list_s[stack[-1]] >= list_s[i]:
            stack.pop()

        if stack:
            result[i] = stack[-1]

        stack.append(i)

    return result


if __name__ == '__main__':

    print(f"3.1 Correct sequence result: {correct_sequence(sequence)}")

    print(f"3.2 Nearest smaller result: {nearest_smaller(n, s)}")
