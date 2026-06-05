import os


def setup(app):
    app.add_html_theme('theme', os.path.abspath(os.path.dirname(__file__)))
