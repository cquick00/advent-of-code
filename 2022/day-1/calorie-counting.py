# =========
# LIBRARIES
# =========

import os
import sys


# =========
# FUNCTIONS
# =========

# Function to read input.txt file and convert the breakdowns per elf into totals
def get_calorie_inputs_func():
    # Local Variables
    calorie_inputs = []
    calorie_sums_per_elf = 0

    # Local Main Code
    calorie_input_file = open(os.path.join(sys.path[0], "input.txt"), "r")
    for calories in calorie_input_file:
        if calories == "\n":
            calorie_inputs.append(calorie_sums_per_elf)
            calorie_sums_per_elf = 0
        else:
            calorie_sums_per_elf += int(calories)
    calorie_input_file.close()
    return calorie_inputs


# ================
# GLOBAL VARIABLES
# ================

calorie_array = []
calorie_array_sums = []

# ====
# MAIN
# ====

if __name__ == "__main__":
    calorie_array = get_calorie_inputs_func()
    print("Part 1:")
    print(max(calorie_array))

    print("\nPart 2:")
    print(calorie_array[0] + calorie_array[1] + calorie_array[2])
