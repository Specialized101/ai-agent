import os
from functions.config import MAX_CHARS

def get_file_content(working_directory, file_path):

    try:
        file_abs = os.path.abspath(os.path.join(working_directory, file_path))
        working_directory_abs = os.path.abspath(working_directory)
        
        if not (file_abs == working_directory_abs or file_abs.startswith(working_directory_abs + "/")):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(file_abs):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(file_abs, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if len(file_content_string) == MAX_CHARS:
                file_content_string += f'[...File "{file_path}" truncated at 10000 characters]'
            return file_content_string

    except Exception as e:
        return f"Error: {e}"
