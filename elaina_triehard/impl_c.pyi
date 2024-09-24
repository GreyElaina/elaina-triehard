"""
This type stub file was generated by cyright.
"""

from typing import Iterator


class TrieHardNode:
    """
    TrieHard 的节点类。
    """
    def __init__(self, mask: int, children_indices: list[int], is_terminal: bool = False) -> None:
        ...
    


class TrieHard:
    """
    TrieHard 的主类。
    """
    def __init__(self, strings: list[str]) -> None:
        """
        初始化 TrieHard，并根据给定的字符串列表构建 Trie。
        """
        ...
    
    def get_closest_prefix(self, key: str) -> str:
        """
        获取 Trie 中与给定字符串最接近的前缀。
        """

    def __iter__(self) -> Iterator[str]:
        """
        返回 Trie 中的所有字符串。
        """
        ...