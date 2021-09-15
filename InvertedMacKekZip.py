import sys
import struct


archive = sys.argv[1]
new_name = sys.argv[2]

with open(archive, 'rb') as source:
	archive_source = source.read()

dir_offset = struct.unpack("i", archive_source[-6:-2])[0]
dir_size = struct.unpack("i", archive_source[-10:-6])[0]
name_len = struct.unpack("h", archive_source[28 + dir_offset:30 + dir_offset])[0]
new_name_len = int(len(new_name))

new_archive = archive_source[:28 + dir_offset] + \
			struct.pack('h', new_name_len) + \
			archive_source[30 + dir_offset:46 + dir_offset] + \
			bytes(new_name.encode("utf-8")) + \
			archive_source[46 + name_len + dir_offset:-10] + \
			struct.pack('i', dir_size + new_name_len - name_len) + \
			archive_source[-6:]

with open("./kek.zip", "wb") as dest:
	dest.write(new_archive)