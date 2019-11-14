import bcrypt
import os


def hashing(args):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(args.password.encode('utf8'),salt)
    file1 = open('specification-4/file1.txt', 'ab')
    file1.write(hashed)
    file1.write((os.linesep).encode('utf8'))
    file1.close()

