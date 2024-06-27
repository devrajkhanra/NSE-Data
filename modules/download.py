# Function to download CSV from URL
import os

import requests


def download_csv(url, filename, folder_path):
    try:
        # Send GET request to URL
        response = requests.get(url)

        # Check if request was successful
        if response.status_code == 200:
            # Determine full path to save the file
            full_path = os.path.join(folder_path, filename)

            # Save CSV content to file
            with open(full_path, 'wb') as f:
                f.write(response.content)

            print(f"CSV file downloaded successfully as '{filename}' in '{folder_path}'")
            return True, full_path
        else:
            print(f"Failed to download CSV. Status code: {response.status_code}")
            return False, None
    except Exception as e:
        print(f"An error occurred: {e}")
        return False, None