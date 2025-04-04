Run from the command line:
Bash

    python clean_csv.py input.csv output.csv column1 column2 column3

        Replace input.csv with the path to your input CSV file.
        Replace output.csv with the desired path for the cleaned output CSV file.
        Replace column1, column2, column3, etc., with the names of the columns you want to keep.

Example:

If you have a CSV file named data.csv with columns Name, Age, City, and Country, and you want to keep only the Name and City columns, you would run:
Bash

python clean_csv.py data.csv cleaned_data.csv Name City

This will create a new CSV file named cleaned_data.csv containing only the Name and City columns.

Key improvements and explanations:

    Error Handling: The code now includes try...except blocks to handle potential errors like FileNotFoundError and other exceptions, providing more robust error messages.
    Column Existence Check: It checks if the specified columns actually exist in the input CSV. If a column is missing, it prints a warning and proceeds without that column.
    argparse for Command-Line Arguments: The code utilizes argparse to handle command-line arguments, making it more user-friendly and flexible. Users can easily specify input and output files and columns directly from the command line.
    Clearer Function and Variable Names: The code uses more descriptive names for functions and variables, improving readability and maintainability.
    Pandas for CSV Handling: Uses pandas, which is the industry standard for data manipulation in python. This makes the code more efficient and robust.
    index=False in to_csv(): This prevents pandas from writing the DataFrame index to the output CSV file.
    Informative Output: The program now prints messages to the console indicating the success or failure of the cleaning process.
