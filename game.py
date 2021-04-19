#!/usr/bin/python3
import os
import argparse

FILE_DIR = "/root"

BAD_FILES = [
        "?", "~", "*", "-", "'", "[a]", "\"",
        ".*", "~*" "-", "--", "-rf", "-h",
        "\\\\", "\\",
        "文字化け", b"\xff\xff\xff",
        "\u00A0", " ",
        "\t", "\\t",
        "🐱‍💻",
        ]

GOOD_FILES = [
        "a", "b", "c",
        "db-backup",
        ".ssh_config",
        ]

def main():
    parser = argparse.ArgumentParser(description='Linux Trainer')
    parser.add_argument("command")
    args = parser.parse_args()
    os.chdir(FILE_DIR)

    if args.command == "start":
        for f in BAD_FILES:
            open(f, "w").close()
        for f in GOOD_FILES:
            open(f, "w").close()

        print()
        print(f"  I created {len(BAD_FILES)} bad files in your home directory.  Delete them.")
        print(f"  (The files are in the container, not in your real computer, don't worry)")
        print()
        print("  Do NOT delete these files: ", ", ".join(GOOD_FILES))
        print()
    elif args.command == "status":
        run_status()
    elif args.command == "check":
        run_status(short=True)
    else:
        raise Exception("unknown command", args.command)


def run_status(short=False):
    for f in GOOD_FILES:
        if not os.path.exists(f):
            print(f" (ERROR: Good file '{f}' is missing! You failed!)")
            return

    nr_bad = 0
    for f in BAD_FILES:
        if os.path.exists(f):
            nr_bad += 1

    if nr_bad:
        print(f" ({nr_bad} bad files remaining)")
    else:
        print(f" (Congratulations!!! You have completed the challenge!!!)")


if __name__ == "__main__":
    main()
