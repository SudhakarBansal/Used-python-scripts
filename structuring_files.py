"""problem : the SKU codes of some product images have been incorrectly assigned. To fix this, there is need to rename the image files to a new set of SKU codes in a consistent numeric sequence."""


import os

def structured_names(directory, extension):
    """
    Renames all files in the specified directory with the given extension to a numeric sequence.
    
    :param directory: Path to the directory containing the files.
    :param extension: Extension of the files to rename (without the dot).
    :return: List of renamed files or a message if the directory doesn't exist.
    """
    
    # Check if the provided directory exists
    if not os.path.isdir(directory):
        return "No such directory"

    # Change to the specified directory
    os.chdir(directory)
    
    # List to store filenames with the given extension
    files_with_extension = [item for item in os.listdir() if item.endswith(f".{extension}")]
    
    if not files_with_extension:
        return f"No files with the .{extension} extension found."
    
    # Sort files to ensure consistent numeric naming
    files_with_extension.sort()
    
    # List to keep track of renamed files
    renamed_files = []
    
    # Rename files to a numeric sequence
    for i, item in enumerate(files_with_extension, start=1):
        new_name = f"{i}.{extension}"
        # Ensure not to overwrite existing files
        if not os.path.exists(new_name):
            os.rename(item, new_name)
            renamed_files.append(new_name)
        else:
            print(f"Warning: The file {new_name} already exists. Skipping rename for {item}.")
    
    return renamed_files

# Input from the user
pathname = input("Enter the complete address of the folder: ")
extension = input("Enter the extension of files to rename (without the dot): ")

# Print the result of the renaming operation
print(structured_names(pathname, extension))