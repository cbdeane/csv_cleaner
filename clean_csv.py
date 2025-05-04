import pandas as pd
import argparse


def clean_csv(input_file, output_file, columns_to_keep):
    """
    Cleans a CSV file by selecting only specified columns and saves the result.

    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to the output CSV file.
        columns_to_keep (list): List of column names to keep.
    """
    try:
        df = pd.read_csv(input_file)

        # Check if all specified columns exist in the DataFrame
        missing_columns = [col for col in columns_to_keep if col not in df.columns]
        if missing_columns:
            print(f"Warning: Columns {missing_columns} not found in the CSV. Proceeding without them.")
            columns_to_keep = [col for col in columns_to_keep if col in df.columns]

        df_filtered = df[columns_to_keep]
        df_filtered.to_csv(output_file, index=False)
        print(f"CSV data cleaned and saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description="Clean CSV data by selecting specified columns.")
    parser.add_argument("input_file", help="Path to the input CSV file.")
    parser.add_argument("output_file", help="Path to the output CSV file.")
    parser.add_argument("columns", nargs="+", help="List of column names to keep (space-separated).")

    args = parser.parse_args()

    clean_csv(args.input_file, args.output_file, args.columns)

if __name__ == "__main__":
    main()
