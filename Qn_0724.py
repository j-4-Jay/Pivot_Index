'''
Steps Planning:
1) make a full sum of the list so as to compare the L_Sum & R_Sum
2) initiate L_Sum to zero & R_Sum to the total sum
3) make R_Sum = total_sum - current_value
4)then check if L_Sum == R_sum, return i
5) L_Sum += current_value
'''


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

def press_enter_to_continue():
    while True:
        user_input = input("Are you Ready to find the Pivot Index of the Given List?(Press Enter to Proceed)")
        if user_input == "":
            break
        else:
            print("Invalid input. Please press Enter without typing anything.")


nums = []
obtain_list = Input_List()
nums.extend(obtain_list)
press_enter_to_continue()

Pivot_Index = -1 # Initialize the value to -1 as if there is no Pivot Index
Total_Sum = sum(nums)
R_Sum = Total_Sum
L_Sum = 0

for i in range(len(nums)):
    Current_Value = nums[i]
    R_Sum -= Current_Value       
    if L_Sum == R_Sum:
        Pivot_Index = i        
    L_Sum += Current_Value
    
print(f'The PIVOT INDEX of the given List is: {Pivot_Index}')