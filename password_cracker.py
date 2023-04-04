import hashlib


def crack_sha1_hash(hash, use_salts = False):
    arr = []
    crackedPassword = None
    fhand = open('top-10000-passwords.txt')
    for line in fhand:
      password = line.strip()
      arr.append(password)

    
    for word in arr:
      bword = word.encode()
      if use_salts is True:
        phand = open('known-salts.txt')
        for line in phand:
          salt = line.strip()
          salt = salt.encode()
          pre = hashlib.sha1(salt + bword).hexdigest()
          end = hashlib.sha1(bword + salt).hexdigest()
          if pre == hash or end == hash:
            crackedPassword = word
            break
      wordHashed = hashlib.sha1(bword).hexdigest()
      if wordHashed == hash:
        crackedPassword = word
        break

  
    if crackedPassword is None:
      return "PASSWORD NOT IN DATABASE"
    else:
      return crackedPassword
