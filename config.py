import os
from pathlib import Path

DATA_DIR = Path(os.environ.get("XDG_DATA_HOME") or Path.home() / ".local/share") / "spf"
DATA_DIR.mkdir(mode=0o755, parents=True, exist_ok=True)
