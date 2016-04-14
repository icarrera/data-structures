import pytest

TEST_DATA_R = [2, 1, 3, 4]
TEST_DATA_L = [3, 2, 4, 1]


@pytest.fixture()
def bst_empty():
    from bst import BST
    return BST()


@pytest.fixture()
def bst():
    from bst import BST
    bst = BST()
    for val in TEST_DATA_R:
        bst.insert(val)
    return bst


@pytest.fixture()
def bst_l():
    from bst import BST
    bst = BST()
    for val in TEST_DATA_L:
        bst.insert(val)
    return bst


def test_Node_setting_left():
    from bst import Node
    node1 = Node()
    node2 = Node()
    node1.left = node2
    assert node1.left == node2


def test_Node_setting_right():
    from bst import Node
    node1 = Node()
    node2 = Node()
    node1.right = node2
    assert node1.right == node2


def test_Node_parent():
    from bst import Node
    node1 = Node()
    node2 = Node()
    node1.right = node2
    assert node2.parent


def test_Node_depth():
    from bst import Node
    node1 = Node()
    node2 = Node()
    node3 = Node()
    node4 = Node()
    node1.left = node2
    node1.right = node3
    node3.right = node4
    results = [node1.depth, node2.depth, node3.depth]
    assert results == [3, 1, 2]


def test_bst_init(bst_empty):
    from bst import BST
    bst_empty
    assert isinstance(bst_empty, BST)
    assert bst_empty.depth_left == 0
    assert bst_empty.depth_right == 0


def test_bst_insert_empty(bst_empty):
    bst_empty.insert(42)
    assert bst_empty.contains(42)
    assert bst_empty.depth_left == 1
    assert bst_empty.depth_right == 1


def test_bst_insert(bst):
    bst.insert(42)
    assert bst.contains(42)
    assert bst.depth_left == 2
    assert bst.depth_right == 4


def test_bst_insert_already_there(bst):
    bst.insert(4)
    assert bst.contains(4)
    assert bst.depth_left == 2
    assert bst.depth_right == 3


def test_contains(bst):
    assert bst.contains(4)


def test_contains_empty(bst_empty):
    assert not bst_empty.contains(4)


def test_size(bst):
    assert bst.size() == len(TEST_DATA_R)


def test_size_empty(bst_empty):
    assert bst_empty.size() == 0


def test_depth(bst):
    assert bst.depth() == 3


def test_depth_empty(bst_empty):
    assert bst_empty.depth() == 0


def test_balance(bst):
    assert bst.balance() == -1


def test_balance_empty(bst_empty):
    assert bst_empty.balance() == 0


def test_in_order(bst):
    output = bst.in_order()
    lst = [next(output) for x in range(bst.size())]
    assert lst == [1, 2, 3, 4]


def test_in_order_empty(bst_empty):
    output = bst_empty.in_order()
    lst = [next(output) for x in range(bst_empty.size())]
    assert lst == []


def test_pre_order(bst):
    output = bst.pre_order()
    lst = [next(output) for x in range(bst.size())]
    assert lst == TEST_DATA_R


def test_pre_order_empty(bst_empty):
    output = bst_empty.pre_order()
    lst = [next(output) for x in range(bst_empty.size())]
    assert lst == []


def test_post_order(bst):
    output = bst.post_order()
    lst = [next(output) for x in range(bst.size())]
    assert lst == [1, 3, 4, 2]


def test_post_order_empty(bst_empty):
    output = bst_empty.post_order()
    lst = [next(output) for x in range(bst_empty.size())]
    assert lst == []


def test_breadth_first(bst):
    output = bst.breadth_first()
    lst = [next(output) for x in range(bst.size())]
    assert lst == [2, 1, 3, 4]


def test_breadth_first_empty(bst_empty):
    output = bst_empty.breadth_first()
    lst = [next(output) for x in range(bst_empty.size())]
    assert lst == []


def test_search(bst):
    assert bst._search(3).val == 3


def test_delete_leaf(bst):
    bst.delete(4)
    assert not bst.contains(4)
    assert not bst._search(4)


def test_delete_node_1_child(bst):
    bst.delete(3)
    assert not bst._search(3)
    assert not bst.contains(3)
    assert bst._search(4)


def test_delete_node_2_child(bst):
    bst.insert(2.5)
    bst.delete(3)
    assert not bst._search(3)
    assert not bst.contains(3)
    assert bst._search(2.5)
    assert bst._search(4)
    assert bst._head.right.val == 4


def test_delete_node_crazy(bst):
    bst.insert(2.5)
    bst.insert(2.25)
    bst.insert(2.75)
    bst.delete(3)
    assert not bst._search(3)
    assert not bst.contains(3)
    assert bst._head.right.val == 2.5
    assert bst._head.right.right.val == 4
    assert bst._head.right.left.val == 2.25


def test_delete_not_there(bst):
    assert not bst.delete(42)


def test_delete_one_item():
    from bst import BST
    bst = BST()
    bst.insert(42)
    bst.delete(42)
    assert not bst._search(42)
    assert not bst.contains(42)


def test_rotate_right():
    from bst import Node
    node1 = Node()
    node2 = Node()
    node2.left = node1
    node1.rotate_right()
    assert node1.right == node2
    assert not node2.left


def test_rotate_left():
    from bst import Node
    node1 = Node()
    node2 = Node()
    node2.right = node1
    node1.rotate_right()
    assert node1.right == node2
    assert not node2.left


def test_balancer_left_left(bst_l):
    bst_l.insert(0.5)
    # bst_l.balancer()
    assert bst_l._head.left.val == 1


def test_balancer_left_right(bst_l):
    bst_l.insert(1.5)
    # bst_l.balancer()
    assert bst_l._head.left.val == 1


def test_balancer_right_right(bst):
    bst.insert(5)
    # bst.balancer()
    assert bst._head.right.val == 4


def test_balancer_right_left(bst):
    bst.insert(3.5)
    # bst.balancer()
    assert bst._head.right.val == 4


def test_balancer_right_left_no_rot(bst):
    bst.insert(1.5)
    # bst.balancer()
    assert bst._head.left.val == 1
