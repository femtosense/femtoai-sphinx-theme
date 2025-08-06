from sphinx.util import logging
import os

logger = logging.getLogger(__name__)

def setup(app):
    theme_name = "femtoai_sphinx_theme"
    theme_path = os.path.abspath(os.path.dirname(__file__))

    # Always add the theme explicitly
    app.add_html_theme(theme_name, theme_path)
    app.add_css_file("css/custom.css")
    logger.info("Registered FemtoAI Sphinx Theme")

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
