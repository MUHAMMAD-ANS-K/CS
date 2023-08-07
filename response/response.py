from validator_collection import checkers

def main():
    print(valid(input('Email: ')))

def valid(email)
    email_true = checkers.is_email(email)
    if email_true:
        return 'Valid'
    else:
        return 'Invalid'

if __name__ == '__main__':
    main()