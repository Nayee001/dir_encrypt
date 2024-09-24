import os
import zipfile
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import secrets

# Function to create a zip file from a directory
def zip_directory(directory_path, output_zip):
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, directory_path))

# Function to encrypt file data using AES encryption
def encrypt_file(input_file, key):
    # Generate a random 16-byte IV
    iv = secrets.token_bytes(16)

    # Create AES cipher object with CBC mode
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Read the content of the file
    with open(input_file, 'rb') as f:
        file_data = f.read()

    # Pad the data to be AES block size (16 bytes)
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(file_data) + padder.finalize()

    # Encrypt the padded data
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    # Return the IV and encrypted data
    return iv, encrypted_data

if __name__ == "__main__":
    # Step 1: Zip the directory
    directory_to_zip = r"E:\Akshay\projects\vFCL IOT DHSE\encryption-decryption-python-code"  # Replace with your directory path
    output_zip_file = 'output.zip'
    zip_directory(directory_to_zip, output_zip_file)

    # Step 2: Generate a random AES key
    aes_key = secrets.token_bytes(32)  # AES-256 key

    # Step 3: Encrypt the zip file
    iv, encrypted_zip_data = encrypt_file(output_zip_file, aes_key)

    # Step 4: Store or print the AES key and the IV (Initialization Vector)
    print(f"AES Key (keep this safe!): {aes_key.hex()}")
    print(f"IV: {iv.hex()}")

    # Optionally, save the encrypted data to a file
    with open('encrypted_output.bin', 'wb') as encrypted_file:
        encrypted_file.write(iv + encrypted_zip_data)  # Save IV and encrypted data together

    print(f"The zip file {output_zip_file} has been encrypted and saved as encrypted_output.bin")
