import hashlib
from os import urandom 

__LOGIN__HASH__SALT__ = None
def set_salt(salt):
    assert salt is not None
    global __LOGIN__HASH__SALT__
    
    if __LOGIN__HASH__SALT__ is not None:
        raise Exception("Already declared login salt!")

    __LOGIN__HASH__SALT__ = salt.encode('utf-8')

def generate_password_hash(password):
    assert password is not None
    global __LOGIN__HASH__SALT__

    if __LOGIN__HASH__SALT__ is None:
        raise Exception("Please call the set_salt() method before")

    salthash = hashlib.sha256(__LOGIN__HASH__SALT__).hexdigest()
    return hashlib.sha512(salthash.encode('utf-8') + password.encode('utf-8') + __LOGIN__HASH__SALT__).hexdigest() 

def check_password_hash(password, password_hash):
   assert password_hash is not None
   global __LOGIN__HASH__SALT__

   if __LOGIN__HASH__SALT__ is None:
       raise Exception("Please call the set_salt() method before")

   return password_hash == generate_password_hash(password) 


if __name__ == '__main__':
    password = "asfdklsjdflkj1k23123"
    set_salt("!@#!@#!@#!@")
    password_hash = generate_password_hash(password)
    assert check_password_hash(password, password_hash)
