import serial.tools.list_ports


def find_available_ports():
    ports = []
    for port in serial.tools.list_ports.comports():
        ports.append(port.device)
    return ports


print(find_available_ports())
