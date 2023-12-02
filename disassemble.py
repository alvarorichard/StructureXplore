def fine_disassemble(exe):
    main_code = get_main_code_section(exe.sections,exe.OPTIONAL_HEADER.BaseOfCode)
    
    md = Cs(CS_ARCH_X86, CS_MODE_32)
    md.detail = True
    last_address = 0
    last_size = 0
    
    begin = main_code.PointerToRawData
    
    end = main_code.PointerToRawData + main_code.SizeOfRawData
    
    while true:
        
        data = exe.get_memory_mapped_image()[begin:end]
        for i in md.disasm(data,begin):
            print("0x%x:\t%s\t%s" %(i.address,i.mnemonic,i.op_str))
            last_address = i.address
            last_size = i.size
            
        begin = max(int(last_address),begin)+last_size+1
        if begin >= end:
            print("disassemble done")
            break