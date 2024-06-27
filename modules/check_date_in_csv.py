import pandas as pd


# Function to read the CSV from URL and check the Date1 column
def check_date_in_csv(url,column_name, date_input):
    try:
        # Format the date_input based on the column_name
        if column_name == 'Index Date':
            # Convert ddmmyyyy to dd-mm-yyyy
            formatted_date = f"{date_input[:2]}-{date_input[2:4]}-{date_input[4:]}"
        else:
            # Keep date_input as it is
            formatted_date = date_input

        # Read CSV from URL
        df = pd.read_csv(url)
        print(df.head())

        # Check if the column_name contains the user-provided date
        if column_name in df.columns:
            if formatted_date in df[column_name].values:
                print(f"The date {formatted_date} is present in the {column_name} column.")
                return True
            else:
                print(f"The date {formatted_date} is NOT present in the {column_name} column.")
                return False
        else:
            print(f"The CSV does not contain a '{column_name}' column.")
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
