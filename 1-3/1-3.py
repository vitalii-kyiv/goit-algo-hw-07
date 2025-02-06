class Node:
    """Клас вузла для представлення елемента двійкового дерева пошуку."""
    def __init__(self, data):
        """Ініціалізація вузла.
        
        Args:
            data (int): Значення вузла.
        """
        self.data = data
        self.left_child = None
        self.right_child = None

class BinarySearchTree:
    """Клас для реалізації двійкового дерева пошуку."""
    def __init__(self):
        """Ініціалізація дерева з порожнім коренем."""
        self.root = None

    def insert(self, data):
        """Додає новий вузол у дерево.
        
        Args:
            data (int): Значення, яке потрібно додати.
        """
        if not self.root:
            print(f'Вузол {data} був вставлений')
            self.root = Node(data)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        """Рекурсивне додавання нового вузла.
        
        Args:
            data (int): Значення нового вузла.
            node (Node): Поточний вузол для порівняння.
        """
        if data < node.data:
            if node.left_child:
                self.insert_node(data, node.left_child)
            else:
                print(f'Вузол {data} був вставлений')
                node.left_child = Node(data)
        else:
            if node.right_child:
                self.insert_node(data, node.right_child)
            else:
                print(f'Вузол {data} був вставлений')
                node.right_child = Node(data)

    def get_max_value(self):
        """Повертає максимальне значення у дереві.
        
        Returns:
            int: Найбільше значення у дереві.
        """
        if self.root:
            return self.get_max(self.root)

    def get_max(self, node):
        """Рекурсивний пошук найбільшого значення у дереві.
        
        Args:
            node (Node): Поточний вузол.
        
        Returns:
            int: Найбільше значення у дереві.
        """
        if node.right_child:
            return self.get_max(node.right_child)
        return node.data

    def get_min_value(self):
        """Повертає мінімальне значення у дереві.
        
        Returns:
            int: Найменше значення у дереві.
        """
        if self.root:
            return self.get_min(self.root)

    def get_min(self, node):
        """Рекурсивний пошук найменшого значення у дереві.
        
        Args:
            node (Node): Поточний вузол.
        
        Returns:
            int: Найменше значення у дереві.
        """
        if node.left_child:
            return self.get_min(node.left_child)
        return node.data 
    
    def get_nodes_sum(self, path):
        """Обчислює суму всіх значень вузлів у дереві.
        
        Args:
            path (list): Список вузлів у дереві.
        
        Returns:
            int: Сума значень всіх вузлів.
        """
        if self.root:
            self.pre_order_traversal(self.root, path)
        return sum(node.data for node in path)

    def pre_order_traversal(self, node, path):
        """Обхід дерева в порядку pre-order (корінь -> лівий піддерево -> правий піддерево).
        
        Args:
            node (Node): Поточний вузол.
            path (list): Список вузлів, через які пройшли.
        """
        if node:
            path.append(node)
            self.pre_order_traversal(node.left_child, path)
            self.pre_order_traversal(node.right_child, path)

if __name__ == '__main__':
    bst = BinarySearchTree()
    path = []
    bst.insert(10)  
    bst.insert(13)
    bst.insert(27)
    bst.insert(12)
    bst.insert(1)
    bst.insert(3)
    bst.insert(2)
    bst.insert(4)
    print("Max node value", bst.get_max_value())
    print("Min node value", bst.get_min_value())
    print("Sum of all nodes", bst.get_nodes_sum(path))