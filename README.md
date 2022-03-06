# shadertoytonotitg
Converts Shadertoy GLSL to NotITG GLSL.

IMPORTANT INFORMATION:
At the moment, this converter supports everything EXCEPT for iChannels. Those will need to be done manually, and unfortunately, there is no easy way to implement iChannels at the moment it seems.

HOW TO USE:
Run the main.py file, a file dialog should come up - select your file, and it should fully convert and be written to the file you prompted.

COMMON ERRORS:

Error:
"requires "#extension GL_EXT_gpu_shader4 : enable" before use"

Fix: 
Uncomment the "This may need to be uncommented" line at the top of the converted code.

Error:
" ...  requires "#version X" or later"

Fix:
Increase or decrease the given version number in the converted code.

OTHER ERRORS:
Most other errors are caused by improper Shadertoy coding, and will manually need to be fixed.
