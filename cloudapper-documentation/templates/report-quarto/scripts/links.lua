-- Point cross-report links at the file type being produced (PDF links to PDFs, HTML to HTML).
function Link(el)
  if quarto.doc.is_format("typst") then
    el.target = el.target:gsub("%.qmd", ".pdf")
  elseif quarto.doc.is_format("html") then
    el.target = el.target:gsub("%.qmd", ".html")
  end
  return el
end
