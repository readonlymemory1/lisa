import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from lisa.ui.app import LisaApp


def main() -> None:
    LisaApp().run()


if __name__ == "__main__":
    main()
