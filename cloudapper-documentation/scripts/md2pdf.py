"""Convert Markdown reports to styled PDFs via headless Chrome.

Usage: python md2pdf.py <file.md> [<file.md> ...]
"""
import re
import subprocess
import sys
import tempfile
from pathlib import Path

import markdown

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
PROFILE = Path(tempfile.gettempdir()) / "md2pdf-chrome-profile"

CSS = """
@page { size: A4; margin: 16mm 14mm 18mm 14mm; }
body { font-family: "Segoe UI", Arial, sans-serif; font-size: 10pt; line-height: 1.45; color: #1f2933; }
h1 { font-size: 20pt; color: #0b3d91; border-bottom: 3px solid #0b3d91; padding-bottom: 6px; margin-top: 0; }
h2 { font-size: 14pt; color: #0b3d91; border-bottom: 1px solid #c9d3e0; padding-bottom: 3px; margin-top: 22px; break-after: avoid; }
h3 { font-size: 11.5pt; color: #12355b; margin-top: 16px; break-after: avoid; }
h4 { font-size: 10.5pt; color: #12355b; break-after: avoid; }
p, li { orphans: 3; widows: 3; }
table { border-collapse: collapse; width: 100%; margin: 8px 0 12px; font-size: 8.6pt; }
th { background: #0b3d91; color: #fff; text-align: left; padding: 5px 6px; }
td { border: 1px solid #d5dce6; padding: 4px 6px; vertical-align: top; }
tr:nth-child(even) td { background: #f5f8fc; }
tr { break-inside: avoid; }
code { font-family: Consolas, monospace; font-size: 8.6pt; background: #eef2f7; padding: 1px 3px; border-radius: 3px; word-break: break-all; }
a { color: #0b5cd5; text-decoration: none; }
hr { border: none; border-top: 1px solid #c9d3e0; margin: 18px 0; }
ul { padding-left: 18px; }
"""

MD_LINK_TARGET = re.compile(r"\(([\w.-]+)\.md(#[^)]*)?\)")
MD_LINK_TEXT = re.compile(r"\[([\w.-]+)\.md\]")
BUG_ID = re.compile(r"BUG-(\d\d)")
NB_HYPHEN = "\u2011"


def convert(md_path: Path) -> Path:
    text = md_path.read_text(encoding="utf-8")
    # Cross-links between the reports point at the PDF versions.
    text = MD_LINK_TARGET.sub(lambda m: f"({m.group(1)}.pdf{m.group(2) or ''})", text)
    text = MD_LINK_TEXT.sub(lambda m: f"[{m.group(1)}.pdf]", text)
    body = markdown.markdown(text, extensions=["tables", "fenced_code", "toc", "sane_lists"])
    # Keep bug IDs on one line in narrow table cells.
    body = BUG_ID.sub(lambda m: f"BUG{NB_HYPHEN}{m.group(1)}", body)
    title = md_path.stem.replace("-", " ")
    html = f"<!doctype html><html><head><meta charset='utf-8'><title>{title}</title><style>{CSS}</style></head><body>{body}</body></html>"
    html_path = md_path.resolve().with_suffix(".print.html")
    html_path.write_text(html, encoding="utf-8")
    pdf_path = md_path.resolve().with_suffix(".pdf")
    subprocess.run([
        CHROME, "--headless=new", "--disable-gpu", f"--user-data-dir={PROFILE}", "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path}", html_path.as_uri(),
    ], check=True, capture_output=True)
    html_path.unlink()
    return pdf_path


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        print(convert(Path(arg)))
