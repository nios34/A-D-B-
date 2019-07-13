from time import sleep

from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import ManagedScreen, Screen

import Command

def demo():
    with ManagedScreen() as screen:
        Command.Start_PREPAR(screen)
        Command.Start_CHECK(screen)
        Command.Wait_for_DEVICE(screen)

        screen.clear()
        screen.refresh()

        Command.Main_menu(screen)
        pass

demo()
