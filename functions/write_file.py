import os

def write_file(working_directory, file_path, content):

    try:
        file_abs = os.path.abspath(os.path.join(working_directory, file_path))
        working_directory_abs = os.path.abspath(working_directory)

        if not (file_abs == working_directory_abs or file_abs.startswith(working_directory_abs + "/")):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.exists(os.path.dirname(file_abs)):
            os.makedirs(os.path.dirname(file_abs))

        with open(file_abs, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {e}"