# GitHub Wiki seed

These Markdown files are seed pages for the GitHub Wiki attached to `TojotheTerror/hermes-webui`.

The GitHub Wiki is stored separately from the main repository. Review these files in a normal pull request, then publish them by copying the pages into the Wiki UI or by pushing them to `TojotheTerror/hermes-webui.wiki`.

## Page map

| File | Wiki page |
| --- | --- |
| `Home.md` | Home |
| `Project-Setup.md` | Project Setup |
| `Build-Instructions.md` | Build Instructions |
| `Architecture-Overview.md` | Architecture Overview |
| `Contribution-Guide.md` | Contribution Guide |
| `Release-Notes.md` | Release Notes |
| `Troubleshooting.md` | Troubleshooting |

## Publishing with Git

After the wiki exists:

```bash
git clone git@github.com:TojotheTerror/hermes-webui.wiki.git
cp docs/wiki/*.md hermes-webui.wiki/
cd hermes-webui.wiki
git add .
git commit -m "Initialize Hermes Android wiki"
git push
```

Keep private machine names, private network details, credentials, tokens, cookies, API keys, and full local config dumps out of wiki pages.
