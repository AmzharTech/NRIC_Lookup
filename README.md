# Lookup ID by Name

This is a simple Python script that allows you to look up a unique ID string by inputting a name or partial name. The script loads a CSV file containing the ID and name pairs and creates a dictionary to store them. It then prompts the user to input a name or partial name and searches the dictionary (case-insensitive) for any matching names. If a match is found, the script prints the corresponding ID and copies it to the clipboard.

## Installation

To use this script, you'll need to have Python 3 installed on your computer. You can download it from the official Python website: https://www.python.org/downloads/

You'll also need to install the `pyperclip` library. You can do this using pip, the Python package manager. Run the following command in your terminal:

```
pip install pyperclip
```

## Usage

1. Download the `ICLookup.py` script and save it to a folder on your computer.
2. Download the `id_names.csv` file and save it to the same folder as the script. Make sure that the CSV file is in the correct format (ID in the first column, name in the second column).
3. Open your terminal or command prompt and navigate to the folder where the script is saved.
5. You will need to edit the file path to fit your requirements.
4. Run the script using the following command:

```
python ICLookup.py
```

5. You'll be prompted to enter a name or partial name to search for. Type in the name or partial name and press enter.
6. If a match is found, the script will print the corresponding ID and copy it to the clipboard. If no match is found, the script will print "Name not found".
7. The script will then loop back and ask for another name. To exit the script, type in "exit" as the input.

## Contributing

If you'd like to contribute to this project, please open a pull request. Make sure your changes are well-tested and that you follow the project's coding style.

## License

Free to use for everyone.

## Contact

If you have any questions or comments, please feel free to reach out to me at amzhar@gmail.com.
