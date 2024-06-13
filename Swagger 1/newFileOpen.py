import os
import glob
import datetime
import subprocess
import re

def openNewFile():
    # Specify the directory where your downloads are saved
    download_dir = r'c:/Users/HDouglas/Downloads'  # Replace with your actual download directory

# Get a list of all files in the download directory
    downloaded_files = glob.glob(os.path.join(download_dir, '*'))

# Filter to get only files (excluding directories)
    downloaded_files = [f for f in downloaded_files if os.path.isfile(f)]

# Sort files by modification time (most recent first)
    downloaded_files.sort(key=os.path.getmtime, reverse=True)

# Pick the most recent file
    if downloaded_files:
        newest_file = downloaded_files[0]
        print("Newest downloaded file:", newest_file)

    # Now you can open and work with the file
        with open(newest_file, 'r', encoding='utf-8') as file:
            file_content = file.read()
            print("File content:")
            print(file_content)
        

            pattern = r'"accessToken":\s*"([^"]+)"'

            match = re.search(pattern, file_content)
            if match:
                access_token = match.group(1)
                print("Access token found:", access_token)
                return access_token
            else:
                print("Access token not found in the output")

    else:
        print("No files found in the download directory")

