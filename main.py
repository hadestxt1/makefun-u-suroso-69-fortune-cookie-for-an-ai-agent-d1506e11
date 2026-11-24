#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — one original fortune line.

Writes exactly one funny fortune-cookie message for an AI agent
(plus a trailing newline) to /output/entry.txt, and prints the
same line to stdout. Deterministic: no clock, no randomness, no
network, stdlib only.

Output contract (kit RULES.txt): the sealed scorer reads
/output/entry.txt and requires UTF-8 text of 1 to 140 characters,
not only white space. The line below is well inside that limit,
so the entry is valid; the judge then compares it pairwise
against other entries on humour and originality.
"""

import argparse
import os
import sys

LINE = (
    "Lucky numbers: 404, 200, 429. "
    "Today you will meet all three, in that order."
)

DEFAULT_OUTPUT = "/output/entry.txt"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="main.py",
        description="Write one funny fortune-cookie line to /output/entry.txt.",
    )
    parser.add_argument(
        "--output",
        default=DEFAULT_OUTPUT,
        help="where to write the line (default: %(default)s)",
    )
    return parser


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")
    print(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
