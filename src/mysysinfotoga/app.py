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
        main_box = toga.Box()
        device = toga.Box(children=[toga.Label("Page 1")])
        about = toga.Box(children=[toga.Label("Page 2")])

        container = toga.OptionContainer(
            content=[
                (tr(csv_file=file, target_key="DEVICE", langcode=lang), device),
                (tr(csv_file=file, target_key="ABOUT", langcode=lang), about),
            ]
        )
        container.current_tab = 0
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = container  # main_box
        self.main_window.show()


def main():
    return MySysInfotoga()
