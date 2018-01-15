1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
import bluetooth
import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
 
def Blink(numTimes,speed):
 for i in range(0,numTimes):
 GPIO.output(18,True)
 print &quot;Blinking &quot; + str(i+1)
 time.sleep(speed)
 GPIO.output(18,False)
 time.sleep(speed)
 print (&quot;Done Blinking LED&quot;)
 
server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
 
port = 1
server_sock.bind((&quot;&quot;,port))
server_sock.listen(1)
 
client_sock,address = server_sock.accept()
print &quot;Accepted connection from &quot;,address
while True:
 
 data = client_sock.recv(1024)
 print &quot;received [%s]&quot; % data
 if (data == &quot;1&quot;):
 print (&quot;LED ON&quot;)
 GPIO.output(18,GPIO.HIGH)
 if (data == &quot;0&quot;):
 print (&quot;LED OFF&quot;)
 GPIO.output(18,GPIO.LOW)
 if (data == &quot;5&quot;):
 print (&quot;LED Blink&quot;)
 Blink(10,0.1)
 if (data == &quot;e&quot;):
 print (&quot;Exit&quot;)
 break
 
client_sock.close()
server_sock.close()