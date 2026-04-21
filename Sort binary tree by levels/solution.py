from collections import deque

def tree_by_levels(node):
    if not node:
        return []
    vertex_list = deque([node])
    result = []

    while vertex_list:
        current = vertex_list.popleft()
        result.append(current.value)   # або cur.data
        if current.left:
            vertex_list.append(current.left)
        if current.right:
            vertex_list.append(current.right)

    return result
