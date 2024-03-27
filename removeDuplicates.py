import os

def remove_duplicates():
    print("Note: Enter the full path to the folder and the file name including the .txt extension in the format 'path/to/folder/[example].txt'.")
    file_path = input("Enter the full path to the folder and the file name: ")
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()

            initial_count = len(lines)
            unique_lines = list(set(lines))

            with open(file_path, 'w') as file:
                file.writelines(unique_lines)
                
            duplicates_removed = initial_count - len(unique_lines)
            final_count = len(unique_lines)
            print(f"{duplicates_removed} duplicates were removed.")
            print(f"Initial count: {initial_count}, Final count: {final_count}")
            
        except FileNotFoundError:
            print("Error: File not found or unable to read the file.")
    else:
        print("Error: The specified file path does not exist. Please check the path and file name.")

remove_duplicates()