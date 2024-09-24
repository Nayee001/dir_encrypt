from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

# Function to decrypt the encrypted data
def decrypt_file(encrypted_file, key):
    # Read the encrypted file (which contains both the IV and the encrypted data)
    with open(encrypted_file, 'rb') as f:
        iv = f.read(16)  # First 16 bytes are the IV
        encrypted_data = f.read()  # The rest is the encrypted data

    # Create AES cipher object with CBC mode using the key and IV
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    # Decrypt the data
    decrypted_padded_data = decryptor.update(encrypted_data) + decryptor.finalize()

    # Remove padding from the decrypted data
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    decrypted_data = unpadder.update(decrypted_padded_data) + unpadder.finalize()

    return decrypted_data

if __name__ == "__main__":
    encrypted_file_path = 'encrypted_output.bin'  # Path to the encrypted file
    output_decrypted_file = 'decrypted_output.zip'  # Path to save the decrypted zip file

    # AES key and IV used for encryption (you must securely store and retrieve them)
    aes_key = bytes.fromhex('087355b9a25229f61aa019ec876f01825bb1bf05496fb68163e152b81dbb1760')  # Replace with your hex AES key from encryption step

    # Step 1: Decrypt the file
    decrypted_zip_data = decrypt_file(encrypted_file_path, aes_key)

    # Step 2: Save the decrypted zip data back to a file
    with open(output_decrypted_file, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_zip_data)

    print(f"The file has been decrypted and saved as {output_decrypted_file}")
