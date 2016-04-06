import pytest

TEST_DATA = [1, 2, 3, 4]


@pytest.fixture()
def bst_empty():
    from bst import BST
    return BST()


@pytest.fixture()
def bst():
    from bst import BST
    bst = BST()
    for val in TEST_DATA:
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


def test_bst_init(bst_empty):
    from bst import BST
    # bst = BST()
    bst_empty
    assert isinstance(bst_empty, BST)


def test_bst_insert_empty(bst_empty):
    bst_empty.insert(42)
    assert bst_empty.contains(42)


def test_bst_insert(bst):
    bst.insert(42)
    assert bst.contains(42)


def test_bst_insert_already_there(bst):
    bst.insert(4)
    pass
