#!/usr/bin/python3
import argparse
import dbus
import fontawesome as fa
pp = ''
song = ''
artist = ''

parser = argparse.ArgumentParser()
parser.add_argument('-l',
        '--length',
        type=int)

parser.add_argument('-f',
        '--format',
        type=str,
        metavar='custom format',
        dest='custom_format',
        default=f'{pp} {song}:{artist}')

parser.add_argument('-q',
        '--quite',
        type=bool,
        default=False)

args = parser.parse_args()

def trim(display, length):
    if len(display) > length:
        display = display[:length]
        display += '...'
        if ('(' in display) and (')' not in display):
            display += ')'
    return display

length = args.length

try:
    session_bus = dbus.SessionBus()
    spotify = session_bus.get_object('org.mpris.MediaPlayer2.spotify','/org/mpris/MediaPlayer2')
    properties = dbus.Interface(spotify,'org.mpris.MediaPlayer2.Player')
    metadata = properties.Get('org.mpris.MediaPlayer2.spotify', 'metadata')
    state = properties.get('org.mpris.MediaPlayer2.spotify', 'PlaybackStatus')
    print(session_bus)
    if state == 'Playing':
        print('playing')
        pp = fa.icon['play']
    elif state == 'Paused':
        pp = fa.icon['pause']
    else:
        pp = ''


    artist = fix_string(metadata['xesam:artist'][0]) if metadata['xesam:artist'] else ''
    song = fix_string(metadata['xesam:title']) if metadata['xesam:title'] else ''
    album = fix_string(metadata['xesam:album']) if metadata['xesam:album'] else ''

    if (quiet and state == 'Paused') or (not artist and not song and not album):
        print('')
    else:
        print(trim(args.format, trunclen + 4))

except Exception as e:
    if isinstance(e, dbus.exceptions.DBusException):
        print('')
    else:
        print(e)
