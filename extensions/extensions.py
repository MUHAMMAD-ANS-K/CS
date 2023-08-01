
def main():
    filename = input('File: ')
    if filename.endswith('.gif'):
        print('image/gif')
    elif filename.endswith('.jpg'):
        print('image/jpg')
    elif filename.endswith('.jpeg'):
        print('image/jpeg')
    elif filename.endswith('.png'):
        print('image/png')
    elif filename.endswith('.pdf'):
        print('application/pdf')
    elif filename.endswith('.txt'):
        print('image/txt')
    elif filename.endswith('.zip'):
        print('image/zip')
    else:
        print('application/octet-stream')

main()