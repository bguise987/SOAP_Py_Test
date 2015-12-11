# This is some simple code meant to test out interfacing Python code and a SOAP API
# Written by Ben Guise
# Released under GNU GPL v3 license

# Some code was referenced from various pages on www.diveintopython.net
# http://www.diveintopython.net/soap_web_services/introspection.html

# Note: This Python script makes use of the Python package SOAPpy, which requires wstools

from SOAPpy import WSDL
wsdlFile = 'ndfdXML.wsdl'
server = WSDL.Proxy(wsdlFile)
keys = server.methods.keys()

print("Print out methods that the server can provide us:\n\n")
for var in keys:
	print(var)
print("\n")

print("Print the input parameters:\n")
callInfo = server.methods['LatLonListZipCode']
params = callInfo.inparams

for par in params:
	print(par)

print(callInfo.inparams[0].name)
print(callInfo.inparams[0].type)

print("\nPrint the output parameters:\n")
callInfo.outparams
print(callInfo.outparams[0].name)
print(callInfo.outparams[0].type)

# Let's try LatLonListZipCode(90210)
print("Let's try to access the NOAA API to get some information on zip code 90210:")
returnData = server.LatLonListZipCode('90210')
print(returnData)
