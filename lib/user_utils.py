import random
import string
import hashlib
import hmac

def make_pw_hash(name, pw, salt = None):
    if not salt:
        salt = make_salt()
    h = hashlib.sha256(name + pw + salt).hexdigest()
    return '%s|%s' % (h,salt)

def make_salt():
    return ''.join(random.choice(string.letters) for _ in xrange(10))

def valid_pw(name, pw, h):
    salt = h.split('|')[1]
    return h == make_pw_hash(name, pw, salt)


SECRET = 'imsosecret'
def hash_str(s):
    return hmac.new('imsosecret', s).hexdigest()

def make_secure_val(s):
    return "%s|%s" % (str(s), hash_str(str(s)))

def check_secure_val(h):
    h = str(h)
    val = h.split('|')[0]
    if h == make_secure_val(val):
        return val