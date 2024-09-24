import os
import zipfile

def zip_directory(directory_path, output_zip):
    # Create a ZipFile object
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Walk through the directory
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                # Create the complete file path
                file_path = os.path.join(root, file)
                # Add file to the zip file, preserving the directory structure
                zipf.write(file_path, os.path.relpath(file_path, directory_path))

if __name__ == "__main__":
    directory_to_zip = r"E:\Akshay\projects\vFCL IOT DHSE\encryption-decryption-python-code"  # Use raw string to handle backslashes
    output_zip_file = 'output.zip'  # Replace with the desired zip file name
    zip_directory(directory_to_zip, output_zip_file)
    print(f'{directory_to_zip} has been zipped into {output_zip_file}')
