def binary2ip(binary):

	#declarations
	firstOctet = ""
	secondOctet = ""
	thirdOctet = ""
	fourthOctet = ""

	firstDecimal = ""
	secondDecimal = ""
	thirdDecimal = ""
	fourthDecimal = ""

	ip = ""

	for i in range(len(binary)):
		if i < 8 :
			firstOctet += str(binary[i])
		elif i < 16 :
			secondOctet += str(binary[i])
		elif i < 24 :
			thirdOctet += str(binary[i])
		else :
			fourthOctet += str(binary[i])
	
	firstDecimal = str(int(firstOctet, 2))
	secondDecimal = str(int(secondOctet, 2))
	thirdDecimal = str(int(thirdOctet, 2))
	fourthDecimal = str(int(fourthOctet, 2))

	ip = firstDecimal+"."+secondDecimal+"."+thirdDecimal+"."+fourthDecimal
	return ip

def sweetBinary(binary):

	binaryIp = ""
	
	for i in range(len(binary)):
		binaryIp += str(binary[i])

	binaryIp = binaryIp[0:8]+"."+binaryIp[8:16]+"."+binaryIp[16:24]+"."+binaryIp[24:]
	return binaryIp

def whatIsClass(binary):
	
	octet = ""
	decimal = 0
	_class = "" 
	
	for i in range(8):
		octet += str(binary[i])
	decimal = int(octet, 2)
	
	if decimal > 0 and decimal <= 127:
		_class = "A"
	elif decimal >= 128 and decimal <= 191:
		_class = "B"
	elif decimal >= 192 and decimal <= 223:
		_class = "C"

	return _class

def getSubnetMask(subnetId, _class):
	
	subnetMask = ""

	if _class == "A":
		subnetMask += "11111111"
	elif _class == "B":
		subnetMask += "1111111111111111"
	elif _class == "C":
		subnetMask += "111111111111111111111111"

	for i in range(len(subnetId)):
		subnetMask += "1"
	subnetMask += "000000000000000000000000"
	subnetMask = subnetMask[0:32]
	return binary2ip(subnetMask)

def getSubnetWork(binaryIp, subnetId, _class):
	subnetWork = ""

	if _class == "A":
		lenght = 8 + len(subnetId)
		subnetWork += binaryIp[0:lenght]
	elif _class == "B":
		lenght = 16 + len(subnetId)
		subnetWork += binaryIp[0:lenght]
	elif _class == "C":
		lenght = 24 + len(subnetId)
		subnetWork += binaryIp[0:lenght]

	subnetWork += "000000000000000000000000"
	subnetWork = subnetWork[0:32]
	return binary2ip(subnetWork)

def getSubnetBroadcast(binaryIp, subnetId, _class):
	subnetBroadcast = ""

	if _class == "A":
		lenght = 8 + len(subnetId)
		subnetBroadcast += binaryIp[0:lenght]
	elif _class == "B":
		lenght = 16 + len(subnetId)
		subnetBroadcast += binaryIp[0:lenght]
	elif _class == "C":
		lenght = 24 + len(subnetId)
		subnetBroadcast += binaryIp[0:lenght]

	subnetBroadcast += "111111111111111111111111"
	subnetBroadcast = subnetBroadcast[0:32]
	return binary2ip(subnetBroadcast)

def getFirstMachine(binaryIp, subnetmaskbits):
	firstMachine = binaryIp[0:subnetmaskbits]
	firstMachine += "000000000000000000000000"
	firstMachine = firstMachine[0:31]
	firstMachine += "1"
	
	return binary2ip(firstMachine)

def getLastMachine(binaryIp, subnetmaskbits):
	lastMachine = binaryIp[0:subnetmaskbits]
	lastMachine += "111111111111111111111111"
	lastMachine = lastMachine[0:31]
	lastMachine += "0"
	
	return binary2ip(lastMachine)

def getMainNetwork(binaryIp, _class):
	mainNetwork = ""

	if _class == "A":
		mainNetwork += binaryIp[0:8]
		mainNetwork += "000000000000000000000000"
	elif _class == "B":
		mainNetwork += binaryIp[0:16]
		mainNetwork += "0000000000000000"
	elif _class == "C":
		mainNetwork += binaryIp[0:24]
		mainNetwork += "00000000"

	return binary2ip(mainNetwork)

def getMaxSubnetCount(subnetId):
	maxSubnet = 1
	for i in range(len(subnetId)):
		maxSubnet *= 2
	return maxSubnet - 2

def getMaxComputerCount(machineId):
	maxComputer = 1
	for i in range(len(machineId)):
		maxComputer *= 2
	return maxComputer - 2
 
from random import randint 
import os

#clean terminal screen
os.system("reset")

#declare array
address = []
binaryIp = "" #not array
sweetAddress = ""
ip = ""
_class = ""
subnetmaskbits = 0
subnetId = ""
machineId = ""
subnetMask = ""
subnetWork = ""
subnetBroadcast = ""
firstMachine = ""
lastMachine = ""
mainNetwork = ""
maxSubnet = 0
maxMachine = 0

for i in range(32):
	address.append(0)

for i in range(len(address)): 
	address[i] = randint(0,1)

for i in range(len(address)):
	binaryIp += str(address[i])

sweetAddress = sweetBinary(address)
ip = binary2ip(address)
_class = whatIsClass(address)

if _class == "A":
	subnetmaskbits = randint(9, 30)
	subnetId = binaryIp[8:subnetmaskbits]
	machineId = binaryIp[subnetmaskbits:]
elif _class == "B":
	subnetmaskbits = randint(17, 30)
	subnetId = binaryIp[16:subnetmaskbits]
	machineId = binaryIp[subnetmaskbits:]
elif _class == "C":
	subnetmaskbits = randint(25, 30)
	subnetId = binaryIp[24:subnetmaskbits]
	machineId = binaryIp[subnetmaskbits:]

subnetMask = getSubnetMask(subnetId, _class)
subnetWork = getSubnetWork(binaryIp, subnetId, _class)
subnetBroadcast = getSubnetBroadcast(binaryIp, subnetId, _class)
firstMachine = getFirstMachine(binaryIp, subnetmaskbits)
lastMachine = getLastMachine(binaryIp, subnetmaskbits)
mainNetwork = getMainNetwork(binaryIp, _class)
maxSubnet = getMaxSubnetCount(subnetId)
maxComputer = getMaxComputerCount(machineId)

#print "[+] Binary address : "+binaryIp
print "[+] Sweet binary address : "+sweetAddress
print "[+] IP : "+ip
print "[+] Subnet mask bits count : "+str(subnetmaskbits)
print "[+] Class : "+_class
print "[+] Subnet id : "+subnetId
print "[+] Machine id : "+machineId
print "[+] This is the "+str(int(subnetId, 2))+"th usable subnet in this class "+_class+" net."
print "[+] This is the "+str(int(machineId, 2))+"th machine on this subnetwork."
print "[+] Subnet mask : "+ subnetMask 
print "[+] Subnet work : "+ subnetWork 
print "[+] Subnet broadcast : "+ subnetBroadcast
print "[+] First machine ip : "+ firstMachine
print "[+] Last machine ip : "+ lastMachine
print "[+] Main network : "+ mainNetwork
print "[+] Maximum subnet count : "+ str(maxSubnet)
print "[+] Maximum computer count : "+ str(maxComputer)