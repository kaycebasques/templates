import os


def setup(app):
    app.add_html_theme('theme', os.path.abspath(os.path.dirname(__file__)))
    return {
        'version': '0.0.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
