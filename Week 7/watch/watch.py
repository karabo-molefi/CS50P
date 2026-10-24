import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r"^<iframe\s?(?:width=\"\d+\")?\s?(?:height=\"\d+\")?\ssrc=\"https?://(?:www\.)?youtube.com/embed/(\w+)+\"\s?(?:title=\"Youtube video player\")?\s?(?:frameborder=\"\d+\")?\s?(?:allow=\"(?:(?:(?:\w|-)+);?\s?)+\")?\s?(?:allowfullscreen)?></iframe>$", s, re.IGNORECASE):
        return f"https://youtu.be/{matches.group(1)}"



if __name__ == "__main__":
    main()

#title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen>