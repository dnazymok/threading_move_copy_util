import argparse
import shutil
import os


def copy(src: list, dst: str) -> None:
    """Copy files or directory to the destination

    Args:
        src: list of files or directory to be moved
        dst: destination directory
    """
    for file in src:
        if os.path.isfile(file):
            shutil.copy(file, dst)
        elif os.path.isdir(file):
            path = dst + file.split("/")[-1]
            os.mkdir(path)
            shutil.copytree(file, path, dirs_exist_ok=True)
        else:
            print("error")  # todo log, permission error


def move(src: list, dst: str) -> None:
    """Move files or directory to the destination

    Args:
        src: list of files or directory to be moved
        dst: destination directory
    """
    for file in src:
        shutil.move(file, dst)
    # todo logging


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--operation", type=str, help="move or copy")
    parser.add_argument("--from", nargs="*", dest="from_", type=str,
                        help="source file or directory")
    parser.add_argument("--to", type=str,
                        help="destination directory")
    parser.add_argument("--threads", type=int, help="amount or threads",
                        default=1)
    args = parser.parse_args()
    if args.operation == "copy":
        copy(args.from_, args.to)
    elif args.operation == "move":
        move(args.from_, args.to)
    else:
        print("error")  # todo log error
