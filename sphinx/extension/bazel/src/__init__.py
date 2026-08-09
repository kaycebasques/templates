from docutils import nodes
from docutils.parsers.rst import Directive


class HelloDirective(Directive):
    def run(self):
        paragraph_node = nodes.paragraph(text="Hello from the extension!")
        return [paragraph_node]


def setup(app):
    app.add_directive("hello", HelloDirective)
    return {
        "version": "0.0.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
