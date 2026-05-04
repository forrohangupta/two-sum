"""
Problem A: Two Sum
==================
Given an array `nums` and an integer `target`, return indices of two numbers
such that they add up to `target`.

Constraints:
    - 2 <= nums.length <= 10^4
    - -10^9 <= nums[i] <= 10^9
    - -10^9 <= target <= 10^9
    - Exactly one valid answer exists.

Approach: Hash Map (One-Pass)
    - Time Complexity  : O(n)
    - Space Complexity : O(n)

For each number, compute its complement (target - num).
If the complement already exists in the hash map, we found our pair.
Otherwise, store the current number and its index.
"""

import sys
input = sys.stdin.readline          # Fast I/O


def two_sum(nums: list[int], target: int) -> list[int]:
    seen: dict[int, int] = {}       # value -> index

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

    return []                        # Guaranteed not reached (exactly one answer)


def main() -> None:
    # ── Read input ──────────────────────────────────────────────────────────
    # Line 1: space-separated integers (nums)
    # Line 2: single integer (target)
    nums   = list(map(int, input().split()))
    target = int(input())

    result = two_sum(nums, target)

    # ── Write output ─────────────────────────────────────────────────────────
    print(*result)


if __name__ == "__main__":
    main()
