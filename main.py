# Joseph Marsh
import tcod
import sys
import os

from engine import Engine
from entity import Entity
from game_map import GameMap
from input_handlers import EventHandler

#append the path to the currently executed python file 
os.environ["path"] = os.path.dirname(sys.executable) + ";" + os.environ["path"]

DATA_FOLDER = 'data'
FONT_FOLDER = 'data\\font'


def main() -> None:
    screen_width = 80
    screen_height = 50

    map_width = 80
    map_height = 45

    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    tileset = tcod.tileset.load_tilesheet(
        os.path.join(FONT_FOLDER, "dejavu10x10_gs_tc.png"), 32, 8, tcod.tileset.CHARMAP_TCOD 
    )

    event_handler = EventHandler()

    player = Entity(int(screen_width / 2), int(screen_height / 2), "@", (50, 255, 50))
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), "g", (255, 255, 0))
    entities = {npc, player}

    game_map = GameMap(map_width, map_height )

    engine = Engine(entities = entities, event_handler = event_handler, game_map = game_map, player = player )

    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset = tileset,
        title = "RogueLike Tuts are the best tuts!",
        vsync = False,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order = "F")
        
        while True:
            engine.render(console = root_console, context = context)

            events = tcod.event.wait()

            engine.handle_events(events)

if __name__ == "__main__":
    main()
