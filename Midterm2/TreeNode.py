from typing import Any


class TreeNode:
    _slots_ = 'value', 'children', 'parent'
    value: Any
    children: list['TreeNode']
    parent: 'TreeNode'

    def _init_(self, value: Any) -> None:
        self.value = value
        self.children = []
        self.parent = None

    def _str_(self) -> str:  # do not modify
        return str(self.value)

    def _repr_(self) -> str: # do not modify
        return self._getStringRep(0)

    def _getStringRep(self, depth: int) -> str:  # do not modify
        ret = self.value
        for c in self.children:
            ret += "\n" + "    " * depth + "+---" + (c._getStringRep(depth + 1))
        return ret

    def _eq_(self, other) -> bool:  # do not modify
        if type(self) != type(other):
            return False
        return self.value == other.value