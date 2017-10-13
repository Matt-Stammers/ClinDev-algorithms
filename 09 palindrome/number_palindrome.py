# import unittest

# The function below can check if a number is a palindrome and returns a bool.

def digits(x):
  
  digs = []
  while x != 0:
    div, mod = divmod(x,10)
    digs.append(mod)
    x = div
  return digs

def is_palindrome(x):
  digs = digits(x)
  for f, r in zip(digs,reversed(digs)):
    if f != r:
      return False
  return True
  
print(is_palindrome(1234)) # will return False
print(is_palindrome(1234321)) # will return True
print(is_palindrome(3456789)) # will return False
print(is_palindrome(6789876)) # will return True

# for strings:

def characters(x):
  return [y for y in x]

def is_palindrome(x):
  chars = characters(x)
  for f, r in zip(chars,reversed(chars)):
    if f != r:
      return False
  return True

'''
class Tests(unittest.TestCase):
  def test_negative(self):
    self.assertFalse(is_palindrome(1234))
  
  def test_positive(self):
    self.assertTrue(is_palindrome(1234321))
  
  def single_digit(self):
    for i in range(10):
      self.assertTrue(True, is_palindrome(i))

'''

# For pdb debugging      
# if name == __main__:
#   unittest.main()
