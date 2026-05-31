# HubBase All Platforms (hbap-test)

Monorepo for all HubBase editions under [HubBase Authority](https://github.com/HubBase-Authority).

## Structure

| Directory | Contents |
|-----------|----------|
| `HubBase/` | Unified launcher (`Launcher.py`) — entry point for all editions |
| `bin/HB/` | HubBase (PC Edition) — `HubBase.py` v0.0.2.0.02 |
| `bin/HubBasePE/` | HubBasePE (Pocket Edition) — `Main.py` v0.0.2.0.01 |
| `bin/HBJE/` | HubBaseJE Python Port — `JsPort.py` |
| `bin/VB/` | Version Backlog — `VersionBacklog.py` |
| `bin/pc/` | Mirror of `bin/HB/HubBase.py` (backward compat) |
| `bin/pe/` | Mirror of `bin/HubBasePE/Main.py` (backward compat) |
| `bin/je/` | Original JS source files (`HB-JS.js`, `Extra-Code.js`) |
| `website/` | HubBase Authority website (HTML, CSS, JS) |
| `docs/` | Documentation (CODE_OF_CONDUCT, CONTRIBUTING, SECURITY) |

## Quick Start

### Using the launcher

```bash
python HubBase/Launcher.py
```

Options: `1` — HubBase PC, `2` — JsPort, `3` — Version Backlog

### Running individually

**HubBase (PC):**
```bash
python -m bin.HB.HubBase
```

**HubBasePE:**
```bash
python -m bin.HubBasePE.Main
```

**HubBaseJE (requires Node.js):**
```bash
node bin/je/HB-JS.js
```

## VIP Access

- Password: `5280`
- Usernames: `voice659`, `vhba`, `vipuser`, `hbaofficial`, `vvoice`, `voice`, `v`, `vip1`

## PE on PyPI

HubBasePE is published to PyPI at [pypi.org/project/HubBasePE](https://pypi.org/project/HubBasePE).

```bash
pip install HubBasePE
```

## Website

The website is live at [hubbase-authority.vercel.app](https://hubbase-authority.vercel.app).  
The `website/` folder contains the source for direct deployment.

## License

MIT — see [LICENSE](LICENSE).
