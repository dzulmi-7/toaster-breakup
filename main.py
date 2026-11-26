import os

TEXT = "It's not me, it's you: I settings sourdough, bagel, and waffle, and four years you still just want toast."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
