# # # # # # # # # # # # #
#     REPEATED ITEM     #
# # # # # # # # # # # # #

'''
Find the repeated item in an array

Say you have an array that has at least one item repeated. How would you find the repeated item. This is a question commonly presented to beginner developers.

We start by creating our function which takes an array of type T and return the repeated item T if any.

Within the function we will throw an error if no item repetition is found.

Factors to keep in mind for higher scores:

Avoid using multiple loops, loop through all the items in the array once.
'''

def repeated_item_finder(array):
  item_list = []
  repeated_items = []
  if type(array) is not list:
    return print('This is not a list:{}, this program only accepts lists'.format(array))
  elif array == []:
    return print('Apologies this is an empty list:{}, please insert some content'.format(array))
  else:
    for item in array:
      if item not in item_list:
        item_list.append(item)
      elif item in item_list:
        repeated_items.append(item)
    try:
      if repeated_items == []:
        return print('There are no repeated items in this array. Here is your original array returned to you: {}'.format(item_list))
      else:
        return set(repeated_items) # this will return a set of the the repeated items
    except:
      return 'Apologies, Something has gone wrong! Ahhh!'
    
# Easy Tests    
test_array1 = ['a','c','a',1,2,1,1,3,'b'] # this will be used as the initial postive test case
test_array2 = [1,2,3,4,5,6] # this is the initial negative test case
print(repeated_item_finder(test_array1))
print(repeated_item_finder(test_array2))

# Tougher Tests
test_array3 = 'broken string' # this is an invalid input and should throw an error
test_array4 = [1,1,2,2,2,2,2,4,4,4,4,4,6,6,6,2,3,4,5,6,3.7,3.7,'a'] # this is a harder test with floats and multiple repetitions
print(repeated_item_finder(test_array3))
print(repeated_item_finder(test_array4))

# Even Tougher Tests
test_array5 = {1:4, 2:4, 1:4, 8:9} # this is an dict so it should throw an error
test_array6 = 'blob', # this is actually a tuple - again it should throw an error
print(repeated_item_finder(test_array5))
print(repeated_item_finder(test_array6))

# Long Arrays
test_array7 = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,'a','a','a','ab','ab','c','b','b'] # check it picks them all up
test_array8 = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,'a','a','a','ab','ab','c','b','b','c'] # check it picks them all up
print(repeated_item_finder(test_array7))
print(repeated_item_finder(test_array8))

