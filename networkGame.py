import networking as net

network = net.Net()

network.putData([['x',0]])

try:
    while True:
        data = network.getData()
        
        val = input(':')
        try:
            val = int(val) + network.getKey('x')
            network.putKey('x', val)
        except ValueError:
            print('Invalid input.')

        print(network.client.get('x'))

except KeyboardInterrupt:
    network.server.stop()