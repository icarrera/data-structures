import pytest


@pytest.fixture()
def test_bst_empty():
    from bst import BST
    return BST()


@pytest.fixture()
def test_bst():
    from bst import BST
    test_bst = BST()
    test_bst.insert(2)
    test_bst.insert(1)
    test_bst.insert(3)
    test_bst.insert(4)


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
    assert node2.has_parent  # is true


def test_bst_init():
    from bst import BST
    bst = BST()
    assert isinstance(bst, BST)


def test_bst_insert_empty(test_bst_empty):
    test_bst_empty.insert(42)
    assert test_bst_empty.contains(42)


def test_bst_insert():
    pass


def test_bst_insert_already_there():
    pass


def