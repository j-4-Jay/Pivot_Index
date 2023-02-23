# Pivot_Index
## Dynamic Pivot Index Finder
- [x] Inspired by the Qn. No. 724 in LeetCode



#### Steps Planning:

i. Get the numbers from User from a user defined function and return the list

ii. Define another function to get a pause in the program

iii. Calculate the Pivot Index:

        1. make a full sum of the list so as to compare the L_Sum & R_Sum
        2. initiate L_Sum to zero & R_Sum to the total_sum
        3. make R_Sum -= current_value
        4. check if L_Sum == R_sum, return i
        5. L_Sum += current_value
