import unittest
import tempfile
import pathlib
import socket
import subprocess
import time
import sys
import textwrap
from contextlib import contextmanager

# from playwright.sync_api import sync_playwright
from sphinx.application import Sphinx

class SphinxTestBase(unittest.TestCase):
    """Base class for Sphinx theme and extension tests.

    Handles temporary directories, free port selection, and HTTP server lifecycle.
    """
    @classmethod
    def setUpClass(cls):
        cls.temp_dir = tempfile.TemporaryDirectory()
        cls.tmp_path = pathlib.Path(cls.temp_dir.name)
        cls.server_proc = None
        # Find a free port
        with socket.socket() as s:
            s.bind(("", 0))
            cls.port = s.getsockname()[1]

    @classmethod
    def tearDownClass(cls):
        if cls.server_proc:
            cls.server_proc.terminate()
            cls.server_proc.wait()
        cls.temp_dir.cleanup()

    def build_docs(self, conf_content, index_content):
        """Builds Sphinx documentation in the temp directory."""
        srcdir = self.tmp_path
        (srcdir / "conf.py").write_text(textwrap.dedent(conf_content))
        (srcdir / "index.rst").write_text(textwrap.dedent(index_content))
        outdir = self.tmp_path / "out"
        if not outdir.exists():
            outdir.mkdir()
        doctreedir = self.tmp_path / "doctrees"
        if not doctreedir.exists():
            doctreedir.mkdir()
        app = Sphinx(str(srcdir), str(srcdir), str(outdir), str(doctreedir), "html")
        app.build()
        return outdir

    def start_server(self, directory):
        """Starts the HTTP server serving the specified directory."""
        self.__class__.server_proc = subprocess.Popen(
            [sys.executable, "-m", "http.server", str(self.port), "--directory", str(directory)],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        time.sleep(1)
        return f"http://localhost:{self.port}"

    # @contextmanager
    # def run_playwright(self):
    #     """Context manager to run Playwright and yield a page object."""
    #     with sync_playwright() as p:
    #         browser = p.chromium.launch()
    #         page = browser.new_page()
    #         try:
    #             yield page
    #         finally:
    #             browser.close()
