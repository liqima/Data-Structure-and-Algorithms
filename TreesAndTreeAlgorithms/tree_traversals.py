import nodes_and_references

def preorder(tree):
	if tree:
		print(tree.get_root_val())
		preorder(tree.get_left_child())
		preorder(tree.get_right_child())

def inorder(tree):
	if tree:
		inorder(tree.get_left_child())
		print(tree.get_root_val())
		inorder(tree.get_right_child())

def postorder(tree):
	if tree:
		postorder(tree.get_left_child())
		postorder(tree.get_right_child())
		print(tree.get_root_val())
