exe_file_path = 'path/to/exe'

try:
    exe = pefile.PE(exe_file_path)
    
    try:
     fine_disassemble(exe)
    except: 
     print("disassemble failed")
except:
    print("open exe failed")
    