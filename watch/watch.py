import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    match = re.search(r'<iframe(.+)? src="https?://(www\.)?youtube.com/embed(/\w+)"(.+)?></iframe>',s)
    if match:
        return 'https://youtu.be' + match.group(3)
    else:
        return None


<iframe width="560" height="315" src="https://www.youtube.com/embed/OmJ-4B-mS-Y" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


if __name__ == "__main__":
    main()