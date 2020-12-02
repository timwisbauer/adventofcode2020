# Advent of Code: Day 2
# Find valid passwords based on checking string positions for a certain letter.

import re

def check_passwords(passwords):
    # Iterate through list of passwords.
    # Use regex to pull out letter and counts.
    # Letter and counts then used for string evaluation.

    valid_pw_count = 0

    for line in passwords:
        parsed_password = re.search(r"^(\d*)-(\d*) (\w*): (\w*)", line)
        lower, upper, letter, password = parsed_password.groups()
        
        if (letter in password[int(lower)-1]) is not (letter in password[int(upper)-1]):
            valid_pw_count += 1
    return valid_pw_count

if __name__ == "__main__":

    with open("input.txt", "r") as file:
        passwords = file.read().splitlines()

    count = check_passwords(passwords)
    print(f"Answer: {count}")

