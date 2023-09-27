def main():
    file = input("File name: ").strip().lower()
    _, file_extension = file.rsplit('.', maxsplit = 1)
    if file_extension == "gif":
        print("image/gif")
    elif file_extension == "jpg" or file_extension == "jpeg":
        print("image/jpeg")
    elif file_extension == "png":
        print("image/png")
    elif file_extension == "pdf":
        print("application/pdf")
    elif file_extension == "txt":
        print("text/plain")
    elif file_extension == "zip":
        print("application/zip")
    elif file_extension == "bin":
        print("application/octet-stream")
if __name__ == "__main__":
    main()