import struct
ret = struct.pack('i', 4096)
print(ret)

num = struct.unpack('i', ret)
print(num[0])