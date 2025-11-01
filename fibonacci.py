"""Command-line tool to display a Fibonacci sequence.

Usage:
    python fibonacci.py --count 10

This will print the first 10 Fibonacci numbers as a space-separated
sequence. Use ``--max`` to print all Fibonacci numbers up to that value
instead.
"""

from __future__ import annotations

import argparse
from typing import Iterable, List


def fibonacci_sequence(count: int | None = None, maximum: int | None = None) -> Iterable[int]:
    """Generate a Fibonacci sequence.

    You must provide either ``count`` (number of terms to generate)
    or ``maximum`` (largest value that should appear in the sequence).
    If both are provided, ``count`` takes precedence.

    Args:
        count: Number of Fibonacci numbers to generate.
        maximum: Largest value to include in the sequence.

    Yields:
        Fibonacci numbers starting from 0.

    Raises:
        ValueError: If neither ``count`` nor ``maximum`` is provided,
            or if a non-positive value is supplied.
    """

    if count is None and maximum is None:
        raise ValueError("Either count or maximum must be provided.")

    if count is not None:
        if count <= 0:
            raise ValueError("count must be a positive integer")
        remaining = count
    else:
        if maximum is None or maximum < 0:
            raise ValueError("maximum must be a non-negative integer")
        remaining = None

    a, b = 0, 1
    while True:
        if remaining is not None:
            if remaining == 0:
                break
            remaining -= 1
        elif maximum is not None and a > maximum:
            break

        yield a
        a, b = b, a + b


def parse_args(argv: List[str] | None = None) -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Display a Fibonacci sequence")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--count",
        type=int,
        help="Number of Fibonacci numbers to display",
    )
    group.add_argument(
        "--max",
        dest="maximum",
        type=int,
        help="Largest Fibonacci number to display",
    )

    return parser.parse_args(argv)


def main(argv: List[str] | None = None) -> None:
    """Entry point for the CLI."""
    args = parse_args(argv)
    sequence = list(fibonacci_sequence(count=args.count, maximum=args.maximum))
    print(" ".join(str(num) for num in sequence))


if __name__ == "__main__":
    main()
