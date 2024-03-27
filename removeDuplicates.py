import argparse

def remove_duplicates(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()

