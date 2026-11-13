"""Bundle the two published PDFs and only the files needed to rebuild them."""

from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parent
FILES = (
    "cv-en.pdf",
    "cv-zh.pdf",
    "README.md",
    "Makefile",
    "package.py",
    "latex/cv-en.tex",
    "latex/cv-zh.tex",
    "latex/cv-style.sty",
    "latex/rubric.tex",
    "latex/publications.bib",
    "latex/photo.jpg",
)


if __name__ == "__main__":
    for name in FILES:
        if not (ROOT / name).is_file():
            raise FileNotFoundError(ROOT / name)
    with ZipFile(ROOT / "cv-bundle.zip", "w", ZIP_DEFLATED) as bundle:
        for name in FILES:
            bundle.write(ROOT / name, "cv/" + name)
    print("Created cv-bundle.zip (English/Chinese PDFs and LaTeX sources).")
