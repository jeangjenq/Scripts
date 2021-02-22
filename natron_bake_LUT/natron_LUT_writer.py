import os
natron_exec = "D:/natron/bin/NatronRenderer.exe"

# shot input, color and output
file_input = ""
ccc = ""
cube = ""
file_output = ""

# specify natron template and output location
template = "D:/natron_LUT_template.py"
template_out = "D:/natron_LUT_output.py"

# replace placeholder in template with shot variables
check_words = ("input_replace_here", "cc_replace_here", "cube_replace_here", "output_replace_here")
replace_words = (file_input, ccc, cube, file_output)

read_template = open(template, "rt")
write_template = open(template_out, "wt")

for line in read_template:
    for check, replace in zip(check_words, replace_words):
        line = line.replace(check, replace)
    write_template.write(line)

read_template.close()
write_template.close()

# launch natron to write
start = 'start cmd /k %s %s -w LUTWriter 1-1' % (natron_exec, template_out)
os.popen(start)