import time
import zmq
import sys

port = "5556"

if len(sys.argv) > 1:
    port = sys.argv[1]
    int(port)

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:%s" % port)
print("[%s] Listening for incoming messages." % port)

while True:
    message = socket.recv()
    print("Processing ", message, end='')
    time.sleep(1)
    socket.send_string("World from %s" % port)