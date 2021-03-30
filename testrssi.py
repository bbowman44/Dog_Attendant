from bluepy.btle import Scanner

scanner = Scanner()
devices = scanner.scan(5.0)

for device in devices:
    print("DEV = {} RSSI = {}".format(device.addr, device.rssi))
    if (device.addr == "f5:af:3d:5b:0e:0d" and device.rssi < 60):
        print("It's Close")
