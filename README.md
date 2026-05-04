# Problem A — Two Sum

## Problem Statement

Given an array `nums` and an integer `target`, return **indices** of the two numbers such that they add up to `target`.

- Exactly one solution exists.  
- You may not use the same element twice.  
- Return the indices in any order.

### Constraints

| Parameter | Range |
|-----------|-------|
| `nums.length` | `2 ≤ n ≤ 10⁴` |
| `nums[i]` | `-10⁹ ≤ nums[i] ≤ 10⁹` |
| `target` | `-10⁹ ≤ target ≤ 10⁹` |

---

## Approach — One-Pass Hash Map

| | Complexity |
|---|---|
| **Time** | O(n) |
| **Space** | O(n) |

Walk through the array once. For each element, calculate its **complement** (`target - num`). If the complement already exists in the hash map, the pair is found and returned immediately. Otherwise, insert the current element into the map.

This avoids the O(n²) brute-force double-loop entirely.

```
nums = [2, 7, 11, 15],  target = 9

i=0  num=2   complement=7   → not in map  | map: {2:0}
i=1  num=7   complement=2   → FOUND at 0  | return [0, 1]  ✓
```

---

## Examples

```
Input : nums = [2,7,11,15]  target = 9
Output: [0, 1]   # nums[0] + nums[1] = 2 + 7 = 9

Input : nums = [3,2,4]      target = 6
Output: [1, 2]   # nums[1] + nums[2] = 2 + 4 = 6

Input : nums = [3,3]        target = 6
Output: [0, 1]   # nums[0] + nums[1] = 3 + 3 = 6
```

---

## File Structure

```
.
├── two_sum.py        # Solution + fast I/O entry point
├── test_two_sum.py   # pytest test suite (11 test cases)
└── README.md
```

---

## Running

### Solution (stdin / stdout)
```bash
# Format:
# Line 1: space-separated integers (nums)
# Line 2: target integer

echo "2 7 11 15
9" | python two_sum.py
# Output: 0 1
```

### Tests
```bash
pip install pytest
pytest test_two_sum.py -v
```

---

## Why Not Brute Force?

The naïve O(n²) approach checks every pair — unacceptable for `n = 10⁴` in competitive programming. The hash-map solution does the same work in a single linear pass.
