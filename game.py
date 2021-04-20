#!/usr/bin/python3
import os
import argparse
import random
from pathlib import Path


LEVEL1_DIR = "/root"
LEVEL2_DIR = "/level2"


def main():
    parser = argparse.ArgumentParser(description='Linux Trainer')
    parser.add_argument("command")
    args = parser.parse_args()
    config = get_config()

    if args.command == "init":
        init(config)
        return

    game_level = int(Path('/etc/gamelevel').read_text().strip())
    if args.command == "help":
        show_help(game_level, config)
    elif args.command == "check":
        if game_level == 1:
            run_status_level1(config)
        if game_level == 2:
            run_status_level2(config)
    else:
        raise Exception("unknown command", args.command)


def run_status_level1(config):
    os.chdir(LEVEL1_DIR)
    for f in config["good_files"]:
        if not os.path.exists(f):
            print(f"ERROR: Good file '{f}' is missing! You failed!")
            return

    nr_bad = get_file_count([x["file_name"] for x in config["bad_file_objects"]])
    if nr_bad:
        print(f"Bad files remaining: {nr_bad}")
    else:
        print(f"Congratulations!!! You have completed challenge 1 !!! Type 'level2' for next level.")


def run_status_level2(config):
    os.chdir(LEVEL2_DIR)
    num_virus_missing = 0
    for obj in config["bad_file_objects"]:
        file_type = obj["file_type"]
        if file_type == "virus":
            expected_path = to_bytes(file_type + "/") + to_bytes(obj["file_name"])
            if not os.path.exists(expected_path):
                num_virus_missing += 1
        elif file_type == "spam":
            expected_path = obj["file_name"]
            if not os.path.exists(expected_path):
                print(f"ERROR: A spam file is missing! You failed!")
                return

    if num_virus_missing:
        print(f"Virus files remaining: {num_virus_missing}")
    else:
        print("Congratulations!!! You have completed challenge 2 !!! You are a Linux Jedi!")


def get_file_type(file_id):
    if (file_id % 2 == 0):
        file_type = "spam"
    else:
        file_type = "virus"
    return file_type


def get_file_count(file_names):
    ret = 0
    for f in file_names:
        if os.path.exists(f):
            ret += 1
    return ret


def get_file_data(file_type):
    num_padding = random.randrange(3, 22)
    return file_type + "-" + ("x"*num_padding)


def to_bytes(s):
    if isinstance(s, str):
        return s.encode("utf-8")
    else:
        return s


def init(config):
    os.chdir(LEVEL1_DIR)
    for f in config["good_files"]:
        open(f, "w").close()
    for obj in config["bad_file_objects"]:
        with open(obj["file_name"], "w") as f:
            f.write(get_file_data(obj["file_type"]))

    os.mkdir(LEVEL2_DIR)
    os.mkdir(LEVEL2_DIR + "/virus/")
    os.chdir(LEVEL2_DIR)
    for obj in config["bad_file_objects"]:
        with open(obj["file_name"], "w") as f:
            f.write(get_file_data(obj["file_type"]))


def show_help(game_level, config):
    if game_level == 1:
        print(f"""
  ** Challenge Level 1 **"

  I created {len(config["bad_file_objects"])} bad files in your home directory (/root/).  Delete them.
  (The files are in the container, not in your real computer, don't worry)

  Do NOT delete these files: {", ".join(config["good_files"])}
""")
    elif game_level == 2:
        print(f"""
  ** Challenge Level 2 **"

  I created {len(config["bad_file_objects"])} bad files in /level2/.
  Some contain the word "virus" in their data, and the others contain "spam".
  Move the "virus" files to /level2/virus/, but don't rename them.
  Leave the "spam" files alone.
""")
    else:
        raise Exception("unknown gamelevel")


def get_config():
    bad_files = [
            "easy", "?", "~", "*", "-", "'", "[a]", "\"",
            ".*", "~*" "-", "--", "-rf", "-h",
            "\\\\", "\\",
            "文字化け", b"\xff\xff\xff",
            "\u00A0", " ",
            "\n", "\\t",
            "🐱‍💻",
            ]

    bad_file_objects = []
    for i, bad_file in enumerate(bad_files):
        bad_file_objects.append(dict(file_name=bad_file, file_type=get_file_type(i)))

    good_files = [
            "a", "b", "c",
            "db-backup",
            ".ssh_config",
            ]

    return dict(good_files=good_files, bad_file_objects=bad_file_objects)


if __name__ == "__main__":
    main()
