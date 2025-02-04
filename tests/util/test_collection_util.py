from typing import Dict, List

from fidesops.util.collection_util import append, merge_dicts, partition


def test_merge_dicts() -> None:
    """Convert an iterable of dictionaries to a dictionary of iterables"""

    assert merge_dicts(
        [{"A": 1, "B": 2}, {"A": 2, "B": 3, "C": 4}, {"A": 4, "C": 5, "D": 6}]
    ) == {"A": [1, 2, 4], "B": [2, 3], "C": [4, 5], "D": [6]}
    assert merge_dicts([{"A": 1, "B": 2}, {}]) == {"A": [1], "B": [2]}
    assert merge_dicts([]) == {}


def test_append() -> None:  # d: Dict[T, List[U]], key: T, val: U) -> None:
    """Append to values stored under a dictionary key.

    append({},"A",1) sets dict to {"A":[1]}
    append({"A":[1],"A",2) sets dict to {"A":[1,2]}
    """

    def append_result(
        key: str, value: int, d: Dict[str, List[int]] = {}
    ) -> Dict[str, List[int]]:
        append(d, key, value)
        return d

    assert append_result("A", 1) == {"A": [1]}
    assert append_result("A", 1, {"A": [1]}) == {"A": [1, 1]}
    assert append_result("A", 1, {"B": [2]}) == {"A": [1], "B": [2]}


def test_partition() -> None:
    assert partition(["Aa", "Ab", "Ac", "Dc", "Dcc", "E", "Ef"], lambda x: x[0]) == {
        "A": ["Aa", "Ab", "Ac"],
        "D": ["Dc", "Dcc"],
        "E": ["E", "Ef"],
    }
