#let navy = rgb("#0b3d91")
#let muted = rgb("#6b7280")
#let rule = rgb("#d6dce5")

#set page(
  header: context [
    #set text(7.5pt, fill: muted)
    CUSTOMER – PROJECT · Software Requirements Specification
    #h(1fr) DOC-ID · vX.Y STATUS
    #v(-4pt)
    #line(length: 100%, stroke: 0.5pt + rule)
  ],
  footer: context [
    #line(length: 100%, stroke: 0.5pt + rule)
    #v(-4pt)
    #set text(7.5pt, fill: muted)
    CloudApper · Internal – not for external distribution
    #h(1fr) Page #counter(page).display("1 of 1", both: true)
  ],
)

#show heading.where(level: 1): it => {
  v(6pt)
  block(width: 100%, below: 8pt, stroke: (bottom: 1.2pt + navy), inset: (bottom: 4pt))[
    #set text(fill: navy, size: 14pt, weight: 600)
    #it
  ]
}
#show heading.where(level: 2): set text(fill: navy, size: 11.5pt, weight: 600)
#show heading.where(level: 3): set text(fill: navy, size: 10pt, weight: 600)

#set table(
  stroke: (x, y) => (bottom: 0.5pt + rule),
  fill: (x, y) => if y == 0 { rgb("#eef2f9") } else if calc.odd(y) { white } else { rgb("#fafbfd") },
  inset: (x: 5pt, y: 4pt),
)
#show table.cell.where(y: 0): set text(weight: 600, fill: navy)
#show table: set text(size: 8.5pt)
#set par(justify: false, leading: 0.62em)
