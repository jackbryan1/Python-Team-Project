import bcrypt


def hashing(args):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(args.password.encode('utf8'),salt)
    file1 = open('specification-4/file1.txt', 'wb')
    print('h')
    file1.write(hashed)
    print('h')
    file1.close()

