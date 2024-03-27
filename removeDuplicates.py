def remove_duplicates():
    print("Note: Remember to keep the .txt extension when entering the input file name.")
    file_name = input("Enter the name of the .txt file: ")
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            
        initial_count = len(lines)
        unique_lines = list(set(lines))
        
        with open(file_name, 'w') as file:
            file.writelines(unique_lines)
            
        duplicates_removed = initial_count - len(unique_lines)
