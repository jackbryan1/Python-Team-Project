import bcrypt


def hashing(args):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(args.password.encode('utf8'),salt)
    print(hashed)

