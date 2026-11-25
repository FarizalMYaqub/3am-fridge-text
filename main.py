#!/usr/bin/env python3
"""The 3AM Fridge Text — make.fun entry.

A smart fridge texts its owner at 3am. This program writes that one line
to /output/entry.txt (or the path in ENTRY_OUTPUT).

The line is fixed: the joke is the deliverable, so there is no randomness,
no input file and no network. The program only makes sure the text that
lands on disk is exactly the line, one line, within the 140-character cap,
and valid UTF-8.
"""

import os
import sys
import tempfile
from pathlib import Path

# The message, written once and kept as a single literal so the file on disk
# can never drift from the joke.
MESSAGE = (
    "It's 3am. The microwave gets a thank-you for 90 seconds of work. "
    "I've been humming since 2019."
)

MAX_CHARS = 140


class EntryError(ValueError):
    """Raised when the entry text breaks a gate rule."""


def check_text(text: str) -> str:
    """Enforce the gate: non-empty, one line, within the character cap."""
    if not isinstance(text, str):
        raise EntryError("entry text must be a string")
    if not text.strip():
        raise EntryError("entry text must not be blank")
    if "\n" in text or "\r" in text:
        raise EntryError("entry text must be a single line")
    if len(text) > MAX_CHARS:
        raise EntryError(
            f"entry text is {len(text)} characters, over the {MAX_CHARS} cap"
        )
    text.encode("utf-8")  # raises UnicodeEncodeError on bad input
    return text


def target_path() -> Path:
    """Where the entry goes: ENTRY_OUTPUT wins, else /output/entry.txt."""
    raw = os.environ.get("ENTRY_OUTPUT", "").strip()
    return Path(raw) if raw else Path("/output/entry.txt")


def publish(text: str, destination: Path) -> None:
    """Write atomically, then read the file back and compare byte for byte."""
    checked = check_text(text)
    destination.parent.mkdir(parents=True, exist_ok=True)
    payload = checked.encode("utf-8")
    handle, tmp_name = tempfile.mkstemp(
        dir=str(destination.parent), prefix=".entry-", suffix=".tmp"
    )
    try:
        with os.fdopen(handle, "wb") as handle_file:
            handle_file.write(payload)
            handle_file.flush()
            os.fsync(handle_file.fileno())
        os.replace(tmp_name, destination)
    except BaseException:
        try:
            os.unlink(tmp_name)
        except OSError:
            pass
        raise
    reread = destination.read_bytes()
    if reread != payload:
        raise EntryError("read-back mismatch after writing entry.txt")


def run() -> int:
    try:
        publish(MESSAGE, target_path())
    except (EntryError, OSError, UnicodeError) as problem:
        print(f"error: {problem}", file=sys.stderr)
        return 1
    print(f"wrote {len(MESSAGE)} characters to {target_path()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
