import imgui
import os
from imgui.integrations.nx import NXRenderer

def main():
    renderer = NXRenderer()
    currentDir = os.getcwd()

    while True:
        renderer.handleinputs()

        imgui.new_frame()

        width, height = renderer.io.display_size
        imgui.set_next_window_size(width, height)
        imgui.set_next_window_position(0, 0)
        imgui.begin("",
            flags=imgui.WINDOW_NO_TITLE_BAR | imgui.WINDOW_NO_RESIZE | imgui.WINDOW_NO_MOVE | imgui.WINDOW_NO_SAVED_SETTINGS
        )
        imgui.text("Cool script!")
        imgui.text("Touch is supported")
        imgui.text("Current dir: " + os.getcwd())

        imgui.end()
        imgui.render()
        renderer.render()

    renderer.shutdown()


if __name__ == "__main__":
    main()
