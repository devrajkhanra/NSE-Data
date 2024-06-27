from datetime import datetime


def convert_date(input_date):
    try:
        # Parse the input date assuming it's in ddmmyyyy format
        parsed_date = datetime.strptime(input_date, '%d%m%Y')
        # Format the parsed date into dd-MMM-yyyy format
        formatted_date = parsed_date.strftime('%d-%b-%Y')
        return formatted_date
    except ValueError:
        # Handle incorrect input format
        return "Invalid date format"


def convert_to_ddmmyy(input_date):
    try:
        # Parse the input date assuming it's in ddmmyyyy format
        parsed_date = datetime.strptime(input_date, '%d%m%Y')
        # Format the parsed date into ddmmyy format
        formatted_date = parsed_date.strftime('%d%m%y')
        return formatted_date
    except ValueError:
        # Handle incorrect input format
        return "Invalid date format"
