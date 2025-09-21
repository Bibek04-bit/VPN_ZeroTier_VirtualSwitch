import socket
import sys

server_port = None
if len(sys.argv)!=2:
  print("Usage: python3 vswitch.py {VSWITCH_PORT}")
  sys.exit(1)
else:
  server_port = int(sys.argv[1])
server_addr = ("0.0.0.0", server_port)





