import csv
from collections import Counter

def count_unique_entries(file_path, column_index):
    # Read the CSV file
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header if there is one
        entries = [row[column_index] for row in reader]  # Extract entries from the specified column
    
    # Count occurrences of each unique entry
    entry_counts = Counter(entries)
    
    # Print the results
    for entry, count in entry_counts.items():
        print(f'{entry}: {count}')

# Usage example:
file_path = './combo.csv'  # Replace with the path to your CSV file
column_index = 1  # Replace with the index of the column you want to count unique entries from
count_unique_entries(file_path, column_index)

