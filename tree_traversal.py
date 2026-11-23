"""Обход бинарного дерева.

При обходе в глубину рекурсивно обходим левое и правое поддеревья.
Пустое поддерево пропускаем. Порядок записи значения узла определяет вид обхода.

Прямой: сначала узел, затем левое и правое поддеревья.
Симметричный: левое поддерево, затем узел и правое поддерево.
Обратный: левое и правое поддеревья, затем узел.

При обходе в ширину кладём корень в очередь. Берём узел из начала
очереди, записываем его значение и добавляем его детей в конец очереди
слева направо. Повторяем, пока очередь не опустеет.
"""

from collections import deque


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def preorder(node):
    if node is not None:
        yield node.value
        yield from preorder(node.left)
        yield from preorder(node.right)


def inorder(node):
    if node is not None:
        yield from inorder(node.left)
        yield node.value
        yield from inorder(node.right)


def postorder(node):
    if node is not None:
        yield from postorder(node.left)
        yield from postorder(node.right)
        yield node.value


def level_order(root):
    if root is None:
        return

    queue = deque([root])
    while queue:
        node = queue.popleft()
        yield node.value
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)


if __name__ == "__main__":
    root = Node(1, Node(2, Node(4), Node(5)), Node(3, right=Node(6)))

    print("Прямой обход:", *preorder(root))
    print("Симметричный обход:", *inorder(root))
    print("Обратный обход:", *postorder(root))
    print("Обход в ширину:", *level_order(root))
