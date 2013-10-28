import sys
import networking as net

try:
    port = int(sys.argv[1])
except:
    port = 0

network = net.Net(port)

network.putData([['x',0]])

try:
    while True:
        data = network.getData()
        val = input(':')
        val = int(val) + network.getKey('x')
        network.putKey('x', val)

        print(network.client.get('x'))

except KeyboardInterrupt:
    network.server.stop()
