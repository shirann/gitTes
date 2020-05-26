# import time
#
# from bluetooth import *
#
# #
# client_socket = BluetoothSocket(RFCOMM)
# client_socket.connect(('EC:D0:9F:3F:45:43',3))
# client_socket.send('hello')
# print('finished')
# #
# while True:
#     time.sleep(1)
#     continue
# client_socket.close()

from bluetooth import *

services=find_service(name="helloService",
                            uuid=SERIAL_PORT_CLASS)

for i in range(len(services)):
   match=services[i]
   if(match["name"]=="helloService"):
      port=match["port"]
      name=match["name"]
      host=match["host"]

      print(name, port, host)

      client_socket=BluetoothSocket( RFCOMM )

      client_socket.connect((host, port))

      client_socket.send("Hello world")

      client_socket.close()

      break