import os
import sys
import tkinter as tk
from tkinter import filedialog as fd
import fileinput
import time


#####################################################################
#checking for iresolution, itime, etc
#####################################################################
itime = ('nil')
ires = ('nil')
iframe = ('nil')
imouse = ('nil')
idate = ('nil')
iframerate = ('nil')
#####################################################################

print('Prompting file...')

file_path = fd.askopenfilename()

startTime = time.time()

searchfile = open(file_path, "r")
for line in searchfile:
    if "iResolution" in line: 
        ires = 'true'
    if "iTime" in line: 
        itime = 'true'
    if "iFrame" in line: 
        iframe = 'true'
    if "iMouse" in line: 
        imouse = 'true'
    if "iDate" in line: 
        idate = 'true'
    if "iFrameRate" in line:
        iframerate = 'true'
searchfile.close()

#if ichannel == 'true':
    #print('THIS SHADER CONTAINS ICHANNEL, WHICH IS NOT SUPPORTED AT THE MOMENT.')

voidmain = ("""void main() {
    mainImage(gl_FragColor.rgba, gl_FragCoord.xy);
    gl_FragColor.a = 1.0;
}
""")

iresReq = ("""
uniform vec2 imageSize;
""")
itimeReq = ("""
uniform float time;
""")
iframeReq = ("""
uniform float frame;
""")
imouseReq = ("""
const vec4 iMouse = vec4(0.0, 0.0, 0.0, 0.0);
""")
idateReq = ("""
const vec4 iDate = vec4(0.0);
""")
iframerateReq = ("""
float frameRate = 60.0;
""")

import fileinput

reading_file = open(file_path, "r")

#####################################################################
#adding neccessary lines
#####################################################################
f = open(file_path,'r+')
lines = f.readlines() # read old content
f.seek(0) # go back to the beginning of the file

f.write('#version 120')

if ires == ('true'):
    f.write(iresReq) 
if itime == ('true'):
    f.write(itimeReq)
if iframe == ('true'):
    f.write(iframeReq)
if imouse == ('true'):
    f.write(imouseReq)
if idate == ('true'):
    f.write(idateReq)
if iframerate == ('true'):
    f.write(iframerateReq)
f.write("""
//this may need to be uncommented
//#extension GL_EXT_gpu_shader4 : enable
""")

for line in lines: # write old content after new
    f.write(line)
f.close()

# Open the file in append & read mode ('a+')
with open(file_path, "a+") as file_object:
    # Move read cursor to the start of file.
    file_object.seek(0)
    # If file is not empty then append '\n'
    data = file_object.read(100)
    if len(data) > 0 :
        file_object.write("\n")
        file_object.write("\n")
    # Append text at the end of file
        file_object.write(voidmain)
        file_object.write("\n //This shader was converted with satori's shader converter, if there are any bugs, please contact me at satori#6585. Also, you can submit issues at the github repo at: https://github.com/satoriscripts/shadertoytonotitg/tree/main")
#####################################################################
#####################################################################


#####################################################################
#finding and replacing (converting)
#####################################################################
print('Converting...')

# Read in the file
with open(file_path, 'r') as file :
  filedata = file.read()

# Replace the target strings
filedata = filedata.replace('iTime', 'time')
filedata = filedata.replace('iResolution', 'imageSize')
filedata = filedata.replace('iFrame', 'frame')


# Write the file out again
with open(file_path, 'w') as file:
  file.write(filedata)
#####################################################################
#####################################################################
executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))
print('Successfully  converted in.')
print('Please credit the shadertoy you used!')
print('YOU MAY HAVE TO TWEAK THE VERSION NUMBER HIGHER OR LOWER!')
print('Be sure to put your shader through https://sm.heysora.net/glsl/ to check for silent errors.')
print('PLEASE NOTE YOU WILL HAVE TO CONVERT ICHANNELS MANUALLY!')
print('https://github.com/PandaP17/shadertoytonotitg/tree/main')
input("Press any key to close...")
