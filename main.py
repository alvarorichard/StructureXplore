

def get_main_code_section(sections,base_of_code):
    addresses = []
    for section in sections:
        addresses.append(section.VirtualAddress)
    if base_of_code in addresses:
        return sections[addresses.index(base_of_code)]
    else:
        addresses.append(base_of_code)
        addresses.sort()
        if addresses.index(base_of_code) == 0:
            return sections[addresses.index(base_of_code)-1]
        else:
            
         return none 
     