import omni.ext
import omni.ui as ui
from demo.core import LetsPrint
from pathlib import Path

# Any class derived from `omni.ext.IExt` in top level module (defined in `python.modules` of `extension.toml`) will be
# instantiated when extension gets enabled and `on_startup(ext_id)` will be called. Later when extension gets disabled
# on_shutdown() is called.
class DemoUi(omni.ext.IExt):
    def __init__(self):
        self._demoWindow = None

    # ext_id is current extension id. It can be used with extension manager to query additional information, like where
    # this extension is located on filesystem.
    def on_startup(self, ext_id):
        print("[omni.epgCustomUi] The epgTestUi on startup callback..")
        self.all_projects = None
        self.__currentPath = Path(__file__).parent
        self.__buttonIconPath = self.__currentPath.parent.parent.parent
        self._default_project_image = "{0}/data/extension_preview_image.png".format(self.__buttonIconPath)

        # Instantiating all the objects we might need.
        # Here we are just instantiating a class to help print when the button is pressed
        self._letsPrint = LetsPrint()
        self._window = self._create_window()

    def on_shutdown(self):
        print("[omni.epgCustomUi] The epgTestUi on shutdown callback..")
        self.destroy()

    def destroy(self):
        self._visiblity_changed_listener = None
        self._demoWindow = None

    def set_visible(self, value):
        self._demoWindow.visible = value

    def onButtonClick(self):
        self._letsPrint.delegatedPrint()

    def _create_window(self):
        # IMPORTANT: Remember to pass in the "flags=ui.WINDOW_FLAGS_MENU_BAR" kwarg if you want to display Menu Items
        if self._demoWindow is None:
            self._demoWindow = ui.Window("Variant Manager", width=800, height=500, padding_x=10, padding_y=10, flags=ui.WINDOW_FLAGS_MENU_BAR)
            self.set_visible(True)
        else:
            self.set_visible(True)

        # This is how you add Menus to your UI.
        with self._demoWindow.menu_bar:
            with ui.Menu("File"):
                ui.MenuItem("New")
                ui.MenuItem("Open")
                with ui.Menu("Open Recent"):
                    ui.MenuItem("myAwesomeScene.usd")
                    ui.MenuItem("anotherAwesomeScene.usd")
                    ui.MenuItem("yetAnotherAwesomeScene.usd")
                ui.MenuItem("Save")

        with self._demoWindow.frame:
            demoLabel = ui.Label("EPIGRAPH PROJECTS", height=30, style={"font_size": 50, "color": 0xFF000000})

            with ui.HStack():
                demoButton = ui.Button("I will print Something", image_url=self._default_project_image, clicked_fn=self.onButtonClick)
