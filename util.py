"""Multithreading util for copy and move files"""
import argparse
import shutil
import os
import logging
from concurrent.futures import ThreadPoolExecutor


logging.basicConfig(filename="log.log", level=logging.DEBUG)


def copy(src: list, dst: str, threads_amount: int) -> None:
    """Copy files or directory to the destination

    Args:
        src: list of files or directory to be moved
        dst: destination directory
        threads_amount: amount of threads
    """
    with ThreadPoolExecutor(threads_amount) as executor:
        for file in src:
            if os.path.isfile(file):
                executor.submit(shutil.copy, file, dst)
                logging.info("File %s is copied to %s", file, dst)
            elif os.path.isdir(file):
                path = dst + file.split("/")[-1]
                if not os.path.exists(path):
                    os.mkdir(path)
                executor.submit(shutil.copytree, file, path,
                                dirs_exist_ok=True)
                logging.info("Directory %s is copied to %s", file, dst)


def move(src: list, dst: str, threads_amount: int) -> None:
    """Move files or directory to the destination

    Args:
        src: list of files or directory to be moved
        dst: destination directory
        threads_amount: amount of threads
    """
    with ThreadPoolExecutor(threads_amount) as executor:
        for file in src:
            executor.submit(shutil.move, file, dst)
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
        copy(args.from_, args.to, args.threads)
    elif args.operation == "move":
        move(args.from_, args.to, args.threads)
    else:
        logging.error("Wrong operation")
