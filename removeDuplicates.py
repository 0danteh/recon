import argparse

def remove_duplicates(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()

    unique_lines = list(set(lines))
    duplicates_count = len(lines) - len(unique_lines)
    with open(file_name, 'w') as file:
        file.writelines(unique_lines)
    print(f"{duplicates_count} duplicates were deleted.")
    print(f"Number of items at the beginning: {len(lines)}, Number of items at the end: {len(unique_lines)}")

