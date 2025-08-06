from setuptools import setup, find_packages

setup(
    name="femtoai-sphinx-theme",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'femtoai_sphinx_theme': [
            'theme.conf',
            'theme.toml',
            '*.html',
            'static/css/*.css',
            'static/images/*.svg',
        ],
    },
    entry_points={
        "sphinx.html_themes": [
            "femtoai_sphinx_theme = femtoai_sphinx_theme",
        ]
    },
    install_requires=["sphinx_rtd_theme"],
)
