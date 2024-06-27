import os

from modules.check_date_in_csv import check_date_in_csv
from modules.convert_date import convert_to_ddmmyy
from modules.create_data_folder import create_data_folder
from modules.download import download_csv
from modules.generate_url import generate_url
from modules.user_input import user_input

if __name__ == "__main__":
    create_data_folder()
    # user_date = user_input()
    # List of dates
    list_of_dates = [
        "01062024", "02062024", "03062024", "04062024", "05062024",
        "06062024", "07062024", "08062024", "09062024", "10062024",
        "11062024", "12062024", "13062024", "14062024", "15062024",
        "16062024", "17062024", "18062024", "19062024", "20062024",
        "21062024", "22062024", "23062024", "24062024", "25062024",
        "26062024", "27062024", "28062024", "29062024", "30062024"
    ]  # Replace with your actual list of dates

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
