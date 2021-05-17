class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def generator(nums:list):
    head = TreeNode(nums[0])
    p = head
    queue = []
    queue.insert(0,p)
    nums.remove(p.val)
    while nums != []:
        p = queue.pop()
        p.left = TreeNode(nums[0])
        queue.insert(0,p.left)
        nums.remove(p.left.val)
        if nums != []:
            p.right = TreeNode(nums[0])
            queue.insert(0,p.right)
            nums.remove(p.right.val)
    return head
