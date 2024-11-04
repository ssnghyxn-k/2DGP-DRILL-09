from pico2d import *

from grass import Grass
from boy import Boy
import game_world

def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            boy.handle_event(event)


def reset_world():
    global running
    global boy

    running = True

    grass_1 = Grass(400, 50)
    game_world.add_object(grass_1, 0)# 영속 객체 -> world가 존재하는 한 계속 살아있는 객체

    boy = Boy()          # 영속 객체
    game_world.add_object(boy, 1)

    grass_2 = Grass(400, 30)
    game_world.add_object(grass_2, 1)




def update_world():
    game_world.update()

def render_world():
    clear_canvas()
    game_world.render()
    update_canvas()


open_canvas()
reset_world()
# game loop
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)
# finalization code
close_canvas()
