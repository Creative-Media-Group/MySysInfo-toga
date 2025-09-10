import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from mylocale.TR import TR
import locale
import platform as p
import os

platform = toga.platform.current_platform
architecture = p.architecture()
architecture, _ = architecture
processor = p.processor()
version = p.version()
node = p.node()
machine = p.machine()
release = p.release()
username = str(os.getenv("USER"))
print(processor)


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
        tr = TR(langcode=lang, csv_file=file)
        # main_box = toga.Box()
        device = toga.Box(
            children=[
                toga.Table(
                    headings=[
                        tr.tr(target_key="PARAMETER", langcode=lang),
                        tr.tr(target_key="VALUE", langcode=lang),
                    ],
                    data=[
                        (
                            tr.tr(target_key="USERNAME", langcode=lang),
                            username,
                        ),
                        (
                            tr.tr(target_key="SYSTEM", langcode=lang),
                            platform,
                        ),
                        (
                            tr(target_key="PROCESSORTYPE", langcode=lang),
                            processor,
                        ),
                        (
                            tr.tr(target_key="ARCHITECTURE", langcode=lang),
                            architecture,
                        ),
                        (
                            tr.tr(target_key="VERSION", langcode=lang),
                            version,
                        ),
                    ],
                )
            ]
        )
        about = toga.Box(children=[toga.Label("Page 2")])

        container = toga.OptionContainer(
            content=[
                (tr.tr(target_key="DEVICE", langcode=lang), device),
                (tr.tr(target_key="ABOUT", langcode=lang), about),
            ]
        )
        device.style.direction = "column"
        about.style.direction = "column"
        container.current_tab = 0
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = container  # main_box
        self.main_window.show()


def main():
    return MySysInfotoga()
