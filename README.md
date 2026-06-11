# Biblije: statički sajt

Statički web sajt napravljen od markdown priručnika u [`docs/`](docs/). Sadrži tri knjige:

| Knjiga | Poglavlja | Izvor |
|---|---|---|
| **Claude Code Biblija**: od ideje do digitalnog proizvoda | 16 | `docs/biblija-parts/` |
| **Marketing Biblija** za SaaS | 15 | `docs/marketing-parts/` |
| **Top 5% Edukator**: mentorski priručnik | 10 | `docs/edukator-parts/` |

## Kako radi

Markdown fajlovi se pretvaraju u statičke HTML stranice (pandoc), sa bočnom navigacijom,
sadržajem po strani (TOC), prev/next navigacijom i svetlom/tamnom temom. Izlaz ide u
[`site/`](site/) i automatski se objavljuje na GitHub Pages preko GitHub Actions-a
([`.github/workflows/deploy.yml`](.github/workflows/deploy.yml)).

Sajt nije indeksiran od strane pretraživača (`noindex` + `robots.txt`).

## Ponovno generisanje sajta

```bash
python3 build.py
```

Zahteva [pandoc](https://pandoc.org/) i Python 3. Skripta čita poglavlja iz `docs/`,
generiše HTML u `site/`, a commit na `main` granu pokreće deploy na GitHub Pages.
