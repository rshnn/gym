




def invert_tree(root): 

	if not root: 
		return 


	tmp = root.left 
	root.left = root.right 
	root.right = tmp 

	invert_tree(root.left)
	invert_tree(root.right) 



