import argparse
import shutil
import os


def copy(src: str, dst: str) -> None:
    """Copy file or directory to the destination

    Args:
        src: file or directory to be moved
        dst: destination directory
    """
    if os.path.isfile(src):
        shutil.copy(src, dst)
    elif os.path.isdir(src):
        shutil.copytree(src, dst)
    else:
        print("error")  # todo log, permission error


def move(src: str, dst: str) -> None:
    """Move file or directory to the destination

    Args:
        src: file or directory to be moved
        dst: destination directory
    """
    shutil.move(src, dst)
    # todo logging


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--operation", type=str, help="move or copy")
    parser.add_argument("--from", dest="from_", type=str,
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
        pass  # todo log error
