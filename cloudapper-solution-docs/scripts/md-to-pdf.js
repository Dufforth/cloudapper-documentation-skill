// Markdown (with mermaid blocks) -> A4 PDF, using headless Chromium via Playwright.
// Usage: node md-to-pdf.js <input.md> <output.pdf>
// Env (optional):
//   PW_PATH     path to the playwright package if `require('playwright')` fails
//   CHROME_EXE  path to a chromium / chrome-headless-shell binary
//   SHOT_DIR    also save each rendered diagram as diagramN.png in this folder (for checking)
//   SKIP_PDF=1  only render diagrams, don't write the PDF
const path = require('path'), fs = require('fs'), url = require('url');
const { chromium } = require(process.env.PW_PATH || 'playwright');

const [mdPath, out] = process.argv.slice(2);
if (!mdPath || !out) { console.error('usage: node md-to-pdf.js <input.md> <output.pdf>'); process.exit(1); }
const md = fs.readFileSync(mdPath, 'utf8');
const title = ((md.match(/^#\s+(.+)$/m) || [])[1] || path.basename(mdPath, '.md')).replace(/[<>&]/g, '');
// The temp HTML sits next to the Markdown so relative image paths resolve.
const tmpHtml = path.join(path.dirname(mdPath), '__render_tmp.html');

const html = `<!doctype html><html><head><meta charset="utf-8"><title>${title}</title>
<style>
 body{font-family:"Segoe UI",Arial,sans-serif;font-size:10.5pt;line-height:1.45;color:#1f2933;margin:0;padding:0 4px}
 h1{font-size:22pt;color:#0b4f71;border-bottom:3px solid #0b6e99;padding-bottom:6px}
 h2{font-size:16pt;color:#0b4f71;border-bottom:1px solid #cfd8dc;padding-bottom:4px;margin-top:26px;page-break-after:avoid}
 h3{font-size:12.5pt;color:#0b6e99;margin-top:18px;page-break-after:avoid}
 table{border-collapse:collapse;width:100%;margin:8px 0 14px;font-size:9pt;page-break-inside:auto}
 tr{page-break-inside:avoid}
 th,td{border:1px solid #cfd8dc;padding:4px 6px;vertical-align:top;text-align:left}
 th{background:#e8f1f6}
 code{background:#f1f4f6;padding:1px 4px;border-radius:3px;font-size:9pt}
 blockquote{border-left:4px solid #f0a020;background:#fff8e6;margin:10px 0;padding:6px 12px}
 img{max-width:100%;border:1px solid #d5dde2;border-radius:4px;margin:6px 0;page-break-inside:avoid}
 td img{max-width:340px}
 .mermaid{text-align:center;margin:10px 0;page-break-inside:avoid}
 hr{border:0;border-top:1px solid #e0e6ea;margin:18px 0}
 a{color:#0b6e99;text-decoration:none}
</style>
<script src="https://cdn.jsdelivr.net/npm/marked@12.0.2/marked.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/mermaid@10.9.1/dist/mermaid.min.js"></script>
</head><body><div id="c"></div>
<script id="src" type="text/markdown">${md.split('</' + 'script>').join('<' + '\\/script>')}</script>
<script>
 document.getElementById('c').innerHTML = marked.parse(document.getElementById('src').textContent);
 document.querySelectorAll('code.language-mermaid').forEach(c=>{const d=document.createElement('div');d.className='mermaid';d.textContent=c.textContent;c.parentElement.replaceWith(d);});
 mermaid.initialize({startOnLoad:false, theme:'default', securityLevel:'loose', flowchart:{useMaxWidth:true}});
 mermaid.run({querySelector:'.mermaid'}).then(()=>{window.__done=true}).catch(e=>{window.__err=String(e);window.__done=true});
</script></body></html>`;
fs.writeFileSync(tmpHtml, html);

(async () => {
  const b = await chromium.launch(process.env.CHROME_EXE ? { executablePath: process.env.CHROME_EXE } : {});
  try {
    const p = await b.newPage();
    await p.goto(url.pathToFileURL(tmpHtml).href);
    await p.waitForFunction(() => window.__done === true, null, { timeout: 60000 });
    // networkidle is unreliable with CDN scripts; wait for images instead.
    await p.waitForFunction(() => [...document.images].every(i => i.complete), null, { timeout: 60000 });
    const err = await p.evaluate(() => window.__err);
    const n = await p.evaluate(() => document.querySelectorAll('.mermaid svg').length);
    console.log('images:', await p.evaluate(() => [...document.images].length + ' total, ' + [...document.images].filter(i => !i.naturalWidth).length + ' broken'));
    console.log('diagrams rendered:', n, 'error:', err || 'none');

    if (process.env.SHOT_DIR) {
      // A4 width at 96 dpi, so the screenshots show the size the reader will see.
      await p.emulateMedia({ media: 'print' });
      await p.setViewportSize({ width: 794, height: 1123 });
      const els = await p.$$('.mermaid');
      for (let i = 0; i < els.length; i++) await els[i].screenshot({ path: path.join(process.env.SHOT_DIR, `diagram${i}.png`) });
    }
    if (!process.env.SKIP_PDF) {
      await p.pdf({ path: out, format: 'A4', printBackground: true, margin: { top: '16mm', bottom: '16mm', left: '14mm', right: '14mm' },
        displayHeaderFooter: true, headerTemplate: '<div></div>',
        footerTemplate: `<div style="font-size:8px;width:100%;text-align:center;color:#888">${title} · page <span class="pageNumber"></span> of <span class="totalPages"></span></div>` });
      console.log('pdf:', out);
    }
  } finally {
    await b.close();
    fs.unlinkSync(tmpHtml);
  }
})().catch(e => { console.error(e); process.exit(1); });
