"""
One Word, First Thought — make.fun entry.

The first word that comes to mind: "petrichor".

It is the smell of rain on dry earth — one word that carries a whole
moment in it. Surprising rather than safe: nobody guesses it, yet
everyone recognises the feeling at once. Vivid and specific: it calls
up wet dust, a first drop on hot pavement, the air changing after a
storm. It has a soft, rain-like sound of its own, and it feels chosen,
not filler — a word picked because it means exactly one unmistakable
thing. No topic, no explanation, no second draft: the first word.
"""

import os

WORD = "petrichor"


def main():
    assert 1 <= len(WORD) <= 24, "word must be 1-24 characters"
    assert WORD.strip(), "word must not be only white space"
    assert len(WORD.split()) == 1, "entry must be exactly one word"
    assert WORD.isalpha(), "entry must be a plain word, no punctuation tricks"
    # The leaderboard breaks exact ties by fewer bytes, so pin the byte
    # size down too: one plain ASCII word, no trailing newline, no BOM.
    encoded = WORD.encode("utf-8")
    assert len(encoded) == len(WORD), "word must be plain ASCII, one byte per letter"
    assert len(encoded) <= 24, "word must be at most 24 bytes"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(encoded)


if __name__ == "__main__":
    main()
