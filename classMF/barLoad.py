import time
from prompt_toolkit.output import ColorDepth
from prompt_toolkit.shortcuts import ProgressBar
from prompt_toolkit.shortcuts.progress_bar import formatters
from prompt_toolkit.shortcuts.prompt import confirm


def BarM1(): #Barra de carregamento rápida
    color_depth = ColorDepth.DEPTH_24_BIT
    custom_formatters = [
        formatters.Label(),
        formatters.Text(" "),
        formatters.Rainbow(formatters.Bar()),
        formatters.Text(" left: "),
        formatters.Rainbow(formatters.TimeLeft()),
    ]
    with ProgressBar(formatters=custom_formatters, color_depth=color_depth) as pb:
        for i in pb(range(20),label="Inicializando..."):
            time.sleep(0.2)