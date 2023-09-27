def main():
    file = input("File name: ").strip()
    _, file_extension = file.split('.')
    if file_extension == "gif":
        print("image/gif")
    elif file_extension == "jpg" or "jpeg":
        print("image/jpeg")
    elif file_extension == "png":
        print("image/png")
    elif file_extension == "pdf":
        print("application/pdf")
    elif file_extension == "txt":
        print("text/plain")
    elif file_extension == "zip":
        print("application/zip")


if __name__ == "__main__":
    main()