# This is my pseudorandom array from before! This is why you wouldn't want to encrypt your device with it!
test_array9 = [] # check it picks up the empty list
test_array10 = [62, 297, 174, 515, 149, 858, 145, 581, 682, 370, 542, 364, 499, 560, 372, 92, 300, 76, 23, 920, 38, 366, 661, 157, 713, 531, 387, 14, 146, 29, 33, 533, 228, 240, 562, 502, 259, 437, 605, 518, 640, 325, 894, 543, 993, 772, 393, 945, 970, 687, 206, 742, 218, 289, 720, 263, 329, 689, 112, 39, 458, 164, 260, 7, 55, 756, 179, 975, 500, 280, 932, 840, 943, 517, 600, 109, 194, 592, 810, 174, 489, 79, 0, 27, 1, 846, 85, 510, 910, 57, 748, 971, 711, 192, 234, 581, 393, 932, 56, 499, 88, 840, 383, 342, 501, 649, 102, 268, 70, 598, 813, 268, 634, 19, 470, 574, 953, 996, 855, 630, 70, 220, 524, 982, 857, 490, 93, 844, 639, 353, 306, 605, 909, 201, 515, 919, 460, 987, 647, 910, 421, 453, 177, 405, 642, 445, 596, 861, 770, 967, 277, 692, 156, 529, 157, 57, 195, 769, 164, 618, 376, 952, 24, 171, 132, 483, 481, 442, 690, 359, 148, 656, 542, 456, 436, 556, 621, 419, 97, 777, 346, 409, 274, 495, 790, 589, 713, 592, 783, 656, 28, 564, 80, 818, 924, 473, 692, 275, 195, 578, 269, 76, 934, 516, 442, 754, 751, 853, 163, 110, 592, 754, 230, 528, 651, 244, 630, 45, 934, 179, 235, 892, 559, 750, 796, 224, 307, 407, 615, 87, 879, 567, 686, 61, 47, 988, 87, 766, 503, 700, 789, 642, 928, 748, 26, 817, 712, 475, 464, 163, 266, 723, 476, 4, 888, 338, 531, 687, 997, 380, 55, 778, 34, 817, 543, 994, 172, 361, 25, 659, 884, 509, 59, 735, 59, 670, 420, 761, 427, 12, 499, 323, 761, 223, 913, 56, 697, 180, 198, 263, 44, 235, 441, 92, 796, 104, 619, 605, 932, 621, 522, 764, 226, 956, 242, 591, 917, 758, 823, 132, 379, 810, 802, 267, 194, 924, 516, 757, 242, 477, 582, 930, 534, 473, 393, 644, 334, 117, 800, 523, 157, 37, 797, 579, 626, 434, 414, 487, 267, 514, 534, 453, 172, 977, 931, 156, 490, 707, 449, 835, 296, 702, 206, 553, 1, 973, 290, 735, 271, 399, 7, 554, 803, 752, 76, 915, 766, 378, 877, 746, 819, 151, 292, 470, 720, 192, 312, 147, 364, 266, 816, 427, 994, 629, 890, 536, 419, 896, 743, 109, 665, 710, 322, 23, 409, 982, 558, 52, 345, 975, 887, 154, 878, 730, 598, 550, 493, 50, 821, 293, 408, 998, 290, 160, 285, 588, 382, 850, 126, 930, 6, 800, 518, 990, 756, 359, 54, 926, 459, 883, 964, 298, 852, 198, 904, 663, 301, 173, 84, 175, 126, 769, 203, 68, 788, 489, 131, 672, 31, 526, 876, 757, 831, 666, 743, 809, 935, 276, 171, 483, 894, 958, 637, 670, 366, 486, 357, 1000, 357, 227, 715, 105, 365, 638, 767, 356, 651, 444, 508, 573, 428, 309, 329, 59, 615, 810, 277, 352, 365, 774, 611, 216, 13, 333, 924, 0, 136, 883, 146, 594, 935, 684, 761, 524, 681, 594, 51, 970, 476, 269, 272, 31, 465, 923, 470, 94, 188, 431, 564, 97, 483, 96, 736, 558, 495, 408, 207, 693, 791, 411, 942, 736, 818, 271, 402, 726, 864, 811, 392, 938, 289, 88, 386, 62, 477, 222, 435, 217, 48, 897, 177, 315, 136, 365, 897, 938, 332, 771, 313, 960, 44, 946, 512, 108, 20, 672, 973, 705, 243, 460, 350, 239, 142, 172, 587, 796, 561, 849, 932, 229, 269, 616, 342, 37, 784, 519, 737, 156, 920, 137, 343, 848, 983, 212, 905, 287, 185, 401, 152, 923, 339, 335, 228, 722, 578, 383, 862, 672, 187, 979, 263, 89, 692, 196, 854, 245, 171, 352, 595, 77, 632, 221, 103, 528, 591, 741, 75, 360, 692, 945, 699, 644, 409, 60, 283, 671, 235, 984, 761, 301, 445, 415, 404, 24, 908, 509, 598, 306, 454, 895, 780, 872, 56, 242, 32, 12, 819, 770, 757, 626, 567, 889, 257, 611, 1000, 713, 639, 595, 628, 452, 775, 89, 494, 521, 854, 308, 331, 90, 610, 612, 508, 135, 853, 101, 21, 57, 237, 928, 616, 75, 455, 85, 617, 188, 517, 88, 793, 923, 676, 602, 104, 809, 707, 822, 441, 225, 772, 151, 476, 654, 286, 802, 504, 927, 359, 957, 617, 195, 614, 973, 287, 893, 590, 567, 544, 976, 745, 585, 796, 590, 257, 173, 102, 180, 617, 609, 883, 712, 725, 137, 902, 526, 684, 554, 964, 413, 49, 566, 816, 705, 71, 741, 267, 885, 158, 292, 542, 235, 4, 132, 602, 135, 874, 579, 569, 116, 831, 190, 45, 751, 344, 446, 893, 715, 932, 495, 236, 521, 579, 450, 241, 736, 728, 994, 413, 457, 548, 917, 211, 432, 720, 437, 130, 770, 635, 771, 555, 52, 859, 722, 976, 838, 134, 340, 560, 133, 817, 222, 191, 243, 107, 980, 235, 981, 592, 15, 460, 637, 362, 472, 197, 207, 218, 497, 509, 752, 323, 440, 366, 220, 154, 549, 873, 37, 909, 589, 9, 641, 713, 742, 556, 236, 501, 421, 565, 103, 313, 458, 25, 893, 523, 504, 55, 521, 441, 883, 760, 417, 657, 862, 430, 151, 218, 439, 991, 196, 960, 462, 944, 551, 946, 993, 716, 870, 462, 38, 257, 449, 810, 459, 379, 258, 220, 278, 467, 974, 929, 883, 188, 981, 321, 518, 67, 172, 663, 141, 621, 352, 496, 380, 465, 394, 657, 30, 563, 22, 236, 136, 329, 204, 453, 951, 63, 574, 26, 131, 577, 675, 565, 533, 695, 126, 752, 137, 589, 631, 445, 39, 840, 381, 13, 929, 298, 665, 759, 564, 108, 708, 677, 269, 640, 350, 589, 21, 673, 819, 369, 26, 167, 759, 348, 567, 672, 881, 115, 900, 198, 545, 463, 291, 675, 764, 386, 51, 131, 840, 227, 855, 702, 592, 410, 713, 667, 846, 588, 703, 227, 332, 487, 79, 113, 449, 572, 979, 471, 870, 512, 192, 904, 20, 150, 477, 665, 1, 640, 522, 335, 12, 580] # Proof that even a pseudorandom number generator will make quite a few reps. This is because of the birthday effect.
print(repeated_item_finder(test_array9))
print(repeated_item_finder(test_array10))
