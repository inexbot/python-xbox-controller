import socket
import json
import zlib


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def Connect(ip, port):
    s.connect((ip, port))


def getBuffer(command, data):
    _preSend = bytearray()
    # get byte of data
    databyte = json.dumps(data).encode()
    # Length
    dataLength = databyte.__len__()
    dataLengthBytes = dataLength.to_bytes(
        length=2, byteorder="big", signed=False)
    # Command
    commandBytes = command.to_bytes(length=2, byteorder="big", signed=False)
    # _preSend
    _preSend.append(0x4E)
    _preSend.append(0x66)
    _preSend.extend(dataLengthBytes)
    _preSend.extend(commandBytes)
    _preSend.extend(databyte)
    # Crc32
    crc32Num = zlib.crc32(bytes(_preSend[2:]), 0)
    crc32Bytes = crc32Num.to_bytes(length=4, byteorder="big", signed=False)
    _preSend.extend(crc32Bytes)
    return bytes(_preSend)


def SendMessage(command, data):
    s.send(getBuffer(command, data))
