import hashlib

def calculate_hash(file_path):
    """Calculate the hash of a file using SHA-256."""
    hash_function = hashlib.sha256()  
    try:
        with open(file_path, 'rb') as file:
            while chunk := file.read(4096):  
                hash_function.update(chunk)
        return hash_function.hexdigest()
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}.")
        return None

def compare_hashes(original_hash, current_hash):
    """Compare two hashes to check if the file is unchanged."""
    return original_hash == current_hash

def main():
    print("File Integrity Checker")
    print("=======================")
    file_path = input("Enter the full path of the file to monitor: ")
    
    
    original_hash = calculate_hash(file_path)
    if not original_hash:
        return

    print(f"Original Hash: {original_hash}")
    
    
    input("\nModify the file (if you want) and press Enter to check integrity...\n")
    
 
    current_hash = calculate_hash(file_path)
    if current_hash:
        print(f"Current Hash: {current_hash}")
        if compare_hashes(original_hash, current_hash):
            print("\n✅ The file has not been modified.")
        else:
            print("\n⚠️ The file has been modified!")
    else:
        print("Unable to calculate current hash.")

if __name__ == "__main__":
    main()
