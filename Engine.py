# Joseph Marsh
from html import entities
from pickle import FALSE
from re import S
from xml.dom.minidom import Entity
import tcod as libtcod 
import sys
import os
import glob

#append the path to the currently executed python file 
os.environ["path"] = os.path.dirname(sys.executable) + ";" + os.environ["path"]

#import key handelers
from data.input_handlers import handle_keys
from entity import Entity
from render_functions import clear_all, render_all

DATA_FOLDER = 'data'
FONT_FOLDER = 'data\\font'
FONT_FILE = os.path.join(FONT_FOLDER,"dejavu10x10_gs_tc.png")

def main():
    screen_width = 80
    screen_hight = 50

    #initialize player location
    player = Entity(int(screen_width / 2 ), int(screen_hight / 2 ), '@', libtcod.blue )
    npc = Entity(int(screen_width / 2 - 5 ), int(screen_hight / 2 ), 'g', libtcod.red )
    entities = [npc, player]

    #allows import font and allow changing color of font
    libtcod.console_set_custom_font( FONT_FILE, libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD )
    #set console dimentions and title for the console and set full screen to false 
    libtcod.console_init_root(screen_width, screen_hight, "Anubit Fire libtcod tutorial revised", False)
    #create a new console 
    con = libtcod.console_new(screen_width, screen_hight)

    key = libtcod.Key()
    mouse = libtcod.Mouse()

    #Keeps console open until player quits the game
    while not libtcod.console_is_window_closed ():
        #check for key or mouse press events
        libtcod.sys_check_for_event( libtcod.EVENT_KEY_PRESS, key, mouse )

        #set default forground color to white
        #libtcod.console_set_default_foreground( con, libtcod.white )
        #prints the innitial charactor for player position
        #libtcod.console_put_char( con, player.x, player.y, '@', libtcod.BKGND_NONE )
        #allow changing console before the next fram is rendered
        #libtcod.console_blit(con, 0, 0, screen_width, screen_hight, 0, 0, 0 )

        render_all(con, entities, screen_width, screen_hight)

        #display current frame
        libtcod.console_flush()
        
        #prints the innitial charactor for player position
        #libtcod.console_put_char( con, player.x, player.y, ' ', libtcod.BKGND_NONE )

        clear_all(con, entities)

        action = handle_keys(key)
        move = action.get("move")
        exit = action.get("exit")
        fullscreen = action.get("fullscreen")

        if move:
            dx, dy = move
            player.move(dx, dy)

        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen() )

        #exits app if player presses escape.
        if exit:
            return True

if __name__ == "__main__":
    main()
