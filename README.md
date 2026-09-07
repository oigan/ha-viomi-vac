# Viomi Vacuum (V13) for Home Assistant

A derivative of [letitbe-dull/xiaomi-vac](https://github.com/letitbe-dull/xiaomi-vac),
narrowed to a single machine: a **Viomi V13** (`viomi.vacuum.v13`).

Upstream supports 67 models across ijai, Dreame, Viomi and Xiaomi. This copy exists because
map support upstream is hardware-verified only on `ijai.v17`, and does not currently work on
this Viomi — so the code needs changes that only make sense for one model.

> This is not a competing project. If you own any other vacuum, use
> [the original](https://github.com/letitbe-dull/xiaomi-vac); it is broader, better tested,
> and actively maintained. Fixes found here are meant to go back upstream.

## Status

Working: local control, sensors, fan speed, water level, room cleaning, **and the map**.

### The map needs the vacuum to move first

A docked Viomi never uploads a map to the cloud, and the Mi Home app shows the *local* map, so
nothing hints that the cloud copy is missing. `get_interim_file_url` makes it worse by minting a
signed URL for an object that does not exist; only the download reveals it:

```
HTTP 404 Object Not Found: Make sure your object exist in current region,
object name: <user_id>/<device_id>/0, region=awsde0
```

If `camera.<name>_map` is `unavailable`, call **`xiaomi_vac.refresh_map`** (with
`confirm_movement: true`). It drives the vacuum off the dock briefly so it uploads, then
re-docks it. Any normal clean does the same.

Two things this is *not*, both checked here so nobody repeats them:

- Empty `wifi_sn` / `mac` in the debug log are normal — `required_map_key_inputs("viomi")` is
  an empty set; only ijai needs key material.
- The fixed slots `"0"` / `"1"` are correct. Once a real upload existed, slot `"0"` returned
  HTTP 200, while the map-list `name` and `id` kept 404ing.

## What was removed

| Removed | Kept |
|---------|------|
| ijai, Dreame, Roidmi and Xiaomi profiles (66 models) | `viomi.vacuum.v13` |
| Their four map-parser dependencies | `vacuum-map-parser-viomi`, `-base` |
| 64 of 68 Lottie shapes (5.6 MB to 400 KB) | `shape-11-*`, the V13 artwork |
| `xiaomi_json_decrypt.py` and the ijai `_parse_rooms` monkeypatch | the shared map pipeline |
| The test suite | — |

The shared dispatch code in `map_parsers.py` is left intact even where it is now unreachable:
its parser imports are lazy, so it costs nothing at runtime, and keeping it makes merges from
upstream far less painful. Dropping the test suite is a real loss of safety net when merging —
upstream's is still reachable through the `upstream` remote.

## Relationship to upstream

The full upstream history is not preserved here, but upstream is wired as a git remote so
fixes can still be pulled selectively:

```bash
git remote add upstream https://github.com/letitbe-dull/xiaomi-vac.git
git fetch upstream
```

The integration domain is deliberately still `xiaomi_vac`, so an existing config entry,
device and entity IDs survive switching between this build and upstream.

## Installation

HACS → three-dot menu → Custom repositories → `oigan/ha-viomi-vac`, category *Integration*.
Then install, restart Home Assistant.

## License

MIT, inherited from upstream. `LICENSE` retains the original copyright of
letitbe-dull; see it for the full text.
