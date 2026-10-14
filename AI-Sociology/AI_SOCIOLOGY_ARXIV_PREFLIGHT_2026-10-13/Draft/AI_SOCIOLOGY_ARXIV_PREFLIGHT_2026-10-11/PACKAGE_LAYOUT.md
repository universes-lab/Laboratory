# Intended arXiv Source Bundle Layout

This is a layout declaration only. The final TeX/PDF cannot be frozen until Appendix A and metadata are approved.

```text
main.tex                 # XeLaTeX top-level file
article_en.tex           # frozen English article, technical conversion only
appendix_a.tex           # exact primary-evidence appendix
article_ru.tex           # approved Russian translation
article_nl.tex           # optional; if Author chooses 3-language v1
references.bib           # verified bibliography
README.txt               # source provenance / compile note, if needed
```

Compilation order in the resulting PDF:

1. English version
2. Appendix A belonging to the English version
3. Russian version
4. Dutch version, only if approved for inclusion in arXiv v1

No `anc/` directory is planned for full-text translations.
