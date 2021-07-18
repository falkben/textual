from rich.markdown import Markdown

from textual import events
from textual.app import App
from textual.widgets import Header, Footer, Placeholder, ScrollView


class MyApp(App):
    """An example of a very simple Textual App"""

    async def on_load(self, event: events.Load) -> None:
        await self.bind("b", "view.toggle('sidebar')", "Toggle sidebar")
        await self.bind("q", "quit", "Quit")

    async def on_startup(self, event: events.Startup) -> None:

        body = ScrollView()

        await self.view.dock(Header(), edge="top")
        await self.view.dock(Footer(), edge="bottom")
        await self.view.dock(Placeholder(), edge="left", size=30, name="sidebar")
        await self.view.dock(body, edge="right")

        async def get_markdown(filename: str) -> None:
            with open(filename, "rt") as fh:
                readme = Markdown(fh.read(), hyperlinks=True)
            await body.update(readme)

        await self.call_later(get_markdown, "richreadme.md")


MyApp.run(title="Simple App", log="textual.log")
