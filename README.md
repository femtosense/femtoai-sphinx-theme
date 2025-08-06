# femtoAI Sphinx Theme

A custom Sphinx theme for femtoAI documentation, styled to match the femtoAI brand guidelines.

## ✨ Features

- Integrated femtoAI brand palette
- Custom sidebar with logo and return button
- Styled admonitions using Spark and Pulse
- Favicon and typography overrides
- Ready for use in internal and public documentation

---

## 🛠 Local Development

### 1. Clone the Repository

```bash
git clone https://github.com/femtosense/femtoai-sphinx-theme.git
cd femtoai-sphinx-theme
```

### 2. Create and Activate a Conda Environment

```bash
conda create -n femtoai-theme python=3.11
conda activate femtoai-theme
```

### 3. Install Dependencies

If you have a pyproject.toml or setup.py:
```bash
pip install -e .
```
This installs the theme in “editable” mode so changes apply live when developing.

### 4. Use in your project

Update `conf.py` in your project to use the theme:
```python
html_theme = "femtoai_sphinx_theme"

# Optional static path if you want to include custom.css
html_static_path = ["_static"]
html_css_files = ["css/custom.css"]
```

Clean build foler and build the docs
```bash
cd [your project directory]
make clean && make html
open _build/html/index.html
```

---

## 🚀 Deployment / Usage in Other Projects

### Install via Git

In your target Sphinx project:
```bash
pip install git+https://github.com/femtosense/femtoai-sphinx-theme.git
```

Then in `conf.py`:
```python
html_theme = "femtoai_sphinx_theme"

# Optional static path if you want to include custom.css
html_static_path = ["_static"]
html_css_files = ["css/custom.css"]
```

---

## 👀 Customization

* Modify `layout.html` for layout tweaks (sidebar, logo, footer, etc.)
* Edit `custom.css` in `_static/css/` to match updated brand styles
* Add additional templates to override Sphinx components

⸻

## 🧪 Testing Tips

* Run make clean html inside the example project to verify updates
* Use Read the Docs builds or a CI pipeline to validate packaging