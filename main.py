class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p, q):
    # Якщо обидва вузли відсутні,
    # дерева в цій частині однакові
    if p is None and q is None:
        return True

    # Якщо один вузол є, а іншого немає,
    # структура дерев відрізняється
    if p is None or q is None:
        return False

    # Якщо значення вузлів різні,
    # дерева не є однаковими
    if p.val != q.val:
        return False

    # Перевіряємо ліві та праві піддерева
    return (
        isSameTree(p.left, q.left)
        and isSameTree(p.right, q.right)
    )


# ==========================================
# ТЕСТУВАННЯ
# ==========================================

# Приклад 1:
# p = [1,2,3]
# q = [1,2,3]
# Очікуваний результат: True

p1 = TreeNode(1)
p1.left = TreeNode(2)
p1.right = TreeNode(3)

q1 = TreeNode(1)
q1.left = TreeNode(2)
q1.right = TreeNode(3)

print("Приклад 1:", isSameTree(p1, q1))


# Приклад 2:
# p = [1,2]
# q = [1,null,2]
# Очікуваний результат: False

p2 = TreeNode(1)
p2.left = TreeNode(2)

q2 = TreeNode(1)
q2.right = TreeNode(2)

print("Приклад 2:", isSameTree(p2, q2))


# Приклад 3:
# p = [1,2,1]
# q = [1,1,2]
# Очікуваний результат: False

p3 = TreeNode(1)
p3.left = TreeNode(2)
p3.right = TreeNode(1)

q3 = TreeNode(1)
q3.left = TreeNode(1)
q3.right = TreeNode(2)

print("Приклад 3:", isSameTree(p3, q3))