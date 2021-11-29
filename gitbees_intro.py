from rich.console import Console
from rich.layout import Layout, LayoutRender
from rich.panel import Panel

def Intro():
    c = Console()
    l = Layout()

    l.split_column(
        Layout(name="Gitbees", ratio=2),
    )

    l["Gitbees"].split_row(
        Layout(Panel("Author"), ratio=4),
        Layout(Panel("License"), ratio=3),
        Layout(Panel("GitHub"), ratio=3)
    )

    c.print("🐝 Gitbees 🐝")
    c.print(l)
    

Intro()