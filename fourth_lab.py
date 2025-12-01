from typing import Tuple


class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

def insert(root: Node, value: int) -> Node:
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)
    return root

def collect_single_child_nodes(root: Node, result: list):
    if root is None:
        return
    if (root.left is None) != (root.right is None):  # ровно один ребёнок
        result.append(root.value)
    collect_single_child_nodes(root.left, result)
    collect_single_child_nodes(root.right, result)


def check_balanced(root: Node) -> Tuple[int, bool]:

    if root is None:
        return 0, True

    left_height, left_balanced = check_balanced(root.left)
    right_height, right_balanced = check_balanced(root.right)

    height = max(left_height, right_height) + 1
    balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1

    return height, balanced

if __name__ == '__main__':
    nums = [7, 3, 2, 1, 9, 5, 4, 6, 8, 0]
    root = None

    for x in nums:
        if x == 0:
            break
        root = insert(root, x)

    result = []

    collect_single_child_nodes(root, result)
    _, is_balanced = check_balanced(root)

    print(result)
    print("YES" if is_balanced else "NO")
