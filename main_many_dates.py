import os
import sys

from check_character import get_user_input, is_letter
from modules.check_date_in_csv import check_date_in_csv
from modules.convert_date import convert_to_ddmmyy
from modules.create_data_folder import create_data_folder
from modules.download import download_csv
from modules.generate_url import generate_url
from modules.user_input import user_input
from modules.pdates import pdate

if __name__ == "__main__":
    create_data_folder()
    user_start_year = user_input("Enter start year as yyyy: ")
    user_start_month = user_input("Enter start month as m: ")
    user_start_date = user_input("Enter start date as d: ")
    user_end_year = user_input("Enter end year as yyyy: ")
    user_end_month = user_input("Enter end month as m: ")
    user_end_date = user_input("Enter end date as d: ")
    # List of dates

    print("The start and end dates are: ")
    print(f('{user_start_year}, {user_start_month} ,{user_start_date} till {user_end_year}, {user_end_month} ,{user_end_date}'))

    
    try:
        user_choice = get_user_input()

        if user_choice == 'Y':
            char = input("Enter a single character to check: ").strip()
            if is_letter(char):
                print(f"The character '{char}' is a letter.")

                # pdate(start_year, start_month, start_day, end_year, end_month, end_day)
            list_of_dates = pdate(user_start_year, user_start_month, user_start_date, user_end_year, user_end_month, user_end_date)

            for user_date in list_of_dates:
                user_date_to_ma = convert_to_ddmmyy(user_date)

                final_url_index = generate_url(user_date,
                                            "https://archives.nseindia.com/content/indices/ind_close_all_date.csv")
                print(f"The generated URL is: {final_url_index}")

                # Check the date in the CSV
                if check_date_in_csv(final_url_index, 'Index Date', user_date):

                    # If date check passes, download the CSV
                    index_csv_filename = f"ind_close_all_{user_date}.csv"

                    # Define path to the desktop's data folder
                    index_desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'data', 'indice')
                    # stock_desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'data', 'stock')

                    # Download the CSV file to the data folder
                    success, saved_path = download_csv(final_url_index, index_csv_filename, index_desktop_path)

                    if success:
                        print(f"CSV file download and date check completed successfully. Saved at '{saved_path}'")
                    else:
                        print("CSV file download failed.")

                    # STOCK
                    final_url_stock = generate_url(user_date,
                                                "https://archives.nseindia.com/products/content/sec_bhavdata_full_date.csv")
                    print(f"The generated URL is: {final_url_stock}")
                    stock_csv_filename = f"sec_bhavdata_full_{user_date}.csv"
                    stock_desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'data', 'stock')
                    # Download the CSV file to the data folder
                    success, saved_path = download_csv(final_url_stock, stock_csv_filename, stock_desktop_path)
                    if success:
                        print(f"CSV file download and date check completed successfully. Saved at '{saved_path}'")
                    else:
                        print("CSV file download failed.")

                    # MA
                    final_url_ma = generate_url(user_date_to_ma,
                                                "https://archives.nseindia.com/archives/equities/mkt/MAdate.csv")
                    print(f"The generated URL is: {final_url_ma}")
                    ma_csv_filename = f"ma{user_date}.csv"
                    ma_desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'data', 'ma')
                    # Download the CSV file to the data folder
                    success, saved_path = download_csv(final_url_ma, ma_csv_filename, ma_desktop_path)
                    if success:
                        print(f"CSV file download and date check completed successfully. Saved at '{saved_path}'")
                    else:
                        print("CSV file download failed.")


                else:
                    print("Date check failed. CSV file not downloaded.")

            else:
                print(f"The character '{char}' is not a letter.")
        elif user_choice == 'N':
            print("Exiting the program.")
            sys.exit(0)

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    
    else:
        sys.exit()