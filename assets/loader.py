import time
import sys

def show_loader():
    loader = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]",
              "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]",
              "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

    for frame in loader:
        sys.stdout.write(f"\rLoading {frame}")
        sys.stdout.flush()
        time.sleep(0.2)
    print("\n")
