import yaml
from pathlib import Path

# Load scripts from YAML config
CONFIG_PATH = Path(__file__).parent.parent / "config" / "scripts.yaml"

with open(CONFIG_PATH) as f:
    CONFIG = yaml.safe_load(f)

SCRIPTS = CONFIG.get("scripts", [])

def parse_nmap_output(data):
    return data