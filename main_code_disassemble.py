exe_file_path = 'path/to/exe/file'

try:
  #parse exe file
  exe = pefile.PE(exe_file_path)
  try:
    #call the function we created earlier
    fine_disassemble(exe)
  except:
    print('something is wrong with this exe file')
except:
  print('pefile cannot parse this file')