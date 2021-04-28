from bluepy import btle 

#Data visualization
import matplotlib
matplotlib.use('tkagg') #Use Matplotlib with tkinter 'tkagg'
import matplotlib.pyplot as plt

import numpy as np


plt.axis([0,100,-1,1]) #xmin, xmax, ymin, ymax



#initialization of animation






#class person:
#	def __init__(self,name,age):
#		self.name = name
#		self.age = age
#	def print_name(self):
#		print("{0} is {1} years old.".format(self.name.capitalize(),self.age))

#p1 = person("benny","25")

#print(type(p1))
#p1.print_name()









#initialisation

p = btle.Peripheral("50:02:91:89:5b:5a")



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


end=100
init_num=0
window_size =100



#Initialization of X,Y,Z
x_val_array =np.zeros(window_size)
y_array = np.zeros(window_size)
z_array = np.zeros(window_size)

print(len(y_array))




plt.title("BLE Data Logging of Acceleration X,Y,Z")



while True:
	try:
		end_add =100
		init_num_add = 0
		x_array = np.linspace(init_num_add,end_add,window_size)
		x_array = x_array[init_num_add:]
		print(len(x_array))
		data = ch_info.read().split()
		#X,Y,Z Data in real-time
		x=float(data[0])
		x_val_array[window_size-1] = x


		y = float(data[1])
		y_array[window_size-1] =y

		z = float(data[2])
		z_array[window_size-1] = z

		#x,y,z plots
		x_plot=plt.plot(x_array,x_val_array,"r")
		y_plot=plt.plot(x_array,y_array,"g")
		z_plot=plt.plot(x_array,z_array,"b")
		plt.legend(loc='upper left',handles=[x_plot,y_plot,z_plot],labels=["x","y","z"],bbox_to_anchor=(5,5))


		plt.pause(0.05)
		plt.clf()
		init_num_add+=1
		end_add+=1
                x_val_array[window_size-2] = x_val_array[window_size-1]
                x_val_array = np.delete(x_val_array,0)
                x_val_array=np.append(x_val_array,0)




		y_array[window_size-2] = y_array[window_size-1]
		y_array = np.delete(y_array,0)
		y_array=np.append(y_array,0)


                z_array[window_size-2] = z_array[window_size-1]
                z_array = np.delete(z_array,0)
                z_array=np.append(z_array,0)




		print("The length of numpy array is %d"%(len(y_array)))


	except:
		raise Exception("BLE Server is not correctly configured.")
		break
	finally:
		pass


