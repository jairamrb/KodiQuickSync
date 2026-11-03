# Kodi QuickSync

A Kodi add-on that triggers a library scan (video and/or music) on demand. It does the same thing as Kodi's **Update library on startup** option, but whenever you want.

It only scans sources that have a **content type** (scraper) set. Folders with no content type are skipped, the same as in Kodi's own scan. When the scan finishes, the add-on shows a summary of what was added to each library.

- Repository: <https://github.com/jairamrb/KodiQuickSync>
- Add-on ID: `script.program.quicksync`
- Requires Kodi 19 (Matrix) or later, Python 3.

## Features

- Manual scan of the video library, the music library, or both.
- Uses Kodi's native scan (`UpdateLibrary`), so your scrapers, exclusions and settings apply.
- Checks whether a scan is already running so two scans never start at once.
- Final summary with the total size of each library and how many items are new.
- **English** and **Spanish** interface (it follows Kodi's language).

## Installation

### From a ZIP

1. Build the ZIP with `python3 tools/build_zip.py` (or download it from the releases).
2. In Kodi, go to **Add-ons → Install from zip file**.

### Manual

Copy the `script.program.quicksync/` folder into the `addons` folder of your Kodi installation and restart Kodi.

## Usage

- Go to **Add-ons → Program add-ons → Kodi QuickSync** and select it to run it.
- You can also add it to **Favourites** (context menu → *Add to favourites*) to launch it from the home screen in one click.
- While the scan runs, Kodi shows its progress in the top-right corner and you can keep using Kodi.

## Settings

| Setting | Description | Default |
|---|---|---|
| Scan video library | Scans video sources that have a content type set | Yes |
| Scan music library | Scans music sources that have a content type set | Yes |
| Show summary when finished | Shows the summary in a dialog. When off, only a notification is shown | Yes |

## Translations

Strings are in `script.program.quicksync/resources/language/resource.language.<lang>/strings.po`. To add a language, copy the `resource.language.en_gb` folder, rename it with the right language code and translate the `msgstr` entries.

## Building the ZIP

```bash
python3 tools/build_zip.py
```

This creates `dist/script.program.quicksync-<version>.zip`, ready to install in Kodi.

## Layout

```
.
├── LICENSE.txt
├── README.md
├── tools/
│   └── build_zip.py
└── script.program.quicksync/
    ├── LICENSE.txt
    ├── addon.xml
    ├── addon.py
    └── resources/
        ├── icon.png
        ├── fanart.jpg
        ├── screenshot-01.jpg … screenshot-04.jpg
        ├── settings.xml
        ├── lib/
        │   └── quicksync.py
        └── language/
            ├── resource.language.en_gb/strings.po
            └── resource.language.es_es/strings.po
```

## License

GPL-2.0-or-later. See [LICENSE.txt](LICENSE.txt).
