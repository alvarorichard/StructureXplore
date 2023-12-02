def fine_disassemble(exe):
    #get main code section
    main_code = get_main_code_section(exe.sections, exe.OPTIONAL_HEADER.BaseOfCode)
    #define architecutre of the machine 
    md = Cs(CS_ARCH_X86, CS_MODE_32)
    md.detail = True
    last_address = 0
    last_size = 0
    #Beginning of code section
    begin = main_code.PointerToRawData
    #the end of the first continuous bloc of code
    end = begin+main_code.SizeOfRawData
    while True:
        #parse code section and disassemble it
        data = exe.get_memory_mapped_image()[begin:end]
        for i in md.disasm(data, begin):
            print(i)
            last_address = int(i.address)
            last_size = i.size
        #sometimes you need to skip some bytes
        begin = max(int(last_address),begin)+last_size+1
        if begin >= end:
            print("out")
            break