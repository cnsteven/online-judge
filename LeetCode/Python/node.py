from typing import Optional


class ListNode:
    def __init__(self, val: any = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next


class TreeNode:
    def __init__(
        self,
        val: any = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right
