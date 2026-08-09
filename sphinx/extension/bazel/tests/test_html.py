import unittest
from harness import SphinxTestBase


class TestHtml(SphinxTestBase):
    def test_title_and_extension(self):
        outdir = self.build_docs(
            conf_content="""
                project = "test_title"
                extensions = ["src"]
            """,
            index_content="""
                ==========
                test_title
                ==========

                .. hello::
            """
        )
        html = (outdir / "index.html").read_text()
        self.assertIn("test_title", html)
        self.assertIn("Hello from the extension!", html)


if __name__ == "__main__":
    unittest.main()
