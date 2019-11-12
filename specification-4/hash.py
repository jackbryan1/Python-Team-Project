import bcrypt

def hashing(args):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(args.password,salt)

    print(hashed)
