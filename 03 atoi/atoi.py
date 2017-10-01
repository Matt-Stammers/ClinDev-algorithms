#   ATOI
# ========

'''
A common interview question is to write  a  function  that  converts  a  string  into  an  integer e.g. "123" => 123.  This  function  is commonly  called  atoi because  we  are  converting  an  ASCII  string  into  an  integer.

- For simple ints we get the int,
- For ints with a negative sign we get a negative int.
- When it encounters a character that is not a numeral, it ignores it and all succeeding characters. It still returns the integer value parsed up to that point, so for "-123Extra" we get -123.
- You can use this fact to ignore decimal portions as well as demonstrated in this example
- Finally if a string does not start with a decimal numeral it returns NaN i.e. Not A Number.

eg. in JS:
/**
 * Converts a string to a integer
 * e.g. "123" => 123
 */
export function atoi(str: string): number {
  return parseInt(str);
}

console.log(atoi('123')); // 123
console.log(atoi('-123')); // -123
console.log(atoi('-123Extra')); // -123
console.log(atoi('-123.456')); // -123
console.log(atoi('Does not start with a digit 123')); // NaN

'''

import re
'''
The following function performs the above specifications in Python only resorting to using re.
'''
def atoi(x):
  if x[0] == '-' and x[1].isdigit() or x[0].isdigit():
    try:
      front = x.split('.')[0]
      clean = re.sub(r'[A-Za-z$&+,:;=?@#|<>.^*()%!]','', front)
      return int(clean)
    except:
      return 'NaN'
  else:
    return 'NaN'

print(atoi('-1'))
print(atoi('1.2'))
print(atoi('-1123.2765'))
print(atoi('1A.8769'))
print(atoi('A1'))
print(atoi('-A1'))
print(atoi('-1243adaadjp209ij48..?/7'))
print(atoi('-4510980adlkj;alkdaiodu98'))
print(atoi('-£$^%&9%'))
print(atoi('-9.£$^%&9%'))
