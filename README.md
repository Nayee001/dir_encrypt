# 🔐 Zip File Encryption and Decryption using AES

This project provides Python scripts to compress a directory into a zip file and encrypt it using AES-256 encryption. The generated AES key must be securely stored for future decryption.

## 📋 Requirements

Make sure you have the following Python package installed:

```bash
pip install cryptography
```

## 📁 Files

- `🔐 encrypt_zip.py`: Script to zip a directory and encrypt it using AES-256 encryption.
- `🔓 decrypt_zip.py`: Script to decrypt an encrypted zip file using the AES key and IV (Initialization Vector).
- `📄 README.md`: Documentation on how to use the project.

## 🚀 How to Use

### 1️⃣ Encrypting a Zip File

1. Open the `encrypt_zip.py` script and specify the path of the directory you want to zip:

   ```python
   directory_to_zip = r"E:\path\to\your\directory"  # Replace with the actual directory path
   ```

2. Run the script to:
   - Compress the specified directory into a zip file.
   - Generate a 256-bit AES key and a random IV (Initialization Vector).
   - Encrypt the zip file using AES in CBC mode.
   
3. Once the encryption is complete, the AES key and IV will be printed in hexadecimal format. **Save these securely!** The encrypted file will be saved as `encrypted_output.bin`.

#### 📋 Example Output:

```
🔑 AES Key (keep this safe!): d9f8e12c2a3e9d0aebbff6d7c78f6a1f6c4c0e9e7f2e5e8b11b17ff72a8e5237
🔑 IV: 3dcb5671dba8bcfb07e2f5686cfa88c1
The zip file has been encrypted and saved as encrypted_output.bin
```

4. **Important**: Save the AES key and IV as they are necessary to decrypt the file.

#### 🏃‍♂️ Run the Script:

```bash
python encrypt_zip.py
```

### 2️⃣ Decrypting the Zip File

1. Open the `decrypt_zip.py` script.

2. Replace the placeholder `your_aes_key_here` with the AES key you obtained during encryption. For example:

   ```python
   aes_key = bytes.fromhex('d9f8e12c2a3e9d0aebbff6d7c78f6a1f6c4c0e9e7f2e5e8b11b17ff72a8e5237')  # Replace with your actual AES key
   ```

3. Run the script, and the decrypted zip file will be saved as `decrypted_output.zip`. You can then extract it using any zip extraction tool.

#### 🏃‍♂️ Run the Script:

```bash
python decrypt_zip.py
```

## ⚠️ Important Notes

- **🔑 AES Key Security**: The AES key is required for decryption. Store it in a secure place, as it cannot be recovered if lost.
- **🔒 IV (Initialization Vector)**: The IV is saved in the encrypted file and used for decryption.
- **🔐 Encryption Algorithm**: The scripts use AES-256 in CBC mode, a symmetric encryption algorithm. The same AES key and IV must be used for decryption.

### 🛠️ Example Workflow

1. **Encrypt a directory**:

   ```bash
   python encrypt_zip.py
   ```

2. **Decrypt the encrypted file**:

   ```bash
   python decrypt_zip.py
   ```

## ✨ Customization

- **📂 Custom Output Locations**: Modify the output paths in the scripts for the zip, encrypted, and decrypted files.
- **📁 Directory Paths**: Replace the default paths in the scripts with the locations of your own directories.

---

💻 Created by **Akshaykumar Nayee** 👨‍💻
