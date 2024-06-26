# Joseph Marsh
from typing import Optional
import tcod.event

from .actions import Action, EscapeAction, MovementAction 

class EventHandler(tcod.event.EventDispatch[Action]):
    
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()
    
    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None

        key = event.sym

        if key == tcod.event.K_UP:
            action = MovementAction( dx = 0, dy = -1)
        elif key == tcod.event.K_DOWN:
            action = MovementAction(dx = 0, dy = 1)
        elif key == tcod.event.K_LEFT:
            action = MovementAction(dx = -1, dy = 0)
        elif key == tcod.event.K_RIGHT:
            action = MovementAction(dx = 1, dy = 0)

        elif key == tcod.event.K_ESCAPE:
            action = EscapeAction()

        # No valid key was pressed
        return action



"""
def handle_keys(key):
    #movment keys
    if key.vk == libtcod.KEY_UP:
        return {"move": ( 0, -1 ) }
    elif key.vk == libtcod.KEY_DOWN:
        return {"move": ( 0, 1 ) }
    elif key.vk == libtcod.KEY_LEFT:
        return {"move": ( -1, 0 ) }
    elif key.vk == libtcod.KEY_RIGHT:
        return {"move": ( 1, 0 ) }

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        #Alt + Etner toggles full screen 
        return  { "fullScreen": True }

    elif key.vk == libtcod.KEY_ESCAPE:
        # Exit app 
        return { "exit" : True }

    #return empty 
    return {}
"""