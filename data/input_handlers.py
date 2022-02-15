# Joseph Marsh
import tcod as libtcod

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