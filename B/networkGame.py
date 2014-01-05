import time
import networking as net

network = net.Net()

network.putData([['x',0]])

try:
    while True:
        data = network.getData()
        val = input(':')
        data[0][1] += int(val)
        network.putData(data)

        print(network.client.get('x'))
        time.sleep(1)
except KeyboardInterrupt:
    network.server.stop()
