import requests
import zipfile
import os

# URL of the Vimeo Septuplet dataset
url = "http://data.csail.mit.edu/tofu/dataset/vimeo_septuplet.zip"

# Specify a directory to save the downloaded file
download_dir = "/misc/dl001/dataset"  # ダウンロードするための一時的なディレクトリ
temp_dataset_dir = "temp_vimeo_septuplet"  # 一時的なサブディレクトリ
os.makedirs(os.path.join(download_dir, temp_dataset_dir), exist_ok=True)
zip_file_path = os.path.join(download_dir, temp_dataset_dir, "vimeo_septuplet.zip")

# Download the file
response = requests.get(url, stream=True)

# Check if the request was successful
if response.status_code == 200:
    with open(zip_file_path, 'wb') as f:
        f.write(response.content)
    message = "Download successful."
    
    # ZIPファイルを解凍
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(os.path.join(download_dir, "dataset"))  # 解凍先のパスを指定
    message += " Extraction successful."
else:
    message = f"Failed to download. Status code: {response.status_code}"

message, zip_file_path
