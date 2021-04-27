# BLE-Sensing
Use ESP32 as sensor nodes to broadcast streaming sensor data to ESP32 server node via Bluetooth Low Energy.

<html>
  
<body>  
  <pre>
The project is aiming to retrieve real-time raw data of IMU from M5StickC
to a BLE server errected from raspberry pi via Bluetooth Low Energy to form
a IOT mesh network and for data analytic. 
  </pre>
<br>
<h2><u><b>M5StickC</b></u></h2>
<br>
<pre>

The esp32 project file is located inside the folder of BLE_M5STICKC and 
is called BLE_M5STICKC.ino.The M5StickC (sensor node) should be launched 
first to build up a BLE server. Then, raspberry pi would serve as a client
to listen to incoming data. 


</pre>

<h2><u><b>Raspberry pi</b></u></h2>
<br>
<pre>
After the M5StickC established as a BLE server, we can use python scripts in
raspberry pi to scan the MAC address of the M5StcikC sensor node with listening
to specific characteristic UUID of specific service.
</pre>
<br>
<h2><b>Data with Console Display</b></h2>
<pre>To run the script with incoming acceleration data from sensor node in console display:</pre>

<pre>
     python ble_noti.py
</pre>  
<img src="https://github.com/chunwmak9/BLE-Sensing/blob/main/BLE_console_display.jpeg" width="40%" height="40%">
<br>

<h2><b> Data Visualization</b></h2>
<pre>To run the script with incoming acceleration data from sensor node with data monitor:</pre>


<pre>
     python ble_accel_vis.py
</pre>
<img src="https://github.com/chunwmak9/BLE-Sensing/blob/main/BLE_data_visualization.jpeg" width="40%" height="40%">







</body>
<html>
