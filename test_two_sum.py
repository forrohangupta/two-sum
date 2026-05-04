"""
Tests for Two Sum
=================
Run with:  python -m pytest test_two_sum.py -v
"""

import pytest
from two_sum import two_sum


# ── Helper ────────────────────────────────────────────────────────────────────

def valid(nums, target, result):
    """Return True if result is a valid answer for the given nums/target."""
    if len(result) != 2:
        return False
    i, j = result
    return (
        i != j
        and 0 <= i < len(nums)
        and 0 <= j < len(nums)
        and nums[i] + nums[j] == target
    )


# ── Provided examples ─────────────────────────────────────────────────────────

def test_example_1():
    assert valid([2, 7, 11, 15], 9, two_sum([2, 7, 11, 15], 9))

def test_example_2():
    assert valid([3, 2, 4], 6, two_sum([3, 2, 4], 6))

def test_example_3():
    assert valid([3, 3], 6, two_sum([3, 3], 6))


# ── Edge cases ────────────────────────────────────────────────────────────────

def test_minimum_length():
    """Smallest possible array (length 2)."""
    assert valid([1, 2], 3, two_sum([1, 2], 3))

def test_negative_numbers():
    assert valid([-3, 4, 3, 90], 0, two_sum([-3, 4, 3, 90], 0))

def test_large_negative_target():
    assert valid([-1_000_000_000, -1_000_000_000], -2_000_000_000,
                 two_sum([-1_000_000_000, -1_000_000_000], -2_000_000_000))

def test_large_positive_values():
    assert valid([999_999_999, 1, 2], 1_000_000_000,
                 two_sum([999_999_999, 1, 2], 1_000_000_000))

def test_answer_not_at_start():
    """Ensure the solution isn't hard-coded to always return early indices."""
    assert valid([1, 2, 3, 4, 5], 9, two_sum([1, 2, 3, 4, 5], 9))

def test_duplicate_values_used_once():
    """Same value appears multiple times; each element used at most once."""
    assert valid([1, 1, 1, 4], 5, two_sum([1, 1, 1, 4], 5))

def test_zero_target():
    assert valid([0, 4, 3, 0], 0, two_sum([0, 4, 3, 0], 0))

def test_larger_array():
    """Performance / correctness on a bigger array."""
    n    = 10_000
    nums = list(range(n))        # 0, 1, 2, … 9999
    target = n - 3               # 9997  → indices 9998 + 9999? No: 9998+9999=19997
    # Use last two elements that sum to target
    nums[-1] = target            # make nums[9999] = 9997
    nums[-2] = 0                 # nums[9998] = 0  →  0 + 9997 = 9997
    assert valid(nums, target, two_sum(nums, target))
