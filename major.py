#!/usr/bin/python3.6
print("content-type: text/html")
print()	
import cgi
import subprocess
import base64
from PIL import Image
from io import BytesIO
from facereg import *

form=cgi.FieldStorage()

imgdata = form.getvalue("n")
filename = '/root/Desktop/test.txt'

print("""
<body style='background:linear-gradient(to right, #4ca1af, #c4e0e5);'>
""")
if(imgdata):
	str = imgdata.split(",",1)[1]
	#print(str)
	im = Image.open(BytesIO(base64.b64decode(str)))
	im.save('image.png','PNG')
	#print('Accuracy')
	conf = face_recognize()
	if conf>70:
		
		print("<h2> Welcome Prashant!!</h2>")
		print("<p>Authenticated with ")
		print(conf)
		print(" % accuracy!!</p><br>")
		print("<a href='http://192.168.43.18:9876/hotspots.html'>Covid Hotspot Data</a>")
	else:
		print("<h2> Sorry,</h2>")
		print("<p>You are not authenticated..please try again!</p>")
		
		print("<a href='http://192.168.43.18:9876/cgi-bin/neudock.py'> Home</a>")

print("</body>")
