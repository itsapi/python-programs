import sys
import os


if len(sys.argv) == 4 and sys.argv[2] == '-v':
    type = 'vid'
    ext = 'h264'
    opt = '-t {}'.format(sys.argv[3])
    run = 'mplayer'
elif len(sys.argv) == 2:
    type = 'still'
    ext = 'jpg'
    opt = ''
    run = 'xdg-open'
else:
    print('Usage: python remoteCapture.py user@host [-v length]')
    sys.exit()

os.system('ssh {host} raspi{type} -o {type}.{ext};\
           scp {host}:~/{type}.{ext} .;\
           {run} {type}.{ext}'
          .format(host=sys.argv[1], type=type, ext=ext, run=run, opt=opt)
)
