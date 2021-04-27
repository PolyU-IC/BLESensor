from bluepy import btle 


class Delegate(btle.DefaultDelegate):
	def __init__(self):
		btle.DefaultDelegate.__init__(self)
	def handlenotification(self,cHandle,data):
		print("The cHandle is {} ".format(str(cHandle)))
		print("The data is {} ".format(str(data)))


#initialisation

p = btle.Peripheral("50:02:91:89:5b:5a")
#p.setDelegate(Delegate())


chlist = p.getCharacteristics()

print("Device UUIDs: \n")
for ch in chlist:
	print(ch.uuid)

svc = p.getServiceByUUID("6e400001-b5a3-f393-e0a9-e50e24dcca9e")
ch_info = svc.getCharacteristics("6e400001-b5a3-f393-e0a9-e50e24dcca9e")[0]
print("The first characteristic message value is "+ch_info.read().rstrip()+"!"+"\n")
#The type of ch_inf.read() is string



connected = False
x = 0
y = 0
z = 0



while True:
	data = ch_info.read().split()
	if p.waitForNotifications(1.0):
		continue
	if not ch_info.read():
		print("Waiting.....")
	else:
		if connected == False:
			print("Connected to BLE Server")
			connected = True
		#print(ch_info.read())
		#print(type(ch_info.read()))
		if len(data)==3:
			x= float(data[0])
			y= float(data[1])
			z= float(data[2])
		print("The acceleration of data are "+"%5.2f %5.2f %5.2f G"%(x,y,z))
		#print(len(ch_info.read().split()))





