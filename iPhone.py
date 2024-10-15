import os

file = open("/private/var/db/os_eligibility/eligibility.plist") #file that contains a few numbers that are important for iPhone Mirroring

newFile = ""

i = 0
for line in file:
    if "IRON" in line:
        newFile += line
        i = 179 #line 179 is the line where the important part of the file starts for me. YOU DON'T NEED TO CHANGE ANYTHING. It counts relative to the "IRON" line
    elif i!=0:
        i += 1
        match i:
            case 184:
                newFile += line.replace("2", "4")
            case 188 | 190:
                newFile += line.replace("2", "3")
            case 194:
                i = 0
                newFile += line
            case _:
                newFile += line



    else:
        newFile += line

file.close()
file = open("/private/var/db/os_eligibility/eligibility.plist", "w")
file.write(newFile)
file.close()