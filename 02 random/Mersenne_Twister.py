# To start with we will use an external library

'''
/** JS example:
 * Returns a random int between
 * @param start inclusive
 * @param before exclusive
 */
export function randomInt(start, before){
}


import numpy as np
np.random.seed(42)

This creates and seeds a psuedorandom number generator - comment this out and it will become a random random number generator.

The purpose of the seeding is to make the test repeatable for running experiments with - so that others can validate them.

print(np.random.rand()) # as a test this will create a float between 0 and 1 using the .rand() method.
      
def rand_num_gen(low, high):
  # This is super simple and creates the numbers in a uniform distribution - random, binomial and normal are other distributions you can specify
    return np.random.randint(low, high)

print(rand_num_gen(0,1))
print(rand_num_gen(0,1))
print(rand_num_gen(0,1))
print(rand_num_gen(0,1))
print(rand_num_gen(0,10))
print(rand_num_gen(0,10))
print(rand_num_gen(0,10))
print(rand_num_gen(0,10))
'''
import random
l=1000
listrandom=[]
for i in range (l):
    value=random.randint(0,l)
    listrandom.append(value)
print(listrandom)
