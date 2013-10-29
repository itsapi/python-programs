import curses
import time
import sys
import networking as net

def main(stdscr, network):
    curses.curs_set(0)
    stdscr.nodelay(1)

    network.putKey('x',0)
    network.putKey('y',0)

    try:
        while True:
            maxy, maxx = stdscr.getmaxyx()
            x, y = int(network.getKey('x')), int(network.getKey('y'))
            xold, yold = x, y
            
            c = stdscr.getch()
            if c == curses.KEY_LEFT and x > 1:
                x -= 2
            elif c == curses.KEY_RIGHT and x < maxx-1:
                x += 2
            elif c == curses.KEY_UP and y > 0:
                y -= 1
            elif c == curses.KEY_DOWN and y < maxy-1:
                y += 1
            
            if not xold == x:
                network.putKey('x', x)
            if not yold == y:
                network.putKey('y', y)
            
            py = int(network.client.get('y'))
            px = int(network.client.get('x'))
            
            if px > maxx:
                px = maxx
            if py > maxy:
                px = maxy
            
            stdscr.clear()
            stdscr.addstr(py, px, '@')
            stdscr.addstr(y, x, '#')
            stdscr.refresh()
            time.sleep(0.01)

    except KeyboardInterrupt:
        network.server.stop()
        curses.endwin()
        sys.exit()

network = net.Net()
print(curses.wrapper(main, network))
