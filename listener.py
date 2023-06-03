import socket
import re
from database import Cords


# tcp listener

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(("0.0.0.0", 8000))


sock.listen(5)

try:
    while True:
        client, addr = sock.accept()
        print("New connection from", addr)

        while True:
            receivedData = client.recv(1024)
            if not receivedData: break
            data = receivedData.decode()
            print("Received>> ", data)
            parts = data.split(",")
            if len(parts) == 18:
                lat = int(parts[5][:2]) + (float(parts[5][2:]) / 60)
                long = int(parts[7][:3]) + (float(parts[7][3:]) / 60)
                serial = parts[1]
                mode = parts[4]
                Cords(serial=serial, lat=lat, lon=long).save()
                print("Saved to db")

        client.close()
except:
    sock.close()
