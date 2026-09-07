# Supported models

One:

| Brand | Model | Model string |
|-------|-------|--------------|
| Viomi | V13 | `viomi.vacuum.v13` |

Upstream [letitbe-dull/xiaomi-vac](https://github.com/letitbe-dull/xiaomi-vac) supports 67
models across ijai, Dreame, Viomi and Xiaomi. This build deliberately registers only the one
machine it runs on — see the README for why, and use upstream for anything else.

Adding a model back means restoring its profile in `spec/profiles/`, re-registering it in
`spec/registry.py`, re-adding its map parser to `manifest.json` requirements, and shipping its
Lottie shape under `www/lottie/`. All four are needed; the registry alone is not enough.
