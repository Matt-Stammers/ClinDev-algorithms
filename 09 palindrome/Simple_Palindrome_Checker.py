# simple:

def characters(x):
  x = str(x)
  return [str(y) for y in x]

def is_palindrome(x):
  chars = characters(x)
  for f, r in zip(chars,reversed(chars)):
    if f != r:
      return False
  return True
  
# even simpler!:

def is_palindrome(string):
    return str(string)[::-1] == str(string)
    
# or:

def is_palindrome(string):
  b = str(string)
  a = ' '.join(b)
  if a[::-1] == a:
    return True
  return False
  
# or:

def characters(x):
  x = str(x)
  return [str(y) for y in x]

def is_palindrome(x):
  chars = characters(x)
  for f, r in zip(chars,reversed(chars)):
    if f != r:
      return False
  return True
