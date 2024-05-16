import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from mylocale.TR import tr
import locale

platform = toga.platform.current_platform


class MySysInfotoga(toga.App):
    def startup(self):
        file = f"{self.paths.app.absolute()}/resources/localisation.csv"
        if platform == "android":
            lang = str(
                self._impl.native.getResources().getConfiguration().getLocales().get(0)
            )

        else:
            lang = locale.getlocale()
            lang, _ = lang
        textbox = toga.Label(
            text=f"{tr(csv_file=file, target_key='HELLOWORLD', langcode=lang)}, {lang}"
        )
        main_box = toga.Box()
        processor = toga.Box()
        about = toga.Box()

        container = toga.OptionContainer(
            content=[("Processor", processor), ("About", about)]
        )
        container.current_tab = 0
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = container  # main_box
        self.main_window.show()


def main():
    return MySysInfotoga()
