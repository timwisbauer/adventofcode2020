# Advent of Code Day 1: Report Repair
# Find the two entries that sum to 2020 and multiply them together.

def find_match(expenses):
    
    # Sort the elements in the list first.
    expenses.sort(reverse=True)
    
    for a_index, a in enumerate(expenses):
        # Starting with a_index + 1, loop through rest of list.
        # Check to see if a + b < 2020.  If so, start with b_index+1
        # and check for acceptance.
        print(f"A: {a}")
        for b_index in range(a_index + 1, len(expenses)):
            b = expenses[b_index]
            print(f"A:{a}, B: {b}")
            if a + b < 2020:
                for c_index in range(b_index + 1, len(expenses)):
                    c = expenses[c_index]
                    print(f"A: {a}, B: {b}, C: {c}")
                    if a + b + c == 2020:
                        return a * b * c

if __name__ == "__main__":
    
    with open("input.txt", 'r') as file:
        contents = file.read().splitlines()
        # Convert to ints.
        expenses = [int(i) for i in contents]
    
    answer = find_match(expenses)
    
    print(f"Answer: {answer}")

