import sys
import struct


archive = sys.argv[1]
new_name = sys.argv[2]

with open(archive, 'rb') as source:
	archive_source = source.read()

name_len = struct.unpack("h", archive_source[26:28])[0]
dir_len = struct.unpack("i", archive_source[-6:-2])[0]
new_name_len = int(len(new_name))

new_archive = archive_source[:26] + \
			struct.pack('h', new_name_len) + \
			archive_source[28:30] + \
			bytes(new_name.encode("utf-8")) + \
			archive_source[30+name_len:-6] + \
			struct.pack('i', dir_len + new_name_len - name_len) + \
			archive_source[-2:]

with open("./kek.zip", "wb") as dest:
	dest.write(new_archive)