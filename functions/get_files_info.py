import os
from google import genai
from google.genai import types

def get_files_info(working_directory, directory=None):

    try:
        directory_abs = os.path.abspath(os.path.join(working_directory, directory))
        working_directory_abs = os.path.abspath(working_directory) 

        if not (directory_abs == working_directory_abs or directory_abs.startswith(working_directory_abs + "/")):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(directory_abs):
            return f'Error: "{directory}" is not a directory'
        
        files = os.listdir(directory_abs)
        output = ""
        for file in files:
            file_path = os.path.join(directory_abs, file)
            output += f"- {file}: file_size={os.path.getsize(file_path)}, is_dir={os.path.isdir(file_path)}\n"
        return output

    except Exception as e:
        return f"Error: {e}"

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)