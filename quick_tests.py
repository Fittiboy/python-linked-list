import linked_lists as ll

nodes = ["Node 1", "Node 2", "Node 3"]
list1 = ll.LinkedList(nodes)
list1.add_back("Node 7")
list1.add_front("Node 0")
list1.add_after("Node 4", "Node 3")
list1.add_before("Node 5", "Node 7")
list1.remove_node("Node 7")
print(list1, end="\n\n")
try:
    list1.remove_node(1)
except list1.NotInLinkedListError:
    pass
try:
    list1.add_after(1, 2)
except list1.NotInLinkedListError:
    pass
try:
    list1.add_before(1, 2)
except list1.NotInLinkedListError:
    pass

back_first_test = ll.LinkedList()
back_first_test.add_back("Node 1")
print(back_first_test)

empty_list = ll.LinkedList()
try:
    empty_list.remove_node(1)
except empty_list.EmptyLinkedListError:
    pass
try:
    empty_list.add_after(1, 2)
except empty_list.EmptyLinkedListError:
    pass
try:
    empty_list.add_before(1, 2)
except empty_list.EmptyLinkedListError:
    pass
