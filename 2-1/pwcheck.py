# Advent of Code: Day 2
# Find valid passwords based on how many of a particular letter the candidate password contains.

import re

def check_passwords(passwords):
    # Iterate through list of passwords.
    # Use regex to pull out letter and counts.
    # Letter and counts then used for string evaluation.

    valid_pw_count = 0

    for line in passwords:
        parsed_password = re.search(r"^(\d*)-(\d*) (\w*): (\w*)", line)
        lower, upper, letter, password = parsed_password.groups()
        
        count = password.count(letter)
        if(count >= int(lower) and count <= int(upper)):
            valid_pw_count += 1
    return valid_pw_count

if __name__ == "__main__":

    with open("input.txt", "r") as file:
        passwords = file.read().splitlines()

    count = check_passwords(passwords)
    print(f"Answer: {count}")

