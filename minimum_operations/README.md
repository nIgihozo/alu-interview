# Minimum Operations

## Project Overview
This project is part of the **alu-interview** repository.  
It implements an algorithm to calculate the minimum number of operations required to generate exactly `n` characters `H` in a text file, given only two possible operations:
- **Copy All**
- **Paste**

The problem is solved by factorizing `n` and summing its prime factors, which represents the optimal sequence of copy/paste operations.

---

## Requirements
- You must have python3 installed on your ubuntu in order to be able 
this files.

---

## Files
- `0-minoperations.py` → contains the `minOperations(n)` function
- `0-main.py` → sample test file

---

## Function Prototype
```python
def minOperations(n)

