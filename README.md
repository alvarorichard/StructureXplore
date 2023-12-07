# StructureXplore 

This project consists of a set of Python scripts designed for disassembling executable files. It utilizes the pefile module for parsing Portable Executable (PE) files and the Capstone disassembly framework for the disassembly process.


### Files Description

1. **fine_disassemble.py**
   - **Purpose**: Disassembles the main code section of an executable file.
   - **Key Function**: `fine_disassemble(exe)`
     - **Parameters**: `exe` - an executable file loaded using `pefile`.
     - **Process**: Identifies and disassembles the main code section, using the Capstone framework for detailed disassembly.

2. **import_capstone_pefile.py**
   - **Purpose**: Importing necessary modules.
   - **Imports**: 
     - `capstone` for disassembly.
     - `pefile` for parsing PE files.

3. **main_code_disassemble.py**
   - **Purpose**: Main script to execute the disassembler.
   - **Process**: 
     - Loads an exe file (main.exe) using `pefile`.
     - Calls `fine_disassemble` to disassemble the loaded exe file.
     - Includes error handling for exe file parsing and disassembly process.

4. **main_code_section.py**
   - **Purpose**: Identifies the main code section in an executable file.
   - **Key Function**: `get_main_code_section(sections, base_of_code)`
     - **Parameters**: 
       - `sections`: Sections of the executable.
       - `base_of_code`: The base address of the code section.
     - **Process**: Determines which section of the executable is the main code section based on its address.

## Requirements
- Python 3.x
- `pefile` module
- `capstone` module

## Usage
1. Ensure all dependencies are installed.
2. Run `main_code_disassemble.py` to disassemble a specified executable file.

## Note
- This tool is intended for educational and legal purposes only.
- Be cautious when handling executable files, especially from untrusted sources.

