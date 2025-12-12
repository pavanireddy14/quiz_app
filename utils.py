import time
import sys

def colored(text, color):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "cyan": "\033[96m",
        "reset": "\033[0m"
    }
    return f"{colors[color]}{text}{colors['reset']}"

def progress_bar(duration=3):
    for i in range(31):
        time.sleep(duration/30)
        sys.stdout.write("\rLoading: [" + "#" * i + " " * (30-i) + "]")
        sys.stdout.flush()
    print("\n")

