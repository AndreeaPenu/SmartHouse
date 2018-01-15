import bluetooth
 
server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
 
port = 1
server_sock.bind((&quot;&quot;,port))
server_sock.listen(1)
 
client_sock,address = server_sock.accept()
print &quot;Accepted connection from &quot;,address
while True:
 
 data = client_sock.recv(1024)
 print &quot;received [%s]&quot; % data
 if (data == &quot;e&quot;):
 print (&quot;Exit&quot;)
 break
 
client_sock.close()
server_sock.close()