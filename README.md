<div align="center">

<pre>
   ____  ____  ___  ____    ___   ___  ____    _
  / __ \/ __ \/ _ \/ __ \  / _ \ / _ \|  _ \  / \
 / /_/ / /_/ /  __/ / / / | | | | | | | | | |/ _ \
/_____/ .___/\___/_/ /_/  | |_| | |_| | |_| / ___ \
      /_/                   \___/ \___/|____/_/   \_\
</pre>

### openOODA — Capability-Secure Computing Stack (L0–L7)

[openooda.org](https://openooda.org) • [@openOODA](https://github.com/openOODA)

</div>

---

## This Repository (`status`)

Public status site served at [status.openooda.org](https://status.openooda.org) via
GitHub Pages (`CNAME`, `.nojekyll`).

- `index.html` — the live telemetry page (auto-refreshes every 300 s). It is
  **generated**, not hand-edited: `openOODA/buildbox/eco/status_sync/sync_status.oo`
  emits the page from fleet telemetry and commits the result here.
- `VERSION` — repository version (semver per `openOODA/rules.oot` §1.21).
- `anchor.oo` — agent-facing anchor describing the repo's role.
- `qa/seal.oo`, `tests/test_status.oo` — governance seal and the compiled probe
  (`bin/test_status`) verifying page integrity and uptime claims.

There is no build step and no CLI surface; changes land through the sync generator.

License: Apache-2.0 (org default; no LICENSE file is carried in this repo).
