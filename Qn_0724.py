
# A Function to get the Integers for the Main List i.e. nums
def Input_List():
    list = []
    while True:
        user_input = input('Please enter the numbers for the list or "Done" to finish the list: ')
        if user_input == "done":
            break
        else:
            try:
                number = int(user_input)
                list.append(number)
            except ValueError:
                print(f'Invalid Input. Please enter an integer or "Done"')
    print(f'The Final List is: {list}')

    return list

# A Function to pause the program and get the user permisson to proceed
def press_enter_to_continue():
    while True:
        user_input = input("Are you Ready to find the Pivot Index of the Given List?(Press Enter to Proceed)")
        if user_input == "":
            break
        else:
            print("Invalid input. Please press Enter without typing anything.")

# Program to find the Pivot Index
nums = []
obtain_list = Input_List() # Get the return value of the predefined Function
nums.extend(obtain_list)  # Get the values to the nums variable
press_enter_to_continue() # Pause for the process

Pivot_Index = -1 # Initialize the value to -1 as if there is no Pivot Index

Total_Sum = sum(nums) # Plan 1
R_Sum = Total_Sum # Plan 1
L_Sum = 0 # Plan 1

for i in range(len(nums)): # Plan 2
    Current_Value = nums[i] # Plan 2
    R_Sum -= Current_Value # Plan 2

    if L_Sum == R_Sum: # Plan 3
        Pivot_Index = i # Plan 3

    L_Sum += Current_Value # Plan 4
    
print(f'The PIVOT INDEX of the given List is: {Pivot_Index}')

# ! this is a test comment
# ? what is this???