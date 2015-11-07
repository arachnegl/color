"""
Give the command line some color::

    >>> from color import color
    >>> print(color.blue('Hello Blue World'))
    Hello Blue World  # in Blue ;)

'\x1b[;31mhi\x1b[00m'
"""
ESC = '\x1b'
pre = '{}['.format(ESC)
suf = '{}[0m'.format(ESC)  # '0' is reset

colors = {color: i for i, color in enumerate((
    'black', 'red', 'green', 'yellow',
    'blue', 'magenta', 'cyan', 'white'  # No more colors after 8
))}

options = {
    'none': '0',
    'bold': '1',
    'underscore': '4',
    'blink': '5',
    'reverse': '7',
    'conceal': '8'  # ??
}

effects = {
    'normal': '3',
    'background': '4',
    'high_intensity': '9',
}


def print_all(msg):
    _all = [
        (o, e, c)
        for o in options.values()
        for e in effects.values()
        for c in colors.values()
    ]

    def render(message, opt, eff, col):
        global pre, suf
        return '{pre}{opt};{eff}{col}m{message}{suf}'.format(
            pre=pre, suf=suf, opt=opt, eff=eff, col=col, message=message)

    for args in _all:
        print(render(msg, *args))


#foreground = dict((colors[x], '3%s' % x) for x in range(8))
#background = dict((colors[x], '4%s' % x) for x in range(8))


def get_color_func(color_number):
    fmt = '{pre};3{}m{{}}{suf}'.format(color_number, pre=pre, suf=suf)
    def color(msg):
        return fmt.format(msg)
    return color

color_mthds = {color: get_color_func(i) for i, color in enumerate(colors)}

color = type('color', (object,), color_mthds)

fg = type('fg', (object,), {'a': 'a'})
color.fg = color.foreground = fg
bg = type('bg', (object,), {'a': 'a'})
color.bg = color.background = bg


# Reset
Color_Off='\e[0m'       # Text Reset

# Regular Colors
Black='\e[0;30m'        # Black
Red='\e[0;31m'          # Red
Green='\e[0;32m'        # Green
Yellow='\e[0;33m'       # Yellow
Blue='\e[0;34m'         # Blue
Purple='\e[0;35m'       # Purple
Cyan='\e[0;36m'         # Cyan
White='\e[0;37m'        # White

# Bold
BBlack='\e[1;30m'       # Black
BRed='\e[1;31m'         # Red
BGreen='\e[1;32m'       # Green
BYellow='\e[1;33m'      # Yellow
BBlue='\e[1;34m'        # Blue
BPurple='\e[1;35m'      # Purple
BCyan='\e[1;36m'        # Cyan
BWhite='\e[1;37m'       # White

# Underline
UBlack='\e[4;30m'       # Black
URed='\e[4;31m'         # Red
UGreen='\e[4;32m'       # Green
UYellow='\e[4;33m'      # Yellow
UBlue='\e[4;34m'        # Blue
UPurple='\e[4;35m'      # Purple
UCyan='\e[4;36m'        # Cyan
UWhite='\e[4;37m'       # White

# Background
On_Black='\e[40m'       # Black
On_Red='\e[41m'         # Red
On_Green='\e[42m'       # Green
On_Yellow='\e[43m'      # Yellow
On_Blue='\e[44m'        # Blue
On_Purple='\e[45m'      # Purple
On_Cyan='\e[46m'        # Cyan
On_White='\e[47m'       # White

# High Intensity
IBlack='\e[0;90m'       # Black
IRed='\e[0;91m'         # Red
IGreen='\e[0;92m'       # Green
IYellow='\e[0;93m'      # Yellow
IBlue='\e[0;94m'        # Blue
IPurple='\e[0;95m'      # Purple
ICyan='\e[0;96m'        # Cyan
IWhite='\e[0;97m'       # White

# Bold High Intensity
BIBlack='\e[1;90m'      # Black
BIRed='\e[1;91m'        # Red
BIGreen='\e[1;92m'      # Green
BIYellow='\e[1;93m'     # Yellow
BIBlue='\e[1;94m'       # Blue
BIPurple='\e[1;95m'     # Purple
BICyan='\e[1;96m'       # Cyan
BIWhite='\e[1;97m'      # White

# High Intensity backgrounds
On_IBlack='\e[0;100m'   # Black
On_IRed='\e[0;101m'     # Red
On_IGreen='\e[0;102m'   # Green
On_IYellow='\e[0;103m'  # Yellow
On_IBlue='\e[0;104m'    # Blue
On_IPurple='\e[0;105m'  # Purple
On_ICyan='\e[0;106m'    # Cyan
On_IWhite='\e[0;107m'   # White
