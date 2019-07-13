from INFO import TTY_SIZE

A_BOLD = 1
A_NORMAL = 2
A_REVERSE = 3
A_UNDERLINE = 4

COLOUR_BLACK = 0
COLOUR_RED = 1
COLOUR_GREEN = 2
COLOUR_YELLOW = 3
COLOUR_BLUE = 4
COLOUR_MAGENTA = 5
COLOUR_CYAN = 6
COLOUR_WHITE = 7

W = int(TTY_SIZE['width']/2)

def Print_at_Center(obj, DPTEXT, H, color = 7, attr = 0, bg = 0, transparent = False):
    minus = W - int(len(DPTEXT)/2)
    obj.print_at(DPTEXT, minus, H, color, attr, bg ,transparent)
    pass

def Print_at_Center_WITH_W(obj, DPTEXT, CW, H, color = 7, attr = 0, bg = 0, transparent = False):
    minus = CW - int(len(DPTEXT)/2)
    obj.print_at(DPTEXT, minus, H, color, attr, bg ,transparent)
    pass

def Print_at(obj, TEXT, X, Y, color = 7, attr = 0, bg = 0, transparent = False):
    obj.print_at(TEXT, Y, X, color, attr, bg ,transparent)
    pass

def Del_line_down(obj, Down):
    for i in range(TTY_SIZE['height'] - Down):
        Print_at(obj, ' '*(TTY_SIZE['width'] + 1), Down + i, 0)
        pass
    pass

def Print_BOX_at(obj, sz):
    # sz = [[X1,Y1], [X2,Y2]]
    X1 = sz[0][0]
    X2 = sz[1][0]
    Y1 = sz[0][1]
    Y2 = sz[1][1]

    obj.move(X1, Y1)
    obj.draw(X2, Y1,char = u'─', thin = True)
    obj.move(X1, Y1)
    obj.draw(X1, Y2,char = u'│', thin = True)
    obj.move(X2, Y1)
    obj.draw(X2, Y2,char = u'│', thin = True)
    obj.draw(X1, Y2,char = u'─', thin = True)
    obj.print_at(u'┌', X1,Y1)
    obj.print_at(u'┐',X2,Y1)
    obj.print_at(u'└',X1,Y2)
    obj.print_at(u'┘',X2,Y2)

    pass