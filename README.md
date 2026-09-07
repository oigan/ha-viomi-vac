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

Local control, sensors, fan speed, water level and room cleaning work.

**Maps do not render yet.** The cloud session is valid and the map is listed
(`maps_listed=1`), but fetching the map blob fails before any decryption is attempted:

```
Map key inputs: brand=viomi wifi_sn='' mac= user_id=... device_id=... model=viomi.vacuum.v13
Map download failed (slot 0)
Map download failed (slot 1)
Map cycle: slot keys=['B', 'B'] active_id=1676290569 maps_listed=1
```

Empty `wifi_sn`/`mac` are **not** the cause — `required_map_key_inputs("viomi")` returns an
empty set, because the Viomi parser needs no local key material.

This build therefore carries **temporary diagnostic logging** (marked `DIAG` in
`cloud/connector.py`) that records the HTTP status of the map download and the raw response
of the interim-file-url call — both of which upstream discards. That logging is the only
change from upstream so far, and comes out once the cause is known.

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
