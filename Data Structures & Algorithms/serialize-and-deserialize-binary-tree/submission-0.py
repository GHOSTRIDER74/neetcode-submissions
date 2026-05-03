# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        arr = []
        def sehelper(root):
            if not root:
                arr.append("N")
                return None 
            arr.append(str(root.val))
            sehelper(root.left)
            sehelper(root.right)
        sehelper(root)
        return ",".join(arr)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(",")
        it = iter(vals)

        def dehelper():
            val = next(it)
            if val == "N":
                return None
            node = TreeNode(int(val))
            node.left = dehelper()
            node.right = dehelper()
            return node
        return dehelper()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))