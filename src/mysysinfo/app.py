import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from mysysinfo.translation import translate
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
        file = f"{str(self.paths.app.absolute())}/localisations"
        print(file)
        if platform == "android":
            lang = str(
                self._impl.native.getResources().getConfiguration().getLocales().get(0)
            )

        else:
            lang = locale.getlocale()
            lang, _ = lang
        # main_box = toga.Box()
        device = toga.Box(
            children=[
                toga.Table(
                    headings=[
                        translate(
                            folder=file, key="PARAMETER", lang=lang
                        ),  # tr.tr(target_key="PARAMETER", langcode=lang),
                        translate(folder=file, key="VALUE", lang=lang),
                    ],
                    data=[
                        (
                            translate(
                                folder=file, key="USERNAME", lang=lang
                            ),  # tr.tr(target_key="USERNAME", langcode=lang),
                            username,
                        ),
                        (
                            translate(
                                folder=file, key="SYSTEM", lang=lang
                            ),  # tr.tr(target_key="SYSTEM", langcode=lang),
                            platform,
                        ),
                        (
                            translate(
                                folder=file, key="PROCESSORTYPE", lang=lang
                            ),  # tr(target_key="PROCESSORTYPE", langcode=lang),
                            processor,
                        ),
                        (
                            translate(
                                folder=file, key="ARCHITECTURE", lang=lang
                            ),  # tr.tr(target_key="ARCHITECTURE", langcode=lang),
                            architecture,
                        ),
                        (
                            translate(
                                folder=file, key="VERSION", lang=lang
                            ),  # tr.tr(target_key="VERSION", langcode=lang),
                            version,
                        ),
                    ],
                )
            ]
        )
        about = toga.Box(children=[toga.Label("Page 2")])

        container = toga.OptionContainer(
            content=[
                (
                    translate(folder=file, key="DEVICE", lang=lang),
                    device,
                ),  # tr.tr(target_key="DEVICE", langcode=lang),
                (
                    translate(folder=file, key="ABOUT", lang=lang),
                    about,
                ),  # tr.tr(target_key="ABOUT", langcode=lang),
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
