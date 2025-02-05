#!/usr/bin/env python3
# coding: utf-8

import sys
import argparse
import json
import yaml
import logging

# send log messages to stderr to avoid mixing with the output
stderr_handler = logging.StreamHandler(sys.stderr)
LOG_FORMAT = "%(filename)s - %(funcName)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.ERROR, format=LOG_FORMAT, handlers=[stderr_handler])
log = logging.getLogger(__name__)

def get_key(data: dict, key: str) -> str:
    if key in data:
        return data[key]
    for k, v in data.items():
        if isinstance(v, dict):
            item = get_key(v, key)
            if item:
                return item
        elif isinstance(v, list):
            for item in v:
                if isinstance(item, dict):
                    result = get_key(item, key)
                    if result:
                        return result
    return None

def main(arguments: any) -> int:
    parser = argparse.ArgumentParser(
        description="Read a key value from a JSON or YAML file",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("-f", "--file", required=True, default=sys.stdin, type=argparse.FileType("r",encoding='UTF-8'), help="Input file")
    parser.add_argument("-k", "--key", required=True,  type=str, help="Key to extract")

    args = parser.parse_args(arguments)

    key = args.key
    data = None

    try:
        log.info(f"Reading file: {args.file.name}")

        _, ext = args.file.name.split(".")
        if ext == "json":
            data = json.load(args.file)
        elif ext == "yaml" or ext == "yml":
            data = yaml.safe_load(args.file)
        else:
            log.error(f"Unsupported file format: {ext}")
            sys.exit(1)

        log.info(f"Extracting key: {key}")
        data = get_key(data, key)
        if data:
            log.info(f"Value: {data}")
            print(data)
            sys.exit(0)
        else:
            log.warn(f"Key '{key}' not found")

    except Exception:
        log.exception("An error occurred", exc_info=True)
        sys.exit(1)

    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))