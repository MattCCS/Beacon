
import pathlib
import subprocess


HERE = pathlib.Path(__file__).parent.absolute()
APPLESCRIPT_PATH = HERE / "sendText.applescript"


def send_message(to_number, message):
    out = subprocess.check_output(["osascript", "-l", "JavaScript", APPLESCRIPT_PATH, to_number, message])
    return out
