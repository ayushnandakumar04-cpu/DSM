#Path Sum
def path_sum(root, target):
    if root is None:
        return False

    target = target - root.val

    if root.left is None and root.right is None:
        return target == 0

    return path_sum(root.left, target) or path_sum(root.right, target)