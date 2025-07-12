import os


def get_files_info(working_directory, directory=None):

    try:
        directory_abs = os.path.abspath(os.path.join(working_directory, directory))
        working_directory_abs = os.path.abspath(working_directory) 

        if not (directory_abs == working_directory_abs or directory_abs.startswith(working_directory_abs + "/")):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(directory_abs):
            return f'Error: "{directory}" is not a directory'
        
        files = os.listdir(directory_abs)
        for file in files:
            file_path = os.path.join(directory_abs, file)
            print(f"- {file}: file_size={os.path.getsize(file_path)}, is_dir={os.path.isdir(file_path)}")

    except Exception as e:
        return f"Error: {e}"