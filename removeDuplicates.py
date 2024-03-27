def remove_duplicates():
    print("Note: Remember to keep the .txt extension when entering the input file name.")
    file_name = input("Enter the name of the .txt file: ")
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()