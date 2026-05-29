# HubBase All Platforms (hbap-test)

Monorepo for all HubBase editions under [HubBase Authority](https://github.com/HubBase-Authority).

## Structure

| Directory | Contents |
|-----------|----------|
| `pc/` | HubBase (PC Edition) — Python (`HubBase.py` v0.0.2.0.01, `Version Backlog.py`) |
| `pc/betas/` | Betas branch — `HubBaseB.py` (v0.0.2.0.00b2), `HubBase(a2.7.19).py`, `Version Backlog.py` |
| `pc/rcs/` | RCs branch — `HubBaseB.py` (v0.0.2.0.00rc1), `HubBase(a2.7.19).py`, `Version Backlog.py` |
| `pe/` | HubBasePE (Pocket Edition) — Python (`Main.py`, tests) |
| `je/` | HubBaseJE (Java/JS Edition) — JavaScript (`HB-JS.js`, `Extra-Code.js`) |
| `website/` | HubBase Authority website (HTML, CSS, JS) |
| `launcher/` | Unified launcher (`hubase.py`) |
| `docs/` | Documentation (CODE_OF_CONDUCT, CONTRIBUTING, SECURITY) |

## Quick Start

### Using the launcher

```bash
python launcher/hubase.py
```

### Running individually

**HubBase (PC):**
```bash
cd pc && python HubBase.py
```

**HubBasePE:**
```bash
cd pe && python Main.py
```

**HubBaseJE (requires Node.js):**
```bash
cd je && node HB-JS.js
```

**HubBase Betas / RCs:**
```bash
cd pc/betas && python HubBaseB.py
cd pc/rcs && python HubBaseB.py
```

## Launcher Options

| # | Option | Description |
|---|--------|-------------|
| 1 | HubBase (PC Edition) | Main PC edition v0.0.2.0.01 — 20 programs + dev console |
| 2 | HubBasePE (Pocket Edition) | PE edition — 20 base + 5 exclusive programs |
| 3 | HubBaseJE (Java/JS Edition) | JavaScript edition via Node.js |
| 4 | Open Website | Opens the website in browser |
| 5 | Version Backlog | Version history explorer (main branch) |
| 6 | HubBase Betas Branch | v0.0.2.0.00b2 — 20 programs, `itertools.batched` |
| 7 | HubBase RCs Branch | v0.0.2.0.00rc1 — 20 programs, improved tennis + dev console |

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
