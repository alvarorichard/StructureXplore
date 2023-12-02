import pefile

exe_file_path = 'main.exe'

try:
  #parse exe file
  exe = pefile.PE(exe_file_path)
  try:
    #call the function we created earlier
    fine_disassemble(exe)
  except:
    print('algo está errado com este arquivo exe')
except:
  print('pefile não pode analisar este arquivo')