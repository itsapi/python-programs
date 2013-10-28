import time
import networking as net

network = net.Net()

network.putData([['x',0]])

try:
    while True:
        data = network.getData()
        val = input(':')
        network.putKey('x', int(val))
        network.putKey('z', 50)

        print(network.client.get('x'))
        time.sleep(1)
except KeyboardInterrupt:
    network.server.stop()
