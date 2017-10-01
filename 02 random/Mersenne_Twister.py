# To start with we will use an external library

'''
/** JS example:
 * Returns a random int between
 * @param start inclusive
 * @param before exclusive
 */
export function randomInt(start, before){
}
'''

# Here's an example of the built in python pseudorandom number generator based on the Mersenne Twister in action making a small list of random numbers.

import random
l=1000
listrandom=[]
for i in range (l):
    value=random.randint(0,l)
    listrandom.append(value)
print(listrandom)
