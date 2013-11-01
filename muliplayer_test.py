import curses
import time
import os
import networking as net

def main(stdscr, network):
    curses.curs_set(0)
    stdscr.nodelay(1)

    maxy, maxx = stdscr.getmaxyx()
    network.putKey('maxy', maxy)
    network.putKey('maxx', maxx)

    othery = int(network.client.get('maxy'))
    otherx = int(network.client.get('maxx'))

    maxy = min((maxy, othery))
    maxx = min((maxx, otherx))

    network.putKey('x', 1)
    network.putKey('y', 1)

    py, px = 1, 1

    try:
        while True:
            x, y = int(network.getKey('x')), int(network.getKey('y'))
            xold, yold = x, y
            pxold, pyold = px, py
            
            c = stdscr.getch()
            curses.flushinp()
            if c == curses.KEY_LEFT and x > 2:
                x -= 2
            elif c == curses.KEY_RIGHT and x < maxx-2:
                x += 2
            elif c == curses.KEY_UP and y > 1:
                y -= 1
            elif c == curses.KEY_DOWN and y < maxy-2:
                y += 1
            
            if not xold == x:
                network.putKey('x', x)
            if not yold == y:
                network.putKey('y', y)
            
            try:
                py = int(network.client.get('y'))
                px = int(network.client.get('x'))
            except:
                pass
            
            if px > maxx-1:
                px = maxx-1
            if py > maxy-2:
                py = maxy-2
            
            if not (pxold == px and
                    pyold == py and
                    xold == x and
                    yold == y):
                stdscr.clear()
                stdscr.addstr(py, px, '@')
                stdscr.addstr(y, x, '#')
                stdscr.refresh()
            time.sleep(0.01)

    except KeyboardInterrupt:
        stop()

def stop():
    try:
        network.server.stop()
        curses.endwin()
    except:
        pass
    time.sleep(0.1)
    print('Unable to connect')
    os._exit(1)
	
network = net.Net(stop)
print(curses.wrapper(main, network))
