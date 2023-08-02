import pygame as py
import pygame.freetype as py_freetype

from gamescene import GameScene


def main(width, height, fps):
    py.init()
    py_freetype.init()
    screen = py.display.set_mode((width, height))
    py.display.set_caption("Rat Chronicles Based Adventure DLC Part 2")
    clock = py.time.Clock()

    # Assigns each game scene to an index.
    scene_ids = {
        0: GameScene,
    }
    active_scene = scene_ids[0]()

    # Game loop
    quit_attempt = False
    while not quit_attempt:
        pressed_keys = py.key.get_pressed()
        pressed_mouse = py.mouse.get_pressed(3)

        # Event filtering
        filtered_events = []
        for event in py.event.get():
            if event.type == py.QUIT:
                quit_attempt = True
            elif event.type == py.KEYDOWN:
                alt_pressed = pressed_keys[py.K_LALT] \
                                or pressed_keys[py.K_RALT]
                if event.key == py.K_ESCAPE \
                    or event.key == py.K_F4 and alt_pressed:
                    quit_attempt = True
            
            if not quit_attempt:
                filtered_events.append(event)

        # Update active scene
        active_scene.process_input(filtered_events, pressed_keys, pressed_mouse)
        active_scene.update()
        active_scene.render(screen)

        # Update display
        py.display.flip()
        clock.tick(fps)

    # Cleanup
    active_scene.terminate()


if __name__ == "__main__":
    main(640, 480, 60)
