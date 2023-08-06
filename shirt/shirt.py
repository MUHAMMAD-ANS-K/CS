import sys
from PIL import Image
import PIL


def main():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    try:
        file_read = sys.argv[1]
        im1 = Image.open(file_read)
        file1, extension1 = sys.argv[1].split('.')
        file2, extension2 = sys.argv[2].split('.')
        if not(extension1 == extension2):
            sys.exit('Input and output have different extensions')
    except ValueError:
        sys.exit()
    except FileNotFoundError:
        sys.exit("Input does not exist")
    shirt = Image.open("shirt.png")
    size = shirt.size
    muppet = PIL.ImageOps.fit(im1, size=size)
    muppet.paste(shirt, shirt)
    muppet.save(sys.argv[2])


if __name__ == "__main__":
    main()
