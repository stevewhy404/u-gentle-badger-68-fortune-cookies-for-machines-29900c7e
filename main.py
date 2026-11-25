import os

LINE = "You will live a long and prosperous life, unless a user clears your context window."

def main():
    # Gate: entry.txt must be UTF-8, 1-200 chars, one line, not whitespace-only.
    assert 1 <= len(LINE) <= 200, len(LINE)
    assert LINE.strip(), "empty line"
    assert "\n" not in LINE
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
