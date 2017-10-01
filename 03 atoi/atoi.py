'''
A common interview question is to write  a  function  that  converts  a  string  into  an  integer e.g. "123" => 123.  This  function  is commonly  called  atoi because  we  are  converting  an  ASCII  string  into  an  integer.
'''
import re
pattern = r'\-$d+'

def atoi(x):
    try:
        a = x.search(pattern)
    a = re.sub('r[A-Za-z]', '', x)
        return int(a)
    except:
        return 'NaN'
    
print(atoi('-1'))
print(atoi('A1'))
print(atoi('1A))
print(atoi('-1'))
