# QuickSync for Kodi

<a href="https://jairamrb.com"><img src="docs/jairamrb-logo.png" alt="jairamrb.com" width="48" align="right"></a>

Developed by [jairamrb.com](https://jairamrb.com).

A Kodi add-on that triggers a library scan (video and/or music) on demand. It does the same thing as Kodi's **Update library on startup** option, but whenever you want.

It only scans sources that have a **content type** (scraper) set. Folders with no content type are skipped, the same as in Kodi's own scan. When the scan finishes, the add-on shows a summary of what was added to each library.

- Website: <https://jairamrb.com/quicksync/>
- Repository: <https://github.com/jairamrb/KodiQuickSync>
- Add-on ID: `script.program.quicksync`
- Requires Kodi 20 (Nexus) or later.

## Features

- Manual scan of the video library, the music library, or both.
- Uses Kodi's native scan (`UpdateLibrary`), so your scrapers, exclusions and settings apply.
- Checks whether a scan is already running so two scans never start at once.
- Final summary with the total size of each library (movies, TV shows, episodes, music videos, artists, albums, songs) and how many items are new. A library that was not scanned says why. The summary window can close by itself after a countdown.
- Launch options to skip the on-screen summary or pick the libraries, for other add-ons, scripts and remote controls.
- Tells other add-ons and JSON-RPC clients when the scan starts and finishes, and what was added.
- **English** and **Spanish** interface (it follows Kodi's language).

## Installation

### From the official Kodi repository (recommended)

QuickSync is available in the official Kodi add-on repository, so updates arrive automatically.

1. In Kodi, go to **Add-ons** and open the **Add-on browser** (box icon).
2. Choose **Install from repository → Kodi Add-on repository → Program add-ons**.
3. Select **QuickSync** and press **Install**.

### From a ZIP

1. Build the ZIP with `python3 tools/build_zip.py` (or download it from the releases).
2. In Kodi, go to **Add-ons → Install from zip file**.

### Manual

Copy the `script.program.quicksync/` folder into the `addons` folder of your Kodi installation and restart Kodi.

## Usage

- Go to **Add-ons → Program add-ons → QuickSync** and select it to run it.
- You can also add it to **Favourites** (context menu → *Add to favourites*) to launch it from the home screen in one click.
- While the scan runs, Kodi shows its progress in the top-right corner and you can keep using Kodi.

## Settings

Kodi only has a video library and a music library. Pictures have no library, so for them the add-on walks the picture sources, counts the files with the extensions Kodi shows, and compares the total with the previous run (saved in the add-on data folder). The first run only takes the count.

| Setting | Description | Default |
|---|---|---|
| Scan video library | Scans video sources that have a content type set | Yes |
| Scan music library | Scans music sources that have a content type set | No |
| Look for new pictures | Counts the files in the picture sources and shows how many are new | No |
| Show summary when finished | Shows the summary in a dialog. When off, only a notification is shown | Yes |
| Close the summary automatically | Closes the summary after a countdown shown in the window. Pressing up or down stops it | Yes |
| Seconds before closing | Length of the countdown (5 to 120) | 15 |

The *About* section has a **Look for new content now** button that runs the scan straight from the settings.

## Launching it from other add-ons or remotely

Options are passed as `key=value` and override the settings for that run:

| Option | Values | Default |
|---|---|---|
| `report` | `dialog` (summary dialog), `notification` (a toast), `none` (nothing on screen) | From *Show summary when finished* |
| `library` | `video`, `music`, `pictures`, `all` | From the *Libraries* settings |

From a skin, a favourite, a keymap or another add-on:

```
RunScript(script.program.quicksync,report=none,library=video)
```

Through JSON-RPC (for example from a web page or a phone app):

```json
{"jsonrpc": "2.0", "id": 1, "method": "Addons.ExecuteAddon",
 "params": {"addonid": "script.program.quicksync", "params": ["report=none", "library=video"]}}
```

If a scan is already running, a new launch does nothing (with `report=none`, not even a notification).

### Notifications

The add-on announces its progress with `JSONRPC.NotifyAll`, sent by `script.program.quicksync`. JSON-RPC clients receive `Other.OnScanStarted` and `Other.OnScanFinished`; service add-ons get them in `xbmc.Monitor.onNotification(sender, method, data)`.

```json
{"status": "done", "libraries": ["video"], "new": 3, "added": {"movies": 2, "tvshows": 0, "episodes": 1}}
```

`OnScanStarted` carries `{"libraries": [...]}`. When no library is selected, `OnScanFinished` carries `{"status": "nothing-selected"}`.

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
├── docs/
│   └── jairamrb-logo.png
├── tools/
│   └── build_zip.py
└── script.program.quicksync/
    ├── LICENSE.txt
    ├── addon.xml
    ├── addon.py
    └── resources/
        ├── icon.png
        ├── fanart.jpg
        ├── screenshot-01.jpg … screenshot-03.jpg
        ├── settings.xml
        ├── skins/default/
        │   ├── 1080i/script-quicksync-summary.xml
        │   └── media/quicksync-white.png
        ├── lib/
        │   └── quicksync.py
        └── language/
            ├── resource.language.en_gb/strings.po
            └── resource.language.es_es/strings.po
```

## Author

Developed by [jairamrb.com](https://jairamrb.com).

## License

GPL-2.0-or-later. See [LICENSE.txt](LICENSE.txt).
