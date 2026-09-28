root1 = [1,2,3,4,None,2,4,None,None,4]
root2 = [2,1,1]
root3 = [2,2,2,3,None,3,None]

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(arr):
    if not arr:
        return None

    nodes = []

    for value in arr:
        if value is None:
            nodes.append(None)
        else:
            nodes.append(TreeNode(value))

    j = 1

    for node in nodes:
        if node is not None:
            if j < len(nodes):
                node.left = nodes[j]
                j += 1

            if j < len(nodes):
                node.right = nodes[j]
                j += 1

    return nodes[0]

def sol(root):
    count = {}
    ans = []

    def dfs(node):
        if node is None:
            return "#"

        left = dfs(node.left)
        right = dfs(node.right)

        key = str(node.val) + "," + left + "," + right

        if key not in count:
            count[key] = 0
        count[key] += 1

        if count[key] == 2:
            ans.append(node)

        return key

    dfs(root)

    return ans

root1 = build_tree(root1)
root2 = build_tree(root2)
root3 = build_tree(root3)

print([node.val for node in sol(root1)])
print([node.val for node in sol(root2)])
print([node.val for node in sol(root3)])