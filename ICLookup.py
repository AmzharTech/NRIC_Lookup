import csv
import os

# Get the path to the desktop folder
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# Get the path to the PI2201J folder on the desktop
pi2201j_path = os.path.join(desktop_path, "PI2201J")

# Get the path to the CSV file within the PI2201J folder
csv_path = os.path.join(pi2201j_path, "id_names.csv")

# Check if the CSV file exists in the folder
if not os.path.exists(csv_path):
    print('CSV file not found in folder')
else:
    # Load the CSV file containing the ID and name pairs
    with open(csv_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        # Create a dictionary to store the ID and name pairs
        id_name_dict = {row[1].lower(): row[0] for row in reader}

    # Loop until user types "exit"
    while True:
        # Ask the user to input a name or partial name
        name = input('Enter a name or partial name to search for (type "exit" to stop): ').lower()

        # Check if the user wants to exit
        if name == "exit":
            break

        # Search for the name in the dictionary (case-insensitive) and print the corresponding ID
        matching_names = [n for n in id_name_dict.keys() if name in n]
        if matching_names:
            for n in matching_names:
                print('ID for', n.title(), 'is', id_name_dict[n])
        else:
            print('Name not found')
