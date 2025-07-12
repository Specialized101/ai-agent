import os
from google import genai
from google.genai import types
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

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Lists the content of the specified file path, truncated at 10k characters, constrained in the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to read content from, relative to the working directory."
            )
        }
    )
)