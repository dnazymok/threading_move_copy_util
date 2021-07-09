"""Multithreading util for copy and move files"""
import argparse
import shutil
import os
import logging
from threading import Thread


logging.basicConfig(filename="log.log", level=logging.DEBUG)


def copy(src: list, dst: str) -> None:
    """Copy files or directory to the destination

    Args:
        src: list of files or directory to be moved
        dst: destination directory
    """
    for file in src:
        if os.path.isfile(file):
            thread = Thread(target=shutil.copy, args=(file, dst))
            thread.start()
            logging.info("File %s is copied to %s", file, dst)
        elif os.path.isdir(file):
            path = dst + file.split("/")[-1]
            os.mkdir(path)
            thread = Thread(target=shutil.copytree, args=(file, path),
                            kwargs={"dirs_exist_ok": True})
            thread.start()
            logging.info("Directory %s is copied to %s", file, dst)


def move(src: list, dst: str) -> None:
    """Move files or directory to the destination

    Args:
        src: list of files or directory to be moved
        dst: destination directory
    """
    for file in src:
        thread = Thread(target=shutil.move, args=(file, dst))
        thread.start()
        logging.info("File %s is moved to %s", file, dst)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--operation", type=str, help="move or copy")
    parser.add_argument("--from", nargs="*", dest="from_", type=str,
                        help="source file or directory")
    parser.add_argument("--to", type=str,
                        help="destination directory")
    parser.add_argument("--threads", type=int, default=1,
                        help="amount or threads")
    args = parser.parse_args()
    if args.operation == "copy":
        copy(args.from_, args.to)
    elif args.operation == "move":
        move(args.from_, args.to)
    else:
        logging.error("Wrong operation")
