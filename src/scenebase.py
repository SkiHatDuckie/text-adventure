class SceneBase:
    def __init__(self):
        '''Interface for creating new game scenes.'''
        self.next = -1

    def process_input(self, events, pressed_keys, pressed_mouse):
        print("oh noes!, you didn't override this in the child class")

    def update(self):
        print("oh noes!, you didn't override this in the child class")

    def render(self, screen):
        print("oh noes!, you didn't override this in the child class")

    def switch_scene(self, scene_id):
        self.next = scene_id

    def terminate(self):
        self.switchToScene(None)
        print("app terminated")