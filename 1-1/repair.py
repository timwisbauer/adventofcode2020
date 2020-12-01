# Advent of Code Day 1: Report Repair
# Find the two entries that sum to 2020 and multiply them together.

def find_match(expenses):
    for a in expenses:
        b = 2020 - a
        
        if b in expenses:
            return a * b

if __name__ == "__main__":
    
    with open("input.txt", 'r') as file:
        contents = file.read().splitlines()
        # Convert to ints.
        expenses = [int(i) for i in contents]
    
    answer = find_match(expenses)
    
    print(f"Answer: {answer}")

