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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Remove duplicates from a text file')
    parser.add_argument('-n', '--name', type=str, help='Name of the file')
    parser.add_argument('-e', '--extension', type=str, help='File extension')
    parser.add_argument('-a', '--about', action='store_true', help='Display help message')
    args = parser.parse_args()

    name = """
    ______                               ______             _ _           _            
    | ___ \                              |  _  \           | (_)         | |           
    | |_/ /___ _ __ ___   _____   _____  | | | |_   _ _ __ | |_  ___ __ _| |_ ___  ___ 
    |    // _ \ '_ ` _ \ / _ \ \ / / _ \ | | | | | | | '_ \| | |/ __/ _` | __/ _ \/ __|
    | |\ \  __/ | | | | | (_) \ V /  __/ | |/ /| |_| | |_) | | | (_| (_| | ||  __/\__ \
    \_| \_\___|_| |_| |_|\___/ \_/ \___| |___/  \__,_| .__/|_|_|\___\__,_|\__\___||___/
                                                    | |                               
                                                    |_|                               

    """

    if args.about:
        print(name)
        print("This script removes duplicates from a text file.")
        print("Flags:")
        print("-n: Stands for 'name' (name of the file)")
        print("-e: Stands for 'extension' (for other extensions)")
        print("-a: Stands for 'about' (display help message)")
    else:
        file_name = f"{args.name}.{args.extension}" if args.extension else f"{args.name}.txt" if args.name else None

        if file_name:
            remove_duplicates(file_name)
        else:
            print("Please provide a valid file name.")