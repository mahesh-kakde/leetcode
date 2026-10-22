root1 = [1, None, [2, [3, None, None], None]]
root2 = [1, [2, None, None], [3, None, None]]
root3 = None

def sol(root):
    ans = []

    def inorder(node):
        if node is None:
            return

        inorder(node[1])
        ans.append(node[0])
        inorder(node[2])

    inorder(root)

    return ans

print(sol(root1))
print(sol(root2))
print(sol(root3))