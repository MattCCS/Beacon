
import json
import pathlib


HERE = pathlib.Path(__file__).parent.absolute()
CONFIG_PATH = HERE / "config.json"


CONFIG = None


def load_config():
    try:
        with open(CONFIG_PATH) as infile:
            return json.loads(infile.read())
    except Exception as exc:
        print(exc)
        return None


def ensure_config():
    global CONFIG
    if CONFIG is None:
        CONFIG = load_config() or {}


def load_contact():
    ensure_config()
    return CONFIG.get("contact", None)


def main():
    print(load_config())


if __name__ == '__main__':
    main()
