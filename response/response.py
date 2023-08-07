from validator_collection import checkers

email = input('Email: ')
email_true = checkers.is_email(email)
if email_true:
    print('Valid')