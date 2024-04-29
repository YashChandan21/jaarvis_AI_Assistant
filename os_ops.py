import os
import subprocess as sp

paths = {
    'notepad': "C:\\notepad_path",
    'calculator': "C:\\calculator_path"
}

# To open Camera
def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)

# Open Notepad and other functions
def open_notepad():
    os.startfile(paths['notepad'])

def open_calculator():
    os.startfile(paths['calculator'])
# We can add more funtions to open more paths

# Open Command prompt
def open_cmd():
    os.system('start cmd')





# HElps to find the path

# import os
# import subprocess
#
# def find_calculator_path():
#     # Use the 'where' command in Windows to find the path of the calculator executable
#     try:
#         result = subprocess.run(['where', 'notepad.exe'], capture_output=True, text=True, check=True)
#         calculator_path = result.stdout.strip()
#         return calculator_path
#     except subprocess.CalledProcessError:
#         print("Calculator not found on this system.")
#         return None
#
# if __name__ == "__main__":
#     calculator_path = find_calculator_path()
#     if calculator_path:
#         print("Calculator path:", calculator_path)
#     else:
#         print("Couldn't find the calculator.")
