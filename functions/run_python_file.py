import os
import subprocess

def run_python_file(working_directory, file_path):

    try:
        file_abs = os.path.abspath(os.path.join(working_directory, file_path))
        working_directory_abs = os.path.abspath(working_directory)

        if not (file_abs == working_directory_abs or file_abs.startswith(working_directory_abs + "/")):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.exists(file_abs):
            return f'Error: File "{file_path}" not found.'
        if not file_abs.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'
             
        cp = subprocess.run(["python3", file_abs], cwd=working_directory_abs, timeout=30, capture_output=True, text=True)
        
        if not (cp.stdout or cp.stderr):
            return "No output produced"
        
        output = ""
        output += f"STDOUT: {cp.stdout}\n"
        output += f"STDERR: {cp.stderr}\n"

        if (cp.returncode != 0):
            output += f"Process exited with code {cp.returncode}"

        return output
    except Exception as e:
        return f"Error: executing Python file: {e}"