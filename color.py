"""
'\x1b[;31mhi\x1b[00m'
"""
ESC = '\x1b'

pre = '{}['.format(ESC)
suf = '{}[0m'.format(ESC)  # '0' is reset

colors = (
    'black', 'red', 'green', 'yellow',
    'blue', 'magenta', 'cyan', 'white'
)

def get_color_func(color_number):

    fmt = '{pre};3{}m{{}}{suf}'.format(
        color_number, pre=pre, suf=suf
    )

    def color(msg):
        return fmt.format(msg)

    return color


colors = dict(
    ((color, get_color_func(i))
    for i, color in enumerate(colors))
)

color = type('color', (object,), colors)
