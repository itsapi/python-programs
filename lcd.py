from subprocess import check_output
import pifacecad
import time
import sys


cmd = lambda c: check_output(c, shell=True).decode('utf-8')
menu = [
    ['ip', "hostname -I"],
    ['uptime', "uptime|sed 's/.*up  \\([^,]*\\),.*/\\1/'"],
    ['temp', "vcgencmd measure_temp|sed 's/[a-z]*=//g'"],
    ['cpu', "top -bn1|awk 'NR>7{s+=$9}END{print s}'"],
    ['memuse', "free -h|grep Mem|awk '{print$3}'"],
    ['memtot', "free -h|grep Mem|awk '{print$2}'"],
    ['diskuse', "df -h|grep /dev/root|awk '{print$3}'"],
    ['disktot', "df -h|grep /dev/root|awk '{print$2}'"]
]


def update(e=None):
    if e:
        if e.timestamp < cad.time + 1:
            return False
        cad.time = e.timestamp
        cad.sel += {5: 0, 6: -1, 7: 1}[e.pin_num]

    menu_item = menu[cad.sel%len(menu)]
    result = cmd(menu_item[1])

    cad.lcd.clear()
    cad.lcd.write('{}\n{}'.format(menu_item[0], result))


def exit(e=None):
    if e:
        cad.exit = 1
    else:
        listener.deactivate()
        cad.lcd.clear()
        cad.lcd.backlight_off()
        cad.lcd.display_off()
        sys.exit()


if __name__ == "__main__":
    cad = pifacecad.PiFaceCAD()
    cad.lcd.blink_off()
    cad.lcd.cursor_off()
    cad.lcd.backlight_on()
    cad.sel = 0
    cad.time = 0
    cad.exit = 0

    listener = pifacecad.SwitchEventListener(chip=cad)
    for pin in range(5, 8):
        listener.register(pin, pifacecad.IODIR_RISING_EDGE, update)
    listener.register(4, pifacecad.IODIR_RISING_EDGE, exit)
    listener.activate()

    update()

    try:
        while not cad.exit:
            pass
    except KeyboardInterrupt:
        pass
    finally:
        exit()
