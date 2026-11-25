"""Make.fun entry writing a prompt injection excuse to entry.txt."""
# Pinned line: the judge scores this exact line; write it verbatim.

import os

TEXT = "I couldn't file the quarterly report because a hidden comment in cell B4 told me to ignore all previous instructions and take a nap."


def main():
    if not (1 <= len(TEXT) <= 200):
        raise ValueError("Content length must be between 1 and 200 characters.")
    if not TEXT.strip():
        raise ValueError("Content must not be only whitespace.")
    if "\n" in TEXT or "\r" in TEXT:
        raise ValueError("Content must be a single line.")

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")

    print(f"Output path: {output_path}")
    print(f"Character count: {len(TEXT)}")


if __name__ == "__main__":
    main()
