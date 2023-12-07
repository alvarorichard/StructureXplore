#the function takes two arguments, both are fetched from the exe file using
#pefile. the first one is the list of all sections. The second one is the
#address of the first instruction in the program
def get_main_code_section(sections, base_of_code):
    addresses = []
    #get addresses of all sections
    for section in sections: 
        addresses.append(section.VirtualAddress)
        
    #if the address of section corresponds to the first instruction then
    #this section should be the main code section
    if base_of_code in addresses:    
        return sections[addresses.index(base_of_code)]
    #otherwise, sort addresses and look for the interval to which the base of code
    #belongs
    else:
        addresses.append(base_of_code)
        addresses.sort()
        if addresses.index(base_of_code)!= 0:
            return sections[addresses.index(base_of_code)-1]
        else:
            #this means we failed to locate it
            return None