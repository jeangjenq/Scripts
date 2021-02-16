# def natron_write(file_input, ccc, cube, output):
file_input = "input_replace_here"
ccc = "cc_replace_here"
cube = "cube_replace_here"
file_output = "output_replace_here"

# create read node
reader = app.createReader(file_input)
reader_color = reader.getParam("ocioInputSpaceIndex")
reader_color.setValue("sRGB")
# set scriptname to be refer by command-line
reader.setScriptName("ColorReader")

# create colorspace node
colorspace = app.createNode("fr.inria.openfx.OCIOColorSpace")
colorspaceOut = colorspace.getParam("ocioOutputSpaceIndex")
colorspaceOut.setValue("input/AlexaV3LogC")
colorspace.connectInput(0, reader)

# create cdl transform node
color_cdl = app.createNode("fr.inria.openfx.OCIOFileTransform")
cdl_file = color_cdl.getParam("file")
cdl_file.setValue(ccc)
color_cdl.connectInput(0, colorspace)

# create OCIOFileTransform
color_file = app.createNode("fr.inria.openfx.OCIOFileTransform")
cube_file = color_file.getParam("file")
cube_file.setValue(cube)
color_file.connectInput(0, color_cdl)

# create Write node
writer = app.createWriter(file_output)
# set writer format to match input format
writer_format = writer.getParam("formatType")
writer_format.setValue(0)
# set scriptname to be refer by command line
writer.setScriptName("LUTWriter")
writer.connectInput(0, color_file)