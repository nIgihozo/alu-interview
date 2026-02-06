## Rainwater Retention

### Description
This project contains a Python function rain(walls) that calculates how many square units of water will be retained after it rains,
given a list of non-negative integers representing the heights of walls.

**The calculation assumes that:**

- Each wall has a unit width of 1.
- The ends of the list are not walls and cannot retain water.
- If the list is empty, the function returns 0

### Logic & Complexity
The solution utilizes a **Two-Pointer** approach to achieve optimal efficiency:

- Time Complexity: $O(n)$ — The list is traversed only once.
- Space Complexity: $O(1)$ — No additional data structures are created; only pointers and counters are used.

### Usage
To test the function, you can run the provided main script:

Bash
# Make the main file executable
chmod +x 0_main.py

# Run the test
./0_main.py

**Example Input/Output**

Python
walls = [0, 1, 0, 2, 0, 3, 0, 4]
# Output: 6

walls = [2, 0, 0, 4, 0, 0, 1, 0]
# Output: 6

### Files
| File | Description |
| :--- | :--- |
| **0-rain.py** | Implementation of the `rain(walls)` function. |
| **0_main.py** | Main script for testing the implementation. |
