class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return self.value


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(elem)
                node = node.next

    class EmptyLinkedListError(Exception):
        def __init__(self):
            message = "The linked list is empty"
            super().__init__(message)

    class NotInLinkedListError(Exception):
        def __init__(self, target):
            message = "The value {} is not in the linked list"
            super().__init__(message.format(target))

    def __repr__(self):
        if self.head is None:
            raise self.EmptyLinkedListError

        values = [node.value for node in self]
        return " ->\n".join(values)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_front(self, value):
        self.head = Node(value, self.head)

    def add_back(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            for node in self:
                pass

            node.next = Node(value)

    def add_after(self, value, target):
        if self.head is None:
            raise self.EmptyLinkedListError

        for node in self:
            if node.value == target:
                following = node.next
                node.next = Node(value, following)
                return

        raise self.NotInLinkedListError(target)

    def add_before(self, value, target):
        if self.head is None:
            raise self.EmptyLinkedListError
        elif self.head.value == target:
            return self.add_front(value)

        for node in self:
            if node.next is not None and node.next.value == target:
                following = node.next
                node.next = Node(value, following)
                return

        raise self.NotInLinkedListError(target)

    def remove_node(self, target):
        if self.head is None:
            raise self.EmptyLinkedListError

        for node in self:
            if node.next is not None and node.next.value == target:
                target_node = node.next
                node.next = target_node.next
                return

        raise self.NotInLinkedListError(target)
