
test_data = [4, 6, 8, 1, 2, 5, 4, 8, 3, 6, 7, 8]

if __name__ == '__main__':

    def bubble_sort(input_data: list) -> list:
        len_list = len(input_data)
        for i in range(len_list):
            for j in range(0, len_list - i - 1):
                if input_data[j] > input_data[j + 1]:
                    input_data[j], input_data[j + 1] = input_data[j + 1], input_data[j]
        return input_data

    print(f"1.1 Bubble sort result: {bubble_sort(test_data)}")


    def merge(left: list, right: list) -> list:
        result = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result


    def merge_sort(input_data: list) -> list:
        if len(input_data) <= 1:
            return input_data

        mid = len(input_data) // 2
        left = merge_sort(input_data[:mid])
        right = merge_sort(input_data[mid:])

        return merge(left, right)

    print(f"1.2 Merge sort result: {merge_sort(test_data)}")


    def quick_sort(input_data: list) -> list:
        if len(input_data) <= 1:
            return input_data

        pivot = input_data[len(input_data) // 2]
        left = [x for x in input_data if x < pivot]
        middle = [x for x in input_data if x == pivot]
        right = [x for x in input_data if x > pivot]

        return quick_sort(left) + middle + quick_sort(right)

    print(f"1.3 Quick sort result: {quick_sort(test_data)}")
