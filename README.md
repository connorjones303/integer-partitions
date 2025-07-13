# Bounded Part Distribution Calculator

This script computes and analyzes bounded part distributions for a range of integers. Specifically, it generates all partitions of integers, where the size of each part is bounded by a specified maximum value. The program then counts how many partitions contain 1's, 2's, and 3's, and summarizes this distribution for each integer within a given range.

## Features

- **Partition Calculation**: Generates all partitions of an integer `k` where each part size is bounded by `max_part`.
- **Range-based Analysis**: Computes the distribution of partitions for all integers within a specified range (from `start_k` to `end_k`).
- **Customizable Parameters**: The maximum part size and the integer range can be customized for your analysis.

## Requirements

- Python 3.x
- `sympy` library

To install the necessary libraries, you can use pip:

```bash
pip install sympy
```